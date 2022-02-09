
'''
THIS FILE IS AUTOGENERATED, DO NOT EDIT!!!
'''

from datetime import datetime
from enum import IntEnum
import uuid

from opcua import ua


class ScalarValueDataType(object):

    '''
    ScalarValueDataType structure autogenerated from xml
    '''

    ua_types = [
        ('BooleanValue', 'Boolean'),
        ('SByteValue', 'SByte'),
        ('ByteValue', 'Byte'),
        ('Int16Value', 'Int16'),
        ('UInt16Value', 'UInt16'),
        ('Int32Value', 'Int32'),
        ('UInt32Value', 'UInt32'),
        ('Int64Value', 'Int64'),
        ('UInt64Value', 'UInt64'),
        ('FloatValue', 'Float'),
        ('DoubleValue', 'Double'),
        ('StringValue', 'String'),
        ('DateTimeValue', 'DateTime'),
        ('GuidValue', 'Guid'),
        ('ByteStringValue', 'ByteString'),
        ('XmlElementValue', 'XmlElement'),
        ('NodeIdValue', 'NodeId'),
        ('ExpandedNodeIdValue', 'ExpandedNodeId'),
        ('QualifiedNameValue', 'QualifiedName'),
        ('LocalizedTextValue', 'LocalizedText'),
        ('StatusCodeValue', 'StatusCode'),
        ('VariantValue', 'Variant'),
        ('EnumerationValue', 'Int32'),
        ('StructureValue', 'ExtensionObject'),
        ('Number', 'Variant'),
        ('Integer', 'Variant'),
        ('UInteger', 'Variant'),
    ]
    def __str__(self):
        vals = [name + ": " + str(val) for name, val in self.__dict__.items()]
        return self.__class__.__name__ + "(" + ", ".join(vals) + ")"

    __repr__ = __str__

    def __init__(self):
        self.BooleanValue = True
        self.SByteValue = 0
        self.ByteValue = 0
        self.Int16Value = 0
        self.UInt16Value = 0
        self.Int32Value = 0
        self.UInt32Value = 0
        self.Int64Value = 0
        self.UInt64Value = 0
        self.FloatValue = 0
        self.DoubleValue = 0
        self.StringValue = ''
        self.DateTimeValue = datetime.utcnow()
        self.GuidValue = uuid.uuid4()
        self.ByteStringValue = b''
        self.XmlElementValue = ua.XmlElement()
        self.NodeIdValue = ua.NodeId()
        self.ExpandedNodeIdValue = ua.ExpandedNodeId()
        self.QualifiedNameValue = ua.QualifiedName()
        self.LocalizedTextValue = ua.LocalizedText()
        self.StatusCodeValue = ua.StatusCode()
        self.VariantValue = ua.Variant()
        self.EnumerationValue = 0
        self.StructureValue = ua.ExtensionObject()
        self.Number = ua.Variant()
        self.Integer = ua.Variant()
        self.UInteger = ua.Variant()


class ArrayValueDataType(object):

    '''
    ArrayValueDataType structure autogenerated from xml
    '''

    ua_types = [
        ('BooleanValue', 'ListOfBoolean'),
        ('SByteValue', 'ListOfSByte'),
        ('ByteValue', 'ListOfByte'),
        ('Int16Value', 'ListOfInt16'),
        ('UInt16Value', 'ListOfUInt16'),
        ('Int32Value', 'ListOfInt32'),
        ('UInt32Value', 'ListOfUInt32'),
        ('Int64Value', 'ListOfInt64'),
        ('UInt64Value', 'ListOfUInt64'),
        ('FloatValue', 'ListOfFloat'),
        ('DoubleValue', 'ListOfDouble'),
        ('StringValue', 'ListOfString'),
        ('DateTimeValue', 'ListOfDateTime'),
        ('GuidValue', 'ListOfGuid'),
        ('ByteStringValue', 'ListOfByteString'),
        ('XmlElementValue', 'ListOfXmlElement'),
        ('NodeIdValue', 'ListOfNodeId'),
        ('ExpandedNodeIdValue', 'ListOfExpandedNodeId'),
        ('QualifiedNameValue', 'ListOfQualifiedName'),
        ('LocalizedTextValue', 'ListOfLocalizedText'),
        ('StatusCodeValue', 'ListOfStatusCode'),
        ('VariantValue', 'ListOfVariant'),
        ('EnumerationValue', 'ListOfInt32'),
        ('StructureValue', 'ListOfExtensionObject'),
        ('Number', 'ListOfVariant'),
        ('Integer', 'ListOfVariant'),
        ('UInteger', 'ListOfVariant'),
    ]
    def __str__(self):
        vals = [name + ": " + str(val) for name, val in self.__dict__.items()]
        return self.__class__.__name__ + "(" + ", ".join(vals) + ")"

    __repr__ = __str__

    def __init__(self):
        self.BooleanValue = []
        self.SByteValue = []
        self.ByteValue = []
        self.Int16Value = []
        self.UInt16Value = []
        self.Int32Value = []
        self.UInt32Value = []
        self.Int64Value = []
        self.UInt64Value = []
        self.FloatValue = []
        self.DoubleValue = []
        self.StringValue = []
        self.DateTimeValue = []
        self.GuidValue = []
        self.ByteStringValue = []
        self.XmlElementValue = []
        self.NodeIdValue = []
        self.ExpandedNodeIdValue = []
        self.QualifiedNameValue = []
        self.LocalizedTextValue = []
        self.StatusCodeValue = []
        self.VariantValue = []
        self.EnumerationValue = []
        self.StructureValue = []
        self.Number = []
        self.Integer = []
        self.UInteger = []


class UserScalarValueDataType(object):

    '''
    UserScalarValueDataType structure autogenerated from xml
    '''

    ua_types = [
        ('BooleanDataType', 'Boolean'),
        ('SByteDataType', 'SByte'),
        ('ByteDataType', 'Byte'),
        ('Int16DataType', 'Int16'),
        ('UInt16DataType', 'UInt16'),
        ('Int32DataType', 'Int32'),
        ('UInt32DataType', 'UInt32'),
        ('Int64DataType', 'Int64'),
        ('UInt64DataType', 'UInt64'),
        ('FloatDataType', 'Float'),
        ('DoubleDataType', 'Double'),
        ('StringDataType', 'String'),
        ('DateTimeDataType', 'DateTime'),
        ('GuidDataType', 'Guid'),
        ('ByteStringDataType', 'ByteString'),
        ('XmlElementDataType', 'XmlElement'),
        ('NodeIdDataType', 'NodeId'),
        ('ExpandedNodeIdDataType', 'ExpandedNodeId'),
        ('QualifiedNameDataType', 'QualifiedName'),
        ('LocalizedTextDataType', 'LocalizedText'),
        ('StatusCodeDataType', 'StatusCode'),
        ('VariantDataType', 'Variant'),
    ]
    def __str__(self):
        vals = [name + ": " + str(val) for name, val in self.__dict__.items()]
        return self.__class__.__name__ + "(" + ", ".join(vals) + ")"

    __repr__ = __str__

    def __init__(self):
        self.BooleanDataType = True
        self.SByteDataType = 0
        self.ByteDataType = 0
        self.Int16DataType = 0
        self.UInt16DataType = 0
        self.Int32DataType = 0
        self.UInt32DataType = 0
        self.Int64DataType = 0
        self.UInt64DataType = 0
        self.FloatDataType = 0
        self.DoubleDataType = 0
        self.StringDataType = ''
        self.DateTimeDataType = datetime.utcnow()
        self.GuidDataType = uuid.uuid4()
        self.ByteStringDataType = b''
        self.XmlElementDataType = ua.XmlElement()
        self.NodeIdDataType = ua.NodeId()
        self.ExpandedNodeIdDataType = ua.ExpandedNodeId()
        self.QualifiedNameDataType = ua.QualifiedName()
        self.LocalizedTextDataType = ua.LocalizedText()
        self.StatusCodeDataType = ua.StatusCode()
        self.VariantDataType = ua.Variant()


class UserArrayValueDataType(object):

    '''
    UserArrayValueDataType structure autogenerated from xml
    '''

    ua_types = [
        ('BooleanDataType', 'ListOfBoolean'),
        ('SByteDataType', 'ListOfSByte'),
        ('ByteDataType', 'ListOfByte'),
        ('Int16DataType', 'ListOfInt16'),
        ('UInt16DataType', 'ListOfUInt16'),
        ('Int32DataType', 'ListOfInt32'),
        ('UInt32DataType', 'ListOfUInt32'),
        ('Int64DataType', 'ListOfInt64'),
        ('UInt64DataType', 'ListOfUInt64'),
        ('FloatDataType', 'ListOfFloat'),
        ('DoubleDataType', 'ListOfDouble'),
        ('StringDataType', 'ListOfString'),
        ('DateTimeDataType', 'ListOfDateTime'),
        ('GuidDataType', 'ListOfGuid'),
        ('ByteStringDataType', 'ListOfByteString'),
        ('XmlElementDataType', 'ListOfXmlElement'),
        ('NodeIdDataType', 'ListOfNodeId'),
        ('ExpandedNodeIdDataType', 'ListOfExpandedNodeId'),
        ('QualifiedNameDataType', 'ListOfQualifiedName'),
        ('LocalizedTextDataType', 'ListOfLocalizedText'),
        ('StatusCodeDataType', 'ListOfStatusCode'),
        ('VariantDataType', 'ListOfVariant'),
    ]
    def __str__(self):
        vals = [name + ": " + str(val) for name, val in self.__dict__.items()]
        return self.__class__.__name__ + "(" + ", ".join(vals) + ")"

    __repr__ = __str__

    def __init__(self):
        self.BooleanDataType = []
        self.SByteDataType = []
        self.ByteDataType = []
        self.Int16DataType = []
        self.UInt16DataType = []
        self.Int32DataType = []
        self.UInt32DataType = []
        self.Int64DataType = []
        self.UInt64DataType = []
        self.FloatDataType = []
        self.DoubleDataType = []
        self.StringDataType = []
        self.DateTimeDataType = []
        self.GuidDataType = []
        self.ByteStringDataType = []
        self.XmlElementDataType = []
        self.NodeIdDataType = []
        self.ExpandedNodeIdDataType = []
        self.QualifiedNameDataType = []
        self.LocalizedTextDataType = []
        self.StatusCodeDataType = []
        self.VariantDataType = []
