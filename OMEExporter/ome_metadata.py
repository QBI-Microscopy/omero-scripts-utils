#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ome_xml
from ome import OMEBase       

shapes = {"Rect":ome_xml.Rectangle,"Ellipse":ome_xml.Ellipse,"Polygon":ome_xml.Polyline}

class OMEExporter(OMEBase):

    def __init__(self,conn=None,source=None,input_dir=None,filename=None,box=None,theZ=None,theC=None,theT=None,ROI=None):
        OMEBase.__init__(self)
        self.store = ome_xml.OME()
        self.conn = conn
        self.source = source
        self.input_dir = input_dir
        self.filename = filename
        self.box = box
        if source:
            if box:
                self.sizeX = int(box[2])
                self.sizeY = int(box[3])
            else:
                self.sizeX = int(source.getSizeX())
                self.sizeY = int(source.getSizeY())
            if theZ is not None:
                if isinstance(theZ,list):
                    self.sizeZ = len(theZ)
                    self.slicesZ = theZ
                else:
                    self.sizeZ = 1
                    self.slicesZ = [theZ]
            else:
                self.sizeZ = int(source.getSizeZ())
                self.slicesZ = range(self.sizeZ)
            if theC is not None:
                if isinstance(theC,list):
                    self.sizeC = len(theC)
                    self.slicesC = theC
                else:
                    self.sizeC = 1
                    self.slicesC = [theC]
            else:
                self.sizeC = int(source.getSizeC())
                self.slicesC = range(self.sizeC)
            if theT is not None:
                if isinstance(theT,list):
                    self.sizeT = len(theT)
                    self.slicesT = theT
                else:
                    self.sizeT = 1
                    self.slicesT = [theT]
            else:
                self.sizeT = int(source.getSizeT())
                self.slicesT = range(self.sizeT)
                
            self.roi_count = 0
            if ROI:    
                self.ROI = ROI
                self.roi_count = len(ROI)
                
            self.Xres = source.getPrimaryPixels().getPhysicalSizeX()
            self.Yres = source.getPrimaryPixels().getPhysicalSizeY()
            self.Zres = source.getPrimaryPixels().getPhysicalSizeZ()
            print 'xres,yres,zres:',self.Xres,self.Yres,self.Zres
            self.dtype = source.getPixelsType()
            print 'dtype',type(self.dtype)
            self.date = str(source.getDate())
        
    def iter_Image(self):

        pixels_d = {}
        pixels_d['PhysicalSizeX'] = str(self.Xres)
        pixels_d['PhysicalSizeY'] = str(self.Yres)
        pixels_d['PhysicalSizeZ'] = str(self.Zres)
        pixels_d['TimeIncrement'] = str(self.sizeT)
        self.PhysSize = (1/self.Xres,1/self.Yres,1/self.Zres)
        order = 'XYZCT'
        channel_d = dict(SamplesPerPixel='1')
        lpath_l = []

        self.tif_uuid = self._mk_uuid()
        self.tif_filename = self.filename  
        print 'tif_filename',self.tif_filename       
        print 'sizeZ,sizeC,sizeT',self.sizeZ,self.sizeC,self.sizeT
        pixels = ome_xml.Pixels(
                    DimensionOrder=order, ID='Pixels:0',
                    SizeX = str(self.sizeX), SizeY = str(self.sizeY), SizeZ = str(self.sizeZ), 
                    SizeT=str(self.sizeT), SizeC = str(self.sizeC),Type = self.dtype, **pixels_d
                    )
        
        colors = []
        labels = []
        for c,ch in enumerate(self.source.getChannels()):
            print "Name: ", ch.getLabel()   # if no name, get emission wavelength or index
            labels.append(ch.getLabel())
            print "  Color:", ch.getColor().getInt()
            r = ch.getColor().getRed()
            g = ch.getColor().getGreen()
            b = ch.getColor().getBlue()
            a = ch.getColor().getAlpha()
            color = (a<<24)+(r<<16)+(g<<8)+(b<<0) - 2**32/2  
            colors.append(str())
#             colors.append(str(ch.getColor().getInt()))
            
        for c in self.slicesC:      
            channel_d['Color'] = colors[c]
            channel_d['Name'] = labels[c]
            channel = ome_xml.Channel(ID='Channel:0:%s' % c, **channel_d)
            print 'channel',channel
            lpath = ome_xml.LightPath(*lpath_l)
            channel.set_LightPath(lpath)
            pixels.insert_Channel_at(c,channel)
            print 'pixels',pixels

        IFD = 0
        for z in range(self.sizeZ):    
            for c in range(self.sizeC): 
                for t in range(self.sizeT):  
                    print 'c',c 
                    d = dict(IFD=str(IFD),FirstC=str(c), FirstZ=str(z),FirstT=str(t), PlaneCount='1')            
                    tiffdata = ome_xml.TiffData(UUID=ome_xml.UUIDType(FileName=self.tif_filename, valueOf_='urn:uuid:%s' % (self.tif_uuid)), **d)
                    pixels.insert_TiffData_at(IFD,tiffdata)   
                    IFD += 1 
                             
        date = self.date.replace(' ','T')
#         if ' ' in str(self.filename):
#             DatasetID = str(self.filename).replace(' ','_')
#         else:
#             DatasetID = str(self.filename)

        image = ome_xml.Image(AcquiredDate=date, Pixels=pixels, ID='Image:%0') 
        for r in range(self.roi_count):
            ref = ome_xml.ROIRef(ID='ROI:%s'%str(r))
            image.insert_ROIRef_at(r,ref)
            
        yield image    
        
    def iter_ROI(self):        
        props = {}
        for rid in range(self.roi_count):
            r = self.ROI[rid]
            roi = ome_xml.ROI(ID='ROI:%s' % rid)
            shape = ome_xml.Shape(ID='Shape:%s'%str(rid+1))
            name = r.value.__class__.__name__[:-1]
            
            # what type of shape are we dealing with?
            obj = shapes[name]
            
            # if it is polygon set the points
            if "Polygon" in name:
                # remove whitespace in points list
                pts = r.fromPoints("points")
                index = 0
                indices = []
                while index < len(pts):
                    index = pts.find(' ', index)
                    if index == -1:
                        break
                    indices.append(index-1)
                    index += 1
                new_points = "".join([char for idx, char in enumerate(pts) if idx not in indices])
                shape.set_Polyline(obj(Points=new_points,Closed=True))
            # if it is rectangle set x,y,w,h
            elif "Rectangle" in name:
                pass
            
            union = ome_xml.UnionType()
            union.insert_Shape_at(rid,shape)
            roi.set_Union(union)
            yield roi    


            
   
