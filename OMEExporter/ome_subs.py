#!/usr/bin/env python

#
# Generated Tue Mar 17 15:08:00 2015 by generateDS.py version 2.15a.
#
# Command line options:
#   ('--export', 'etree')
#   ('-o', 'ome.py')
#   ('-s', 'ome_subs.py')
#
# Command line arguments:
#   ome.xsd
#
# Command line:
#   generateDS.py --export="etree" -o "ome.py" -s "ome_subs.py" ome.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.15a
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(*args, **kwargs):
    if 'parser' not in kwargs:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class OMESub(supermod.OME):
    def __init__(self, UUID=None, Project=None, Dataset=None, Experiment=None, Plate=None, Screen=None, Experimenter=None, Group=None, Instrument=None, Image=None, StructuredAnnotations=None, ROI=None):
        super(OMESub, self).__init__(UUID, Project, Dataset, Experiment, Plate, Screen, Experimenter, Group, Instrument, Image, StructuredAnnotations, ROI, )
supermod.OME.subclass = OMESub
# end class OMESub


class ImageSub(supermod.Image):
    def __init__(self, ID=None, Name=None, AcquiredDate=None, ExperimenterRef=None, Description=None, ExperimentRef=None, GroupRef=None, DatasetRef=None, InstrumentRef=None, ObjectiveSettings=None, ImagingEnvironment=None, StageLabel=None, Pixels=None, ROIRef=None, MicrobeamManipulationRef=None, AnnotationRef=None):
        super(ImageSub, self).__init__(ID, Name, AcquiredDate, ExperimenterRef, Description, ExperimentRef, GroupRef, DatasetRef, InstrumentRef, ObjectiveSettings, ImagingEnvironment, StageLabel, Pixels, ROIRef, MicrobeamManipulationRef, AnnotationRef, )
supermod.Image.subclass = ImageSub
# end class ImageSub


class PixelsSub(supermod.Pixels):
    def __init__(self, SizeT=None, DimensionOrder=None, TimeIncrement=None, PhysicalSizeY=None, PhysicalSizeX=None, PhysicalSizeZ=None, SizeX=None, SizeY=None, SizeZ=None, SizeC=None, Type=None, ID=None, Channel=None, BinData=None, TiffData=None, MetadataOnly=None, Plane=None, AnnotationRef=None):
        super(PixelsSub, self).__init__(SizeT, DimensionOrder, TimeIncrement, PhysicalSizeY, PhysicalSizeX, PhysicalSizeZ, SizeX, SizeY, SizeZ, SizeC, Type, ID, Channel, BinData, TiffData, MetadataOnly, Plane, AnnotationRef, )
supermod.Pixels.subclass = PixelsSub
# end class PixelsSub


class PlaneSub(supermod.Plane):
    def __init__(self, ExposureTime=None, PositionZ=None, PositionX=None, PositionY=None, DeltaT=None, TheC=None, TheZ=None, TheT=None, HashSHA1=None, AnnotationRef=None):
        super(PlaneSub, self).__init__(ExposureTime, PositionZ, PositionX, PositionY, DeltaT, TheC, TheZ, TheT, HashSHA1, AnnotationRef, )
supermod.Plane.subclass = PlaneSub
# end class PlaneSub


class ChannelSub(supermod.Channel):
    def __init__(self, PinholeSize=None, Name=None, AcquisitionMode=None, Color=-2147483648, ContrastMethod=None, ExcitationWavelength=None, IlluminationType=None, Fluor=None, PockelCellSetting=None, EmissionWavelength=None, NDFilter=None, ID=None, SamplesPerPixel=None, LightSourceSettings=None, OTFRef=None, DetectorSettings=None, FilterSetRef=None, AnnotationRef=None, LightPath=None):
        super(ChannelSub, self).__init__(PinholeSize, Name, AcquisitionMode, Color, ContrastMethod, ExcitationWavelength, IlluminationType, Fluor, PockelCellSetting, EmissionWavelength, NDFilter, ID, SamplesPerPixel, LightSourceSettings, OTFRef, DetectorSettings, FilterSetRef, AnnotationRef, LightPath, )
supermod.Channel.subclass = ChannelSub
# end class ChannelSub


class MetadataOnlySub(supermod.MetadataOnly):
    def __init__(self):
        super(MetadataOnlySub, self).__init__()
supermod.MetadataOnly.subclass = MetadataOnlySub
# end class MetadataOnlySub


class TiffDataSub(supermod.TiffData):
    def __init__(self, IFD='0', PlaneCount=None, FirstZ='0', FirstC='0', FirstT='0', UUID=None):
        super(TiffDataSub, self).__init__(IFD, PlaneCount, FirstZ, FirstC, FirstT, UUID, )
supermod.TiffData.subclass = TiffDataSub
# end class TiffDataSub


class StageLabelSub(supermod.StageLabel):
    def __init__(self, Y=None, X=None, Z=None, Name=None):
        super(StageLabelSub, self).__init__(Y, X, Z, Name, )
supermod.StageLabel.subclass = StageLabelSub
# end class StageLabelSub


class MicrobeamManipulationSub(supermod.MicrobeamManipulation):
    def __init__(self, Type=None, ID=None, ROIRef=None, ExperimenterRef=None, LightSourceSettings=None):
        super(MicrobeamManipulationSub, self).__init__(Type, ID, ROIRef, ExperimenterRef, LightSourceSettings, )
supermod.MicrobeamManipulation.subclass = MicrobeamManipulationSub
# end class MicrobeamManipulationSub


class InstrumentSub(supermod.Instrument):
    def __init__(self, ID=None, Microscope=None, LightSource=None, Detector=None, Objective=None, FilterSet=None, Filter=None, Dichroic=None, OTF=None):
        super(InstrumentSub, self).__init__(ID, Microscope, LightSource, Detector, Objective, FilterSet, Filter, Dichroic, OTF, )
supermod.Instrument.subclass = InstrumentSub
# end class InstrumentSub


class OTFSub(supermod.OTF):
    def __init__(self, SizeX=None, SizeY=None, Type=None, ID=None, OpticalAxisAveraged=None, ObjectiveSettings=None, FilterSetRef=None, BinaryFile=None):
        super(OTFSub, self).__init__(SizeX, SizeY, Type, ID, OpticalAxisAveraged, ObjectiveSettings, FilterSetRef, BinaryFile, )
supermod.OTF.subclass = OTFSub
# end class OTFSub


class ImagingEnvironmentSub(supermod.ImagingEnvironment):
    def __init__(self, CO2Percent=None, Temperature=None, AirPressure=None, Humidity=None):
        super(ImagingEnvironmentSub, self).__init__(CO2Percent, Temperature, AirPressure, Humidity, )
supermod.ImagingEnvironment.subclass = ImagingEnvironmentSub
# end class ImagingEnvironmentSub


class ProjectSub(supermod.Project):
    def __init__(self, Name=None, ID=None, Description=None, ExperimenterRef=None, GroupRef=None, AnnotationRef=None):
        super(ProjectSub, self).__init__(Name, ID, Description, ExperimenterRef, GroupRef, AnnotationRef, )
supermod.Project.subclass = ProjectSub
# end class ProjectSub


class GroupSub(supermod.Group):
    def __init__(self, Name=None, ID=None, Description=None, Leader=None, Contact=None):
        super(GroupSub, self).__init__(Name, ID, Description, Leader, Contact, )
supermod.Group.subclass = GroupSub
# end class GroupSub


class DatasetSub(supermod.Dataset):
    def __init__(self, Name=None, ID=None, Description=None, ExperimenterRef=None, GroupRef=None, ProjectRef=None, AnnotationRef=None):
        super(DatasetSub, self).__init__(Name, ID, Description, ExperimenterRef, GroupRef, ProjectRef, AnnotationRef, )
supermod.Dataset.subclass = DatasetSub
# end class DatasetSub


class ExperimentSub(supermod.Experiment):
    def __init__(self, Type=None, ID=None, Description=None, ExperimenterRef=None, MicrobeamManipulation=None):
        super(ExperimentSub, self).__init__(Type, ID, Description, ExperimenterRef, MicrobeamManipulation, )
supermod.Experiment.subclass = ExperimentSub
# end class ExperimentSub


class ExperimenterSub(supermod.Experimenter):
    def __init__(self, UserName=None, DisplayName=None, FirstName=None, MiddleName=None, LastName=None, Email=None, Institution=None, ID=None, GroupRef=None, AnnotationRef=None):
        super(ExperimenterSub, self).__init__(UserName, DisplayName, FirstName, MiddleName, LastName, Email, Institution, ID, GroupRef, AnnotationRef, )
supermod.Experimenter.subclass = ExperimenterSub
# end class ExperimenterSub


class ManufacturerSpecSub(supermod.ManufacturerSpec):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None):
        super(ManufacturerSpecSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, )
supermod.ManufacturerSpec.subclass = ManufacturerSpecSub
# end class ManufacturerSpecSub


class ObjectiveSub(supermod.Objective):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, Iris=None, WorkingDistance=None, Immersion=None, Correction=None, LensNA=None, NominalMagnification=None, CalibratedMagnification=None, ID=None):
        super(ObjectiveSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, Iris, WorkingDistance, Immersion, Correction, LensNA, NominalMagnification, CalibratedMagnification, ID, )
supermod.Objective.subclass = ObjectiveSub
# end class ObjectiveSub


class DetectorSub(supermod.Detector):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, Zoom=None, AmplificationGain=None, Gain=None, Offset=None, Type=None, ID=None, Voltage=None):
        super(DetectorSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, Zoom, AmplificationGain, Gain, Offset, Type, ID, Voltage, )
supermod.Detector.subclass = DetectorSub
# end class DetectorSub


class FilterSetSub(supermod.FilterSet):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, ID=None, ExcitationFilterRef=None, DichroicRef=None, EmissionFilterRef=None):
        super(FilterSetSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, ID, ExcitationFilterRef, DichroicRef, EmissionFilterRef, )
supermod.FilterSet.subclass = FilterSetSub
# end class FilterSetSub


class FilterSub(supermod.Filter):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, FilterWheel=None, Type=None, ID=None, TransmittanceRange=None):
        super(FilterSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, FilterWheel, Type, ID, TransmittanceRange, )
supermod.Filter.subclass = FilterSub
# end class FilterSub


class TransmittanceRangeSub(supermod.TransmittanceRange):
    def __init__(self, CutIn=None, Transmittance=None, CutOut=None, CutInTolerance=None, CutOutTolerance=None):
        super(TransmittanceRangeSub, self).__init__(CutIn, Transmittance, CutOut, CutInTolerance, CutOutTolerance, )
supermod.TransmittanceRange.subclass = TransmittanceRangeSub
# end class TransmittanceRangeSub


class DichroicSub(supermod.Dichroic):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, ID=None):
        super(DichroicSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, ID, )
supermod.Dichroic.subclass = DichroicSub
# end class DichroicSub


class LightPathSub(supermod.LightPath):
    def __init__(self, ExcitationFilterRef=None, DichroicRef=None, EmissionFilterRef=None):
        super(LightPathSub, self).__init__(ExcitationFilterRef, DichroicRef, EmissionFilterRef, )
supermod.LightPath.subclass = LightPathSub
# end class LightPathSub


class LightSourceSub(supermod.LightSource):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, ID=None, Power=None, Laser=None, Filament=None, Arc=None, LightEmittingDiode=None):
        super(LightSourceSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, ID, Power, Laser, Filament, Arc, LightEmittingDiode, )
supermod.LightSource.subclass = LightSourceSub
# end class LightSourceSub


class LaserSub(supermod.Laser):
    def __init__(self, PockelCell=None, Pulse=None, LaserMedium=None, Tuneable=None, Wavelength=None, FrequencyMultiplication=None, Type=None, RepetitionRate=None, Pump=None):
        super(LaserSub, self).__init__(PockelCell, Pulse, LaserMedium, Tuneable, Wavelength, FrequencyMultiplication, Type, RepetitionRate, Pump, )
supermod.Laser.subclass = LaserSub
# end class LaserSub


class ArcSub(supermod.Arc):
    def __init__(self, Type=None):
        super(ArcSub, self).__init__(Type, )
supermod.Arc.subclass = ArcSub
# end class ArcSub


class FilamentSub(supermod.Filament):
    def __init__(self, Type=None):
        super(FilamentSub, self).__init__(Type, )
supermod.Filament.subclass = FilamentSub
# end class FilamentSub


class LightEmittingDiodeSub(supermod.LightEmittingDiode):
    def __init__(self):
        super(LightEmittingDiodeSub, self).__init__()
supermod.LightEmittingDiode.subclass = LightEmittingDiodeSub
# end class LightEmittingDiodeSub


class ReferenceSub(supermod.Reference):
    def __init__(self):
        super(ReferenceSub, self).__init__()
supermod.Reference.subclass = ReferenceSub
# end class ReferenceSub


class FilterRefSub(supermod.FilterRef):
    def __init__(self, ID=None):
        super(FilterRefSub, self).__init__(ID, )
supermod.FilterRef.subclass = FilterRefSub
# end class FilterRefSub


class MicrobeamManipulationRefSub(supermod.MicrobeamManipulationRef):
    def __init__(self, ID=None):
        super(MicrobeamManipulationRefSub, self).__init__(ID, )
supermod.MicrobeamManipulationRef.subclass = MicrobeamManipulationRefSub
# end class MicrobeamManipulationRefSub


class ExperimentRefSub(supermod.ExperimentRef):
    def __init__(self, ID=None):
        super(ExperimentRefSub, self).__init__(ID, )
supermod.ExperimentRef.subclass = ExperimentRefSub
# end class ExperimentRefSub


class ChannelRefSub(supermod.ChannelRef):
    def __init__(self, ID=None):
        super(ChannelRefSub, self).__init__(ID, )
supermod.ChannelRef.subclass = ChannelRefSub
# end class ChannelRefSub


class ProjectRefSub(supermod.ProjectRef):
    def __init__(self, ID=None):
        super(ProjectRefSub, self).__init__(ID, )
supermod.ProjectRef.subclass = ProjectRefSub
# end class ProjectRefSub


class ExperimenterRefSub(supermod.ExperimenterRef):
    def __init__(self, ID=None):
        super(ExperimenterRefSub, self).__init__(ID, )
supermod.ExperimenterRef.subclass = ExperimenterRefSub
# end class ExperimenterRefSub


class GroupRefSub(supermod.GroupRef):
    def __init__(self, ID=None):
        super(GroupRefSub, self).__init__(ID, )
supermod.GroupRef.subclass = GroupRefSub
# end class GroupRefSub


class InstrumentRefSub(supermod.InstrumentRef):
    def __init__(self, ID=None):
        super(InstrumentRefSub, self).__init__(ID, )
supermod.InstrumentRef.subclass = InstrumentRefSub
# end class InstrumentRefSub


class DatasetRefSub(supermod.DatasetRef):
    def __init__(self, ID=None):
        super(DatasetRefSub, self).__init__(ID, )
supermod.DatasetRef.subclass = DatasetRefSub
# end class DatasetRefSub


class FilterSetRefSub(supermod.FilterSetRef):
    def __init__(self, ID=None):
        super(FilterSetRefSub, self).__init__(ID, )
supermod.FilterSetRef.subclass = FilterSetRefSub
# end class FilterSetRefSub


class OTFRefSub(supermod.OTFRef):
    def __init__(self, ID=None):
        super(OTFRefSub, self).__init__(ID, )
supermod.OTFRef.subclass = OTFRefSub
# end class OTFRefSub


class SettingsSub(supermod.Settings):
    def __init__(self):
        super(SettingsSub, self).__init__()
supermod.Settings.subclass = SettingsSub
# end class SettingsSub


class LightSourceSettingsSub(supermod.LightSourceSettings):
    def __init__(self, Wavelength=None, Attenuation=None, ID=None):
        super(LightSourceSettingsSub, self).__init__(Wavelength, Attenuation, ID, )
supermod.LightSourceSettings.subclass = LightSourceSettingsSub
# end class LightSourceSettingsSub


class DetectorSettingsSub(supermod.DetectorSettings):
    def __init__(self, Binning=None, ReadOutRate=None, Gain=None, Offset=None, ID=None, Voltage=None):
        super(DetectorSettingsSub, self).__init__(Binning, ReadOutRate, Gain, Offset, ID, Voltage, )
supermod.DetectorSettings.subclass = DetectorSettingsSub
# end class DetectorSettingsSub


class ObjectiveSettingsSub(supermod.ObjectiveSettings):
    def __init__(self, RefractiveIndex=None, CorrectionCollar=None, ID=None, Medium=None):
        super(ObjectiveSettingsSub, self).__init__(RefractiveIndex, CorrectionCollar, ID, Medium, )
supermod.ObjectiveSettings.subclass = ObjectiveSettingsSub
# end class ObjectiveSettingsSub


class ExternalSub(supermod.External):
    def __init__(self, href=None, Compression='none', SHA1=None):
        super(ExternalSub, self).__init__(href, Compression, SHA1, )
supermod.External.subclass = ExternalSub
# end class ExternalSub


class BinDataSub(supermod.BinData):
    def __init__(self, BigEndian=None, Length=None, Compression='none', valueOf_=None):
        super(BinDataSub, self).__init__(BigEndian, Length, Compression, valueOf_, )
supermod.BinData.subclass = BinDataSub
# end class BinDataSub


class BinaryFileSub(supermod.BinaryFile):
    def __init__(self, MIMEType=None, Size=None, FileName=None, External=None, BinData=None):
        super(BinaryFileSub, self).__init__(MIMEType, Size, FileName, External, BinData, )
supermod.BinaryFile.subclass = BinaryFileSub
# end class BinaryFileSub


class MicroscopeSub(supermod.Microscope):
    def __init__(self, LotNumber=None, Model=None, SerialNumber=None, Manufacturer=None, Type=None):
        super(MicroscopeSub, self).__init__(LotNumber, Model, SerialNumber, Manufacturer, Type, )
supermod.Microscope.subclass = MicroscopeSub
# end class MicroscopeSub


class LeaderSub(supermod.Leader):
    def __init__(self, ID=None):
        super(LeaderSub, self).__init__(ID, )
supermod.Leader.subclass = LeaderSub
# end class LeaderSub


class ContactSub(supermod.Contact):
    def __init__(self, ID=None):
        super(ContactSub, self).__init__(ID, )
supermod.Contact.subclass = ContactSub
# end class ContactSub


class DichroicRefSub(supermod.DichroicRef):
    def __init__(self, ID=None):
        super(DichroicRefSub, self).__init__(ID, )
supermod.DichroicRef.subclass = DichroicRefSub
# end class DichroicRefSub


class PumpSub(supermod.Pump):
    def __init__(self, ID=None):
        super(PumpSub, self).__init__(ID, )
supermod.Pump.subclass = PumpSub
# end class PumpSub


class PlateSub(supermod.Plate):
    def __init__(self, Status=None, Rows=None, ExternalIdentifier=None, RowNamingConvention=None, ColumnNamingConvention=None, WellOriginY=None, WellOriginX=None, ID=None, Columns=None, Name=None, Description=None, ScreenRef=None, Well=None, AnnotationRef=None, PlateAcquisition=None):
        super(PlateSub, self).__init__(Status, Rows, ExternalIdentifier, RowNamingConvention, ColumnNamingConvention, WellOriginY, WellOriginX, ID, Columns, Name, Description, ScreenRef, Well, AnnotationRef, PlateAcquisition, )
supermod.Plate.subclass = PlateSub
# end class PlateSub


class ReagentSub(supermod.Reagent):
    def __init__(self, ReagentIdentifier=None, ID=None, Name=None, Description=None, AnnotationRef=None):
        super(ReagentSub, self).__init__(ReagentIdentifier, ID, Name, Description, AnnotationRef, )
supermod.Reagent.subclass = ReagentSub
# end class ReagentSub


class ReagentRefSub(supermod.ReagentRef):
    def __init__(self, ID=None):
        super(ReagentRefSub, self).__init__(ID, )
supermod.ReagentRef.subclass = ReagentRefSub
# end class ReagentRefSub


class ScreenSub(supermod.Screen):
    def __init__(self, Name=None, ProtocolDescription=None, ProtocolIdentifier=None, ReagentSetDescription=None, Type=None, ID=None, ReagentSetIdentifier=None, Description=None, Reagent=None, PlateRef=None, AnnotationRef=None):
        super(ScreenSub, self).__init__(Name, ProtocolDescription, ProtocolIdentifier, ReagentSetDescription, Type, ID, ReagentSetIdentifier, Description, Reagent, PlateRef, AnnotationRef, )
supermod.Screen.subclass = ScreenSub
# end class ScreenSub


class PlateAcquisitionSub(supermod.PlateAcquisition):
    def __init__(self, MaximumFieldCount=None, EndTime=None, ID=None, StartTime=None, Name=None, Description=None, WellSampleRef=None, AnnotationRef=None):
        super(PlateAcquisitionSub, self).__init__(MaximumFieldCount, EndTime, ID, StartTime, Name, Description, WellSampleRef, AnnotationRef, )
supermod.PlateAcquisition.subclass = PlateAcquisitionSub
# end class PlateAcquisitionSub


class WellSub(supermod.Well):
    def __init__(self, Status=None, ExternalIdentifier=None, Column=None, ExternalDescription=None, Color=-2147483648, ID=None, Row=None, WellSample=None, ReagentRef=None, AnnotationRef=None):
        super(WellSub, self).__init__(Status, ExternalIdentifier, Column, ExternalDescription, Color, ID, Row, WellSample, ReagentRef, AnnotationRef, )
supermod.Well.subclass = WellSub
# end class WellSub


class WellSampleSub(supermod.WellSample):
    def __init__(self, Index=None, PositionX=None, PositionY=None, ID=None, Timepoint=None, ImageRef=None, AnnotationRef=None):
        super(WellSampleSub, self).__init__(Index, PositionX, PositionY, ID, Timepoint, ImageRef, AnnotationRef, )
supermod.WellSample.subclass = WellSampleSub
# end class WellSampleSub


class ImageRefSub(supermod.ImageRef):
    def __init__(self, ID=None):
        super(ImageRefSub, self).__init__(ID, )
supermod.ImageRef.subclass = ImageRefSub
# end class ImageRefSub


class WellSampleRefSub(supermod.WellSampleRef):
    def __init__(self, ID=None):
        super(WellSampleRefSub, self).__init__(ID, )
supermod.WellSampleRef.subclass = WellSampleRefSub
# end class WellSampleRefSub


class StructuredAnnotationsSub(supermod.StructuredAnnotations):
    def __init__(self, XMLAnnotation=None, FileAnnotation=None, ListAnnotation=None, LongAnnotation=None, DoubleAnnotation=None, CommentAnnotation=None, BooleanAnnotation=None, TimestampAnnotation=None, TagAnnotation=None, TermAnnotation=None):
        super(StructuredAnnotationsSub, self).__init__(XMLAnnotation, FileAnnotation, ListAnnotation, LongAnnotation, DoubleAnnotation, CommentAnnotation, BooleanAnnotation, TimestampAnnotation, TagAnnotation, TermAnnotation, )
supermod.StructuredAnnotations.subclass = StructuredAnnotationsSub
# end class StructuredAnnotationsSub


class AnnotationRefSub(supermod.AnnotationRef):
    def __init__(self, ID=None):
        super(AnnotationRefSub, self).__init__(ID, )
supermod.AnnotationRef.subclass = AnnotationRefSub
# end class AnnotationRefSub


class AnnotationSub(supermod.Annotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, extensiontype_=None):
        super(AnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, extensiontype_, )
supermod.Annotation.subclass = AnnotationSub
# end class AnnotationSub


class FileAnnotationSub(supermod.FileAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, BinaryFile=None):
        super(FileAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, BinaryFile, )
supermod.FileAnnotation.subclass = FileAnnotationSub
# end class FileAnnotationSub


class XMLAnnotationSub(supermod.XMLAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(XMLAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.XMLAnnotation.subclass = XMLAnnotationSub
# end class XMLAnnotationSub


class ListAnnotationSub(supermod.ListAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None):
        super(ListAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, )
supermod.ListAnnotation.subclass = ListAnnotationSub
# end class ListAnnotationSub


class CommentAnnotationSub(supermod.CommentAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(CommentAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.CommentAnnotation.subclass = CommentAnnotationSub
# end class CommentAnnotationSub


class LongAnnotationSub(supermod.LongAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(LongAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.LongAnnotation.subclass = LongAnnotationSub
# end class LongAnnotationSub


class DoubleAnnotationSub(supermod.DoubleAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(DoubleAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.DoubleAnnotation.subclass = DoubleAnnotationSub
# end class DoubleAnnotationSub


class BooleanAnnotationSub(supermod.BooleanAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(BooleanAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.BooleanAnnotation.subclass = BooleanAnnotationSub
# end class BooleanAnnotationSub


class TimestampAnnotationSub(supermod.TimestampAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(TimestampAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.TimestampAnnotation.subclass = TimestampAnnotationSub
# end class TimestampAnnotationSub


class TagAnnotationSub(supermod.TagAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(TagAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.TagAnnotation.subclass = TagAnnotationSub
# end class TagAnnotationSub


class TermAnnotationSub(supermod.TermAnnotation):
    def __init__(self, Namespace=None, ID=None, Description=None, AnnotationRef=None, Value=None):
        super(TermAnnotationSub, self).__init__(Namespace, ID, Description, AnnotationRef, Value, )
supermod.TermAnnotation.subclass = TermAnnotationSub
# end class TermAnnotationSub


class ROISub(supermod.ROI):
    def __init__(self, Namespace=None, ID=None, Name=None, Union=None, AnnotationRef=None, Description=None):
        super(ROISub, self).__init__(Namespace, ID, Name, Union, AnnotationRef, Description, )
supermod.ROI.subclass = ROISub
# end class ROISub


class ShapeSub(supermod.Shape):
    def __init__(self, StrokeDashArray=None, StrokeWidth=None, FillRule=None, LineCap=None, TheC=None, TheT=None, Transform=None, Label=None, FontFamily=None, Stroke=None, FontStyle=None, MarkerEnd=None, TheZ=None, FontSize=None, ID=None, Fill=None, MarkerStart=None, Name=None, Line=None, Rectangle=None, Mask=None, Ellipse=None, Point=None, Polyline=None, Path=None, Text=None, Description=None):
        super(ShapeSub, self).__init__(StrokeDashArray, StrokeWidth, FillRule, LineCap, TheC, TheT, Transform, Label, FontFamily, Stroke, FontStyle, MarkerEnd, TheZ, FontSize, ID, Fill, MarkerStart, Name, Line, Rectangle, Mask, Ellipse, Point, Polyline, Path, Text, Description, )
supermod.Shape.subclass = ShapeSub
# end class ShapeSub


class RectangleSub(supermod.Rectangle):
    def __init__(self, Y=None, X=None, Height=None, Width=None):
        super(RectangleSub, self).__init__(Y, X, Height, Width, )
supermod.Rectangle.subclass = RectangleSub
# end class RectangleSub


class MaskSub(supermod.Mask):
    def __init__(self, Y=None, X=None, Height=None, Width=None, BinData=None):
        super(MaskSub, self).__init__(Y, X, Height, Width, BinData, )
supermod.Mask.subclass = MaskSub
# end class MaskSub


class PointSub(supermod.Point):
    def __init__(self, Y=None, X=None):
        super(PointSub, self).__init__(Y, X, )
supermod.Point.subclass = PointSub
# end class PointSub


class EllipseSub(supermod.Ellipse):
    def __init__(self, Y=None, X=None, RadiusY=None, RadiusX=None):
        super(EllipseSub, self).__init__(Y, X, RadiusY, RadiusX, )
supermod.Ellipse.subclass = EllipseSub
# end class EllipseSub


class LineSub(supermod.Line):
    def __init__(self, Y1=None, X2=None, X1=None, Y2=None):
        super(LineSub, self).__init__(Y1, X2, X1, Y2, )
supermod.Line.subclass = LineSub
# end class LineSub


class PolylineSub(supermod.Polyline):
    def __init__(self, Points=None, Closed=False):
        super(PolylineSub, self).__init__(Points, Closed, )
supermod.Polyline.subclass = PolylineSub
# end class PolylineSub


class PathSub(supermod.Path):
    def __init__(self, Definition=None):
        super(PathSub, self).__init__(Definition, )
supermod.Path.subclass = PathSub
# end class PathSub


class TextSub(supermod.Text):
    def __init__(self, Y=None, X=None, Value=None):
        super(TextSub, self).__init__(Y, X, Value, )
supermod.Text.subclass = TextSub
# end class TextSub


class ROIRefSub(supermod.ROIRef):
    def __init__(self, ID=None):
        super(ROIRefSub, self).__init__(ID, )
supermod.ROIRef.subclass = ROIRefSub
# end class ROIRefSub


class UUIDTypeSub(supermod.UUIDType):
    def __init__(self, FileName=None, valueOf_=None):
        super(UUIDTypeSub, self).__init__(FileName, valueOf_, )
supermod.UUIDType.subclass = UUIDTypeSub
# end class UUIDTypeSub


class UUIDType6Sub(supermod.UUIDType6):
    def __init__(self, FileName=None, valueOf_=None):
        super(UUIDType6Sub, self).__init__(FileName, valueOf_, )
supermod.UUIDType6.subclass = UUIDType6Sub
# end class UUIDType6Sub


class ScreenRefTypeSub(supermod.ScreenRefType):
    def __init__(self, ID=None):
        super(ScreenRefTypeSub, self).__init__(ID, )
supermod.ScreenRefType.subclass = ScreenRefTypeSub
# end class ScreenRefTypeSub


class PlateRefTypeSub(supermod.PlateRefType):
    def __init__(self, ID=None):
        super(PlateRefTypeSub, self).__init__(ID, )
supermod.PlateRefType.subclass = PlateRefTypeSub
# end class PlateRefTypeSub


class ValueTypeSub(supermod.ValueType):
    def __init__(self, anytypeobjs_=None):
        super(ValueTypeSub, self).__init__(anytypeobjs_, )
supermod.ValueType.subclass = ValueTypeSub
# end class ValueTypeSub


class UnionTypeSub(supermod.UnionType):
    def __init__(self, Shape=None):
        super(UnionTypeSub, self).__init__(Shape, )
supermod.UnionType.subclass = UnionTypeSub
# end class UnionTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'OME'
        rootClass = supermod.OME
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:OME="http://www.openmicroscopy.org/Schemas/OME/2010-06"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'OME'
        rootClass = supermod.OME
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'OME'
        rootClass = supermod.OME
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:OME="http://www.openmicroscopy.org/Schemas/OME/2010-06"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'OME'
        rootClass = supermod.OME
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
