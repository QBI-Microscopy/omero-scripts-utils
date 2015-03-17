#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from uuid import uuid1 as uuid
from lxml import etree
from lxml.builder import ElementMaker
#from pylibtiff import TIFFimage
from tifffile import imsave
try:
    from libtiff import TIFF
except:
    import traceback
    traceback.print_exc()
    raw_input('enter to close')
import numpy as np

namespace_map=dict(bf = "http://www.openmicroscopy.org/Schemas/BinaryFile/2013-06",
                   ome = "http://www.openmicroscopy.org/Schemas/OME/2013-06",
                   xsi = "http://www.w3.org/2001/XMLSchema-instance",
                   roi = "http://www.openmicroscopy.org/Schemas/ROI/2012-06",
#                    sa = "http://www.openmicroscopy.org/Schemas/SA/2013-06",
#                    spw = "http://www.openmicroscopy.org/Schemas/SPW/2013-06"
                   )
default = {"OME" : "http://www.openmicroscopy.org/Schemas/OME/2013-06"}
# create element makers: bf, ome, xsi
default_validate = False
# if default_validate:
#     # use this when validating
#     ome = ElementMaker (namespace = namespace_map['ome'], nsmap = namespace_map) 
# else:
#     # use this for creating imagej readable ome.tiff files.
#     ome = ElementMaker (nsmap = namespace_map) 
ome = ElementMaker(namespace = namespace_map['ome'], nsmap = namespace_map)
roi = ElementMaker(namespace = namespace_map['roi']) 
# bf = ElementMaker (namespace = namespace_map['bf'], nsmap = namespace_map)
# sa = ElementMaker (namespace = namespace_map['sa'], nsmap = namespace_map)
# spw = ElementMaker (namespace = namespace_map['spw'], nsmap = namespace_map)

def ATTR(namespace, name, value):
    return {'{%s}%s' % (namespace_map[namespace], name): value}

def validate_xml(xml):
    if getattr(sys,'frozen',None):
        ome_xsd_path = os.path.dirname(sys.executable)
    elif __file__:  
        ome_xsd_path = os.path.dirname(__file__)
        
    ome_xsd = os.path.join(ome_xsd_path,'ome.xsd')    

    if os.path.isfile (ome_xsd):
        ome_xsd = os.path.join(namespace_map['ome'],'ome.xsd')
        f = open (ome_xsd) 
    else:
        import urllib2
        ome_xsd = os.path.join(namespace_map['ome'],'ome.xsd')
        f = urllib2.urlopen(ome_xsd)
    sys.stdout.write('Validating XML content against %r...' % (ome_xsd))
    xmlschema_doc = etree.parse(f)
    
    xmlschema = etree.XMLSchema(xmlschema_doc)
    if isinstance (xml, basestring):
        xml = etree.parse(xml)
    result = xmlschema.validate(xml)
    if not result:
        sys.stdout.write('FAILED:\n')
        for error in xmlschema.error_log:
            s = str (error)
            for k,v in namespace_map.items():
                s = s.replace ('{%s}' % v, '%s:' % k)
        sys.stdout.write('-----\n')
    else:
        sys.stdout.write('SUCCESS!\n')
    return result

class ElementBase:

    def __init__ (self, parent, root, nsn):
        self.parent = parent
        self.root = root
        
        n = self.__class__.__name__
        iter_mth = getattr(parent, 'iter_%s' % (n), None)
        nm = n
        if '_' in n:
            nsn, nm = n.split('_',1)
            nsn = nsn.lower()
        ns = eval(nsn)    
        print 'nsn,nm,ns',nsn,nm,ns
        ome_el = getattr (ns, nm, None)

        if iter_mth is not None:
            for element in iter_mth(ome_el):
                root.append(element)
        elif 0:
            print 'NotImplemented: %s.iter_%s(<%s.%s callable>)' % (parent.__class__.__name__, n, nsn, nm)

class TiffImageGenerator:
    
    def __init__(self,conn,source,input_dir,filename,box):
        self.conn = conn
        self.source = source
        self.input_dir = input_dir
        self.filename = filename
        self.box = box
        self.dtype = source.getPixelsType()
        
    def set_tags(self,tif,imageWidth,imageLength,tileWidth,tileHeight):
        tif.SetField('tilewidth',tileWidth)
        tif.SetField('tilelength',tileHeight)
        tif.SetField('imagelength',imageLength)
        tif.SetField('imagewidth',imageWidth)
        tif.SetField('samplesperpixel', 1)
        tif.SetField('orientation',1)
        tif.SetField('photometric', 1)
        tif.SetField('planarconfig', 2)
        bpp = self.bitspersample(self.source.getPixelsType())
        tif.SetField('bitspersample',bpp)
        tif.SetField('compression',5)        
        
    def create_tiles(self,sizeX,sizeY,slicesZ,slicesC,slicesT,description):    

        tileWidth = 1024
        tileHeight = 1024
        primary_pixels = self.source.getPrimaryPixels()
    
        # Make a list of all the tiles we're going to need.
        zctTileList = []
        for z in slicesZ:
            for c in slicesC:
                for t in slicesT:
                    for tileOffsetY in range(
                            0, int((sizeY + tileHeight - 1) / tileHeight)):
                        for tileOffsetX in range(
                                0, int((sizeX + tileWidth - 1) / tileWidth)):
                            x = tileOffsetX * tileWidth
                            y = tileOffsetY * tileHeight
                            w = tileWidth
                            if (w + x > sizeX):
                                w = sizeX - x
                            h = tileHeight
                            if (h + y > sizeY):
                                h = sizeY - y
                            if self.box:
                                tile_xywh = (self.box[0] + x, self.box[1] + y, w, h)
                            else:
                                tile_xywh = (x, y, w, h)
                            zctTileList.append((z, c, t, tile_xywh))
    
        # This is a generator that will return tiles in the sequence above
        # getTiles() only opens 1 rawPixelsStore for all the tiles
        # whereas getTile() opens and closes a rawPixelsStore for each tile.
        tile_gen = primary_pixels.getTiles(zctTileList)
    
        def next_tile():
            return tile_gen.next()
        
        tile_count = 0
        planes = len(slicesZ) * len(slicesC) * len(slicesT)
        tif_image = TIFF.open(os.path.join(self.input_dir,self.filename), 'w')
        print 'description:',description
        for p in range(planes):
            self.set_tags(tif_image,sizeX,sizeY,tileWidth,tileHeight)
            if p == 0:
                tif_image.set_description(description) 

            # tile_image_params sets the key tags per IFD rather than doing so
            # per tile
#                     tif_image.tile_image_params(sizeX,sizeY,1,tileWidth,tileHeight,'lzw')
            
            for tileOffsetY in range(
                    0, ((sizeY + tileHeight - 1) / tileHeight)):
    
                for tileOffsetX in range(
                        0, ((sizeX + tileWidth - 1) / tileWidth)):
    
                    x = tileOffsetX * tileWidth
                    y = tileOffsetY * tileHeight
                    w = tileWidth
    
                    if (w + x > sizeX):
                        w = sizeX - x
    
                    h = tileHeight
                    if (h + y > sizeY):
                        h = sizeY - y
                    
                    tile_count += 1
                    tile_data = next_tile()
                    if (h != tile_data.shape[0]) or (w != tile_data.shape[1]):
                        h = tile_data.shape[0]
                        w = tile_data.shape[1]
                    tile_dtype = tile_data.dtype
                    tile = np.zeros((1,tileWidth,tileHeight),dtype=tile_dtype)
                    tile[0,:h,:w] = tile_data[:,:]                     
                    tif_image.write_tile(tile,x,y)
            tif_image.WriteDirectory()
        tif_image.close()
        return tile_count
        
    def create_planes(self,sizeX,sizeY,slicesZ,slicesC,slicesT,description):
        sizeZ = len(slicesZ)
        sizeC = len(slicesC)
        print 'sizeC',sizeC
        sizeT = len(slicesT)
        if self.box:
            roi = self.box[:-1]
            zctList = []
            for z in slicesZ:
                for c in slicesC:
                    for t in slicesT:
                        zctList.append((z,c,t,roi))
                        
            planes = self.source.getPrimaryPixels().getTiles(zctList)    # A generator (not all planes in hand)
        else:
            zctList = []
            for z in slicesZ:
                for c in slicesC:
                    for t in slicesT:
                        zctList.append((z,c,t))
                        
            planes = self.source.getPrimaryPixels().getPlanes(zctList)    # A generator (not all planes in hand) 
        plane_list = []
        for i,p in enumerate(planes):
            plane_list.append(p)
    
        p = 0
        image_data = np.zeros((sizeZ,sizeC,sizeT,sizeY,sizeX),dtype=self.dtype)
        print('image data shape:',image_data.shape)
        for z in range(sizeZ):
            for c in range(sizeC):
                for t in range(sizeT):
                    image_data[z,c,t,:,:] = plane_list[p]
                    p += 1

        imsave(os.path.join(self.input_dir,self.filename),image_data,description=description,compress=6)
        
    @staticmethod
    def bitspersample(dtype):
        return dict(uint8=8,uint16=16).get(dtype)
        

class Dataset(ElementBase): pass            
class Group(ElementBase): pass
class Experimenter(ElementBase): pass
class Instrument(ElementBase): pass
class Image(ElementBase): pass
class ROI(ElementBase): pass

class OMEBase:
    """ Base class for OME-XML writers.
    """

#     _subelement_classes = [Dataset, Experimenter, Group, Instrument, Image]
    _subelement_classes = [Image, ROI]

    prefix = ''
    def __init__(self):
        self.tif_images = {}

    def generate(self, options=None, validate=default_validate):
        template_xml = list(self.make_xml())
        tif_gen = TiffImageGenerator(self.conn,self.source,self.input_dir,self.filename,self.box)
        self.tif_images[self.tif_filename,self.tif_uuid,self.PhysSize] = tif_gen

        s = None
        for (fn, uuid, res), tif_gen in self.tif_images.items():
            xml= ome.OME(ATTR('xsi','schemaLocation',"%s %s/ome.xsd" % ((namespace_map['ome'],)*2)),
                          UUID = uuid)
            for item in template_xml:

#                 if item.tag.endswith('Image') and item.get('ID')!='Image:%s' % (detector):
#                     continue
                xml.append(item)
                
            if s is None and validate:
                s = etree.tostring(xml, encoding='UTF-8', xml_declaration=True)
                validate_xml(xml)
            else:
                s = etree.tostring(xml, encoding='UTF-8', xml_declaration=True)
            print 'ome-xml',etree.tostring(xml,pretty_print=True)
            if (self.sizeX < 4096) and (self.sizeY < 4096):
                print 'slicesZ',self.slicesZ
                tif_gen.create_planes(self.sizeX,self.sizeY,self.slicesZ,self.slicesC,self.slicesT,s)
            else:
                tc = tif_gen.create_tiles(self.sizeX,self.sizeY,self.slicesZ,self.slicesC,self.slicesT,s)
                print 'tile count=',tc
            print 'SUCCESS!'

        return s

    def _mk_uuid(self):
        return 'urn:uuid:%s' % (uuid())

    def make_xml(self):
        self.temp_uuid = self._mk_uuid()
        xml = ome.OME(ATTR('xsi','schemaLocation',"%s %s/ome.xsd" % ((namespace_map['ome'],)*2)),
                       UUID = self.temp_uuid)
        for element_cls in self._subelement_classes:
            if element_cls.__name__ == "ROI":
                nsn = "roi"
            else:
                nsn = "ome"
            element_cls(self, xml, nsn) # element_cls should append elements to root
        return xml   

    def get_AcquiredDate(self):
        return None

    @staticmethod
    def dtype2PixelIType(dtype):
        return dict (int8='int8',int16='int16',int32='int32',
                     uint8='uint8',uint16='uint16',uint32='uint32',
                     complex128='double-complex', complex64='complex',
                     float64='double', float32='float',
                     ).get(dtype.name, dtype.name)