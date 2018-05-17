# ./channel.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2018-05-07 19:43:56.146941 by PyXB version 1.2.6 using Python 3.6.3.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d545e4b8-5215-11e8-8463-acbc3296bf4d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: bool
class bool (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bool')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 179, 2)
    _Documentation = None
bool._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'bool', bool)
_module_typeBindings.bool = bool

# Atomic simple type: string
class string (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'string')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 183, 2)
    _Documentation = None
string._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'string', string)
_module_typeBindings.string = string

# Atomic simple type: int
class int (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'int')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 187, 2)
    _Documentation = None
int._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'int', int)
_module_typeBindings.int = int

# Complex type BaseType with content type EMPTY
class BaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BaseType = BaseType
Namespace.addCategoryObject('typeBinding', 'BaseType', BaseType)


# Complex type RpcBaseType with content type EMPTY
class RpcBaseType (BaseType):
    """Complex type RpcBaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 22, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcBaseType = RpcBaseType
Namespace.addCategoryObject('typeBinding', 'RpcBaseType', RpcBaseType)


# Complex type RpcCommandInfoType with content type ELEMENT_ONLY
class RpcCommandInfoType (RpcBaseType):
    """Complex type RpcCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 29, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element Call uses Python identifier Call
    __Call = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Call'), 'Call', '__AbsentNamespace0_RpcCommandInfoType_Call', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 33, 10), )

    
    Call = property(__Call.value, __Call.set, None, None)

    
    # Element Result uses Python identifier Result
    __Result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Result'), 'Result', '__AbsentNamespace0_RpcCommandInfoType_Result', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 34, 10), )

    
    Result = property(__Result.value, __Result.set, None, None)

    
    # Element Release uses Python identifier Release
    __Release = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Release'), 'Release', '__AbsentNamespace0_RpcCommandInfoType_Release', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 35, 10), )

    
    Release = property(__Release.value, __Release.set, None, None)

    _ElementMap.update({
        __Call.name() : __Call,
        __Result.name() : __Result,
        __Release.name() : __Release
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcCommandInfoType = RpcCommandInfoType
Namespace.addCategoryObject('typeBinding', 'RpcCommandInfoType', RpcCommandInfoType)


# Complex type RpcCommandContentInfoType with content type EMPTY
class RpcCommandContentInfoType (RpcBaseType):
    """Complex type RpcCommandContentInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcCommandContentInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 41, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcCommandContentInfoType = RpcCommandContentInfoType
Namespace.addCategoryObject('typeBinding', 'RpcCommandContentInfoType', RpcCommandContentInfoType)


# Complex type RpcSharedObjectKeyInfoType with content type ELEMENT_ONLY
class RpcSharedObjectKeyInfoType (RpcBaseType):
    """Complex type RpcSharedObjectKeyInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcSharedObjectKeyInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 86, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__AbsentNamespace0_RpcSharedObjectKeyInfoType_Value', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 90, 10), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcSharedObjectKeyInfoType = RpcSharedObjectKeyInfoType
Namespace.addCategoryObject('typeBinding', 'RpcSharedObjectKeyInfoType', RpcSharedObjectKeyInfoType)


# Complex type RpcMethodReferencInfoType with content type ELEMENT_ONLY
class RpcMethodReferencInfoType (RpcBaseType):
    """Complex type RpcMethodReferencInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcMethodReferencInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 96, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element GenericSignatureTypes uses Python identifier GenericSignatureTypes
    __GenericSignatureTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GenericSignatureTypes'), 'GenericSignatureTypes', '__AbsentNamespace0_RpcMethodReferencInfoType_GenericSignatureTypes', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10), )

    
    GenericSignatureTypes = property(__GenericSignatureTypes.value, __GenericSignatureTypes.set, None, None)

    
    # Attribute DeclaringTypeName uses Python identifier DeclaringTypeName
    __DeclaringTypeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DeclaringTypeName'), 'DeclaringTypeName', '__AbsentNamespace0_RpcMethodReferencInfoType_DeclaringTypeName', _module_typeBindings.string, required=True)
    __DeclaringTypeName._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 102, 8)
    __DeclaringTypeName._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 102, 8)
    
    DeclaringTypeName = property(__DeclaringTypeName.value, __DeclaringTypeName.set, None, None)

    
    # Attribute MethodName uses Python identifier MethodName
    __MethodName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MethodName'), 'MethodName', '__AbsentNamespace0_RpcMethodReferencInfoType_MethodName', _module_typeBindings.string, required=True)
    __MethodName._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 103, 8)
    __MethodName._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 103, 8)
    
    MethodName = property(__MethodName.value, __MethodName.set, None, None)

    
    # Attribute MetadataToken uses Python identifier MetadataToken
    __MetadataToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MetadataToken'), 'MetadataToken', '__AbsentNamespace0_RpcMethodReferencInfoType_MetadataToken', _module_typeBindings.int, required=True)
    __MetadataToken._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 104, 8)
    __MetadataToken._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 104, 8)
    
    MetadataToken = property(__MetadataToken.value, __MetadataToken.set, None, None)

    _ElementMap.update({
        __GenericSignatureTypes.name() : __GenericSignatureTypes
    })
    _AttributeMap.update({
        __DeclaringTypeName.name() : __DeclaringTypeName,
        __MethodName.name() : __MethodName,
        __MetadataToken.name() : __MetadataToken
    })
_module_typeBindings.RpcMethodReferencInfoType = RpcMethodReferencInfoType
Namespace.addCategoryObject('typeBinding', 'RpcMethodReferencInfoType', RpcMethodReferencInfoType)


# Complex type RpcMethodReferenceGenericTypesInfoType with content type ELEMENT_ONLY
class RpcMethodReferenceGenericTypesInfoType (RpcBaseType):
    """Complex type RpcMethodReferenceGenericTypesInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcMethodReferenceGenericTypesInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 109, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element TypeName uses Python identifier TypeName
    __TypeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TypeName'), 'TypeName', '__AbsentNamespace0_RpcMethodReferenceGenericTypesInfoType_TypeName', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10), )

    
    TypeName = property(__TypeName.value, __TypeName.set, None, None)

    _ElementMap.update({
        __TypeName.name() : __TypeName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcMethodReferenceGenericTypesInfoType = RpcMethodReferenceGenericTypesInfoType
Namespace.addCategoryObject('typeBinding', 'RpcMethodReferenceGenericTypesInfoType', RpcMethodReferenceGenericTypesInfoType)


# Complex type RpcValueContainersListType with content type ELEMENT_ONLY
class RpcValueContainersListType (RpcBaseType):
    """Complex type RpcValueContainersListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcValueContainersListType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 119, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__AbsentNamespace0_RpcValueContainersListType_Value', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 123, 10), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcValueContainersListType = RpcValueContainersListType
Namespace.addCategoryObject('typeBinding', 'RpcValueContainersListType', RpcValueContainersListType)


# Complex type RpcValueContainerType with content type ELEMENT_ONLY
class RpcValueContainerType (RpcBaseType):
    """Complex type RpcValueContainerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcValueContainerType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 129, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element Instance uses Python identifier Instance
    __Instance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Instance'), 'Instance', '__AbsentNamespace0_RpcValueContainerType_Instance', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 134, 12), )

    
    Instance = property(__Instance.value, __Instance.set, None, None)

    
    # Element String uses Python identifier String
    __String = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'String'), 'String', '__AbsentNamespace0_RpcValueContainerType_String', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 135, 12), )

    
    String = property(__String.value, __String.set, None, None)

    
    # Element Int32 uses Python identifier Int32
    __Int32 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Int32'), 'Int32', '__AbsentNamespace0_RpcValueContainerType_Int32', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 136, 12), )

    
    Int32 = property(__Int32.value, __Int32.set, None, None)

    
    # Element Boolean uses Python identifier Boolean
    __Boolean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Boolean'), 'Boolean', '__AbsentNamespace0_RpcValueContainerType_Boolean', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 137, 12), )

    
    Boolean = property(__Boolean.value, __Boolean.set, None, None)

    _ElementMap.update({
        __Instance.name() : __Instance,
        __String.name() : __String,
        __Int32.name() : __Int32,
        __Boolean.name() : __Boolean
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcValueContainerType = RpcValueContainerType
Namespace.addCategoryObject('typeBinding', 'RpcValueContainerType', RpcValueContainerType)


# Complex type RpcExceptionDescriptionInfoType with content type ELEMENT_ONLY
class RpcExceptionDescriptionInfoType (RpcBaseType):
    """Complex type RpcExceptionDescriptionInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcExceptionDescriptionInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 144, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element Message uses Python identifier Message
    __Message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Message'), 'Message', '__AbsentNamespace0_RpcExceptionDescriptionInfoType_Message', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 148, 10), )

    
    Message = property(__Message.value, __Message.set, None, None)

    
    # Element StackTrace uses Python identifier StackTrace
    __StackTrace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StackTrace'), 'StackTrace', '__AbsentNamespace0_RpcExceptionDescriptionInfoType_StackTrace', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 149, 10), )

    
    StackTrace = property(__StackTrace.value, __StackTrace.set, None, None)

    
    # Element InnerException uses Python identifier InnerException
    __InnerException = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InnerException'), 'InnerException', '__AbsentNamespace0_RpcExceptionDescriptionInfoType_InnerException', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10), )

    
    InnerException = property(__InnerException.value, __InnerException.set, None, None)

    _ElementMap.update({
        __Message.name() : __Message,
        __StackTrace.name() : __StackTrace,
        __InnerException.name() : __InnerException
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcExceptionDescriptionInfoType = RpcExceptionDescriptionInfoType
Namespace.addCategoryObject('typeBinding', 'RpcExceptionDescriptionInfoType', RpcExceptionDescriptionInfoType)


# Complex type RpcRemoteObjectReferenceInfoType with content type ELEMENT_ONLY
class RpcRemoteObjectReferenceInfoType (RpcBaseType):
    """Complex type RpcRemoteObjectReferenceInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcRemoteObjectReferenceInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 156, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element RemoteInstanceId uses Python identifier RemoteInstanceId
    __RemoteInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId'), 'RemoteInstanceId', '__AbsentNamespace0_RpcRemoteObjectReferenceInfoType_RemoteInstanceId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 160, 10), )

    
    RemoteInstanceId = property(__RemoteInstanceId.value, __RemoteInstanceId.set, None, None)

    
    # Element InterfaceTypes uses Python identifier InterfaceTypes
    __InterfaceTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InterfaceTypes'), 'InterfaceTypes', '__AbsentNamespace0_RpcRemoteObjectReferenceInfoType_InterfaceTypes', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 161, 10), )

    
    InterfaceTypes = property(__InterfaceTypes.value, __InterfaceTypes.set, None, None)

    _ElementMap.update({
        __RemoteInstanceId.name() : __RemoteInstanceId,
        __InterfaceTypes.name() : __InterfaceTypes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcRemoteObjectReferenceInfoType = RpcRemoteObjectReferenceInfoType
Namespace.addCategoryObject('typeBinding', 'RpcRemoteObjectReferenceInfoType', RpcRemoteObjectReferenceInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (RpcBaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 162, 12)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_Type', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 166, 20), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type RpcCallCommandInfoType with content type ELEMENT_ONLY
class RpcCallCommandInfoType (RpcCommandContentInfoType):
    """Complex type RpcCallCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcCallCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 50, 2)
    _ElementMap = RpcCommandContentInfoType._ElementMap.copy()
    _AttributeMap = RpcCommandContentInfoType._AttributeMap.copy()
    # Base type is RpcCommandContentInfoType
    
    # Element RemoteInstanceId uses Python identifier RemoteInstanceId
    __RemoteInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId'), 'RemoteInstanceId', '__AbsentNamespace0_RpcCallCommandInfoType_RemoteInstanceId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 54, 10), )

    
    RemoteInstanceId = property(__RemoteInstanceId.value, __RemoteInstanceId.set, None, None)

    
    # Element MethodId uses Python identifier MethodId
    __MethodId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MethodId'), 'MethodId', '__AbsentNamespace0_RpcCallCommandInfoType_MethodId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 55, 10), )

    
    MethodId = property(__MethodId.value, __MethodId.set, None, None)

    
    # Element Arguments uses Python identifier Arguments
    __Arguments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Arguments'), 'Arguments', '__AbsentNamespace0_RpcCallCommandInfoType_Arguments', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 56, 10), )

    
    Arguments = property(__Arguments.value, __Arguments.set, None, None)

    
    # Attribute CallId uses Python identifier CallId
    __CallId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CallId'), 'CallId', '__AbsentNamespace0_RpcCallCommandInfoType_CallId', _module_typeBindings.int, required=True)
    __CallId._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 58, 8)
    __CallId._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 58, 8)
    
    CallId = property(__CallId.value, __CallId.set, None, None)

    _ElementMap.update({
        __RemoteInstanceId.name() : __RemoteInstanceId,
        __MethodId.name() : __MethodId,
        __Arguments.name() : __Arguments
    })
    _AttributeMap.update({
        __CallId.name() : __CallId
    })
_module_typeBindings.RpcCallCommandInfoType = RpcCallCommandInfoType
Namespace.addCategoryObject('typeBinding', 'RpcCallCommandInfoType', RpcCallCommandInfoType)


# Complex type RpcResultCommandInfoType with content type ELEMENT_ONLY
class RpcResultCommandInfoType (RpcCommandContentInfoType):
    """Complex type RpcResultCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcResultCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 63, 2)
    _ElementMap = RpcCommandContentInfoType._ElementMap.copy()
    _AttributeMap = RpcCommandContentInfoType._AttributeMap.copy()
    # Base type is RpcCommandContentInfoType
    
    # Element ReturnValue uses Python identifier ReturnValue
    __ReturnValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ReturnValue'), 'ReturnValue', '__AbsentNamespace0_RpcResultCommandInfoType_ReturnValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 67, 10), )

    
    ReturnValue = property(__ReturnValue.value, __ReturnValue.set, None, None)

    
    # Element OutArguments uses Python identifier OutArguments
    __OutArguments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OutArguments'), 'OutArguments', '__AbsentNamespace0_RpcResultCommandInfoType_OutArguments', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 68, 10), )

    
    OutArguments = property(__OutArguments.value, __OutArguments.set, None, None)

    
    # Element Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Exception'), 'Exception', '__AbsentNamespace0_RpcResultCommandInfoType_Exception', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 69, 10), )

    
    Exception = property(__Exception.value, __Exception.set, None, None)

    
    # Attribute CallId uses Python identifier CallId
    __CallId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CallId'), 'CallId', '__AbsentNamespace0_RpcResultCommandInfoType_CallId', _module_typeBindings.int, required=True)
    __CallId._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 71, 8)
    __CallId._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 71, 8)
    
    CallId = property(__CallId.value, __CallId.set, None, None)

    _ElementMap.update({
        __ReturnValue.name() : __ReturnValue,
        __OutArguments.name() : __OutArguments,
        __Exception.name() : __Exception
    })
    _AttributeMap.update({
        __CallId.name() : __CallId
    })
_module_typeBindings.RpcResultCommandInfoType = RpcResultCommandInfoType
Namespace.addCategoryObject('typeBinding', 'RpcResultCommandInfoType', RpcResultCommandInfoType)


# Complex type RpcReleaseCommandInfoType with content type ELEMENT_ONLY
class RpcReleaseCommandInfoType (RpcCommandContentInfoType):
    """Complex type RpcReleaseCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcReleaseCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 76, 2)
    _ElementMap = RpcCommandContentInfoType._ElementMap.copy()
    _AttributeMap = RpcCommandContentInfoType._AttributeMap.copy()
    # Base type is RpcCommandContentInfoType
    
    # Element RemoteInstanceId uses Python identifier RemoteInstanceId
    __RemoteInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId'), 'RemoteInstanceId', '__AbsentNamespace0_RpcReleaseCommandInfoType_RemoteInstanceId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 80, 10), )

    
    RemoteInstanceId = property(__RemoteInstanceId.value, __RemoteInstanceId.set, None, None)

    _ElementMap.update({
        __RemoteInstanceId.name() : __RemoteInstanceId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcReleaseCommandInfoType = RpcReleaseCommandInfoType
Namespace.addCategoryObject('typeBinding', 'RpcReleaseCommandInfoType', RpcReleaseCommandInfoType)


RpcCommand = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RpcCommand'), RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 15, 2))
Namespace.addCategoryObject('elementBinding', RpcCommand.name().localName(), RpcCommand)



RpcCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Call'), RpcCallCommandInfoType, scope=RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 33, 10)))

RpcCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Result'), RpcResultCommandInfoType, scope=RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 34, 10)))

RpcCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Release'), RpcReleaseCommandInfoType, scope=RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 35, 10)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Call')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 33, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Result')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 34, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Release')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 35, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcCommandInfoType._Automaton = _BuildAutomaton()




RpcSharedObjectKeyInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Value'), string, scope=RpcSharedObjectKeyInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 90, 10)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcSharedObjectKeyInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Value')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 90, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcSharedObjectKeyInfoType._Automaton = _BuildAutomaton_()




RpcMethodReferencInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GenericSignatureTypes'), RpcMethodReferenceGenericTypesInfoType, scope=RpcMethodReferencInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcMethodReferencInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'GenericSignatureTypes')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RpcMethodReferencInfoType._Automaton = _BuildAutomaton_2()




RpcMethodReferenceGenericTypesInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TypeName'), string, scope=RpcMethodReferenceGenericTypesInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcMethodReferenceGenericTypesInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'TypeName')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RpcMethodReferenceGenericTypesInfoType._Automaton = _BuildAutomaton_3()




RpcValueContainersListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Value'), RpcValueContainerType, scope=RpcValueContainersListType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 123, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 122, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcValueContainersListType._UseForTag(pyxb.namespace.ExpandedName(None, 'Value')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 123, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RpcValueContainersListType._Automaton = _BuildAutomaton_4()




RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Instance'), BaseType, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 134, 12)))

RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'String'), string, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 135, 12)))

RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Int32'), int, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 136, 12)))

RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Boolean'), bool, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 137, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(None, 'Instance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 134, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(None, 'String')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 135, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(None, 'Int32')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 136, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(None, 'Boolean')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 137, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcValueContainerType._Automaton = _BuildAutomaton_5()




RpcExceptionDescriptionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Message'), string, scope=RpcExceptionDescriptionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 148, 10)))

RpcExceptionDescriptionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StackTrace'), string, scope=RpcExceptionDescriptionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 149, 10)))

RpcExceptionDescriptionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InnerException'), RpcExceptionDescriptionInfoType, scope=RpcExceptionDescriptionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcExceptionDescriptionInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Message')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 148, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcExceptionDescriptionInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'StackTrace')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 149, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcExceptionDescriptionInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'InnerException')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcExceptionDescriptionInfoType._Automaton = _BuildAutomaton_6()




RpcRemoteObjectReferenceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId'), RpcSharedObjectKeyInfoType, scope=RpcRemoteObjectReferenceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 160, 10)))

RpcRemoteObjectReferenceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InterfaceTypes'), CTD_ANON, scope=RpcRemoteObjectReferenceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 161, 10)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcRemoteObjectReferenceInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 160, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcRemoteObjectReferenceInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'InterfaceTypes')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 161, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcRemoteObjectReferenceInfoType._Automaton = _BuildAutomaton_7()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Type'), string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 166, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 165, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Type')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 166, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_8()




RpcCallCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId'), RpcSharedObjectKeyInfoType, scope=RpcCallCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 54, 10)))

RpcCallCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MethodId'), RpcMethodReferencInfoType, scope=RpcCallCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 55, 10)))

RpcCallCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Arguments'), RpcValueContainersListType, scope=RpcCallCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 56, 10)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcCallCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 54, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcCallCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'MethodId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 55, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCallCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Arguments')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 56, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcCallCommandInfoType._Automaton = _BuildAutomaton_9()




RpcResultCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ReturnValue'), RpcValueContainerType, scope=RpcResultCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 67, 10)))

RpcResultCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OutArguments'), RpcValueContainersListType, scope=RpcResultCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 68, 10)))

RpcResultCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Exception'), RpcExceptionDescriptionInfoType, scope=RpcResultCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 69, 10)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcResultCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'ReturnValue')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 67, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcResultCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'OutArguments')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 68, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcResultCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'Exception')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 69, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcResultCommandInfoType._Automaton = _BuildAutomaton_10()




RpcReleaseCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId'), RpcSharedObjectKeyInfoType, scope=RpcReleaseCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 80, 10)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcReleaseCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'RemoteInstanceId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 80, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcReleaseCommandInfoType._Automaton = _BuildAutomaton_11()

