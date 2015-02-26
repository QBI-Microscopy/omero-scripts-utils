#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ome import ome, roi, OMEBase           

shapes = {"Rect":roi.Rectangle,"Ellipse":roi.Ellipse,"Polygon":roi.Polygon}

class OMEExporter(OMEBase):

    prefix = 'ome'
    def __init__(self,conn,source,input_dir,filename,box=None,theZ=None,theC=None,theT=None,ROI=None):
        OMEBase.__init__(self)
        self.conn = conn
        self.source = source
        self.input_dir = input_dir
        self.filename = filename
        self.box = box
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
        
    def iter_Image(self, func):

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
        pixels = ome.Pixels(
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
            colors.append(str((r<<24)+(g<<16)+(b<<8)+(a<<0)))
            
        for c in self.slicesC:      
            channel_d['Color'] = colors[c]
            channel_d['Name'] = labels[c]
            channel = ome.Channel(ID='Channel:0:%s' % c, **channel_d)
            print 'channel',channel
            lpath = ome.LightPath(*lpath_l)
            channel.append(lpath)
            pixels.append(channel)
            print 'pixels',pixels

        plane_l = []
        IFD = 0
        for z in range(self.sizeZ):    
            for c in range(self.sizeC): 
                for t in range(self.sizeT):  
                    print 'c',c 
                    d = dict(IFD=str(IFD),FirstC=str(c), FirstZ=str(z),FirstT=str(t), PlaneCount='1')
                    plane_l.append(d)
            
                    tiffdata = ome.TiffData(ome.UUID (self.tif_uuid, FileName=self.tif_filename), **d)
                    pixels.append(tiffdata)   
                    IFD += 1 
                             
        date = self.date.replace(' ','T')
#         if ' ' in str(self.filename):
#             DatasetID = str(self.filename).replace(' ','_')
#         else:
#             DatasetID = str(self.filename)
        
        roirefs = []    
        for r in range(self.roi_count):
            ref = roi.ROIREF(ID='ROI:%s'%str(r+1))
            roirefs.append(ref)
            
        image = ome.Image (ome.AcquiredDate(date),
#                            ome.DatasetRef(ID='Dataset:%s' % (DatasetID)),
                           pixels, *roirefs, ID='Image:%0')
        yield image    
        
    def iter_ROI(self, func):        
        props = {}
        for rid in range(self.roi_count):
            r = self.ROI[rid]
            e = func(ID='ROI:%s' % rid)
            union = roi.Union()
            shape = roi.Shape(ID='Shape:%s'%str(rid+1))
            name = r.value.__class__.__name__[:-1]
            # need a function here to change the properties for each ROI type
            pts = r.fromPoints("points")
            index = 0
            indices = []
            while index < len(pts):
                index = pts.find(' ', index)
                if index == -1:
                    break
                indices.append(index-1)
                index += 1 # +2 because len('ll') == 2
            new_points = "".join([char for idx, char in enumerate(pts) if idx not in indices])
            props['Points'] = new_points
            obj = shapes[name]
            shape.append(obj(**props))
            union.append(shape)
            e.append(union)
            yield e    


            
   
