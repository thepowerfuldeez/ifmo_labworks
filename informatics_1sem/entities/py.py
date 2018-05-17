# ./entities/py.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:79b323c55194720203ac63f811545a5d38486007
# Generated 2018-05-07 19:42:33.315104 by PyXB version 1.2.6 using Python 3.6.3.final.0
# Namespace EventsGraphNavigator.Interaction.Entities

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a3c6f882-5215-11e8-a469-acbc3296bf4d')

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
Namespace = pyxb.namespace.NamespaceForURI('EventsGraphNavigator.Interaction.Entities', create_if_missing=True)
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


# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}bool
class bool (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bool')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 179, 2)
    _Documentation = None
bool._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'bool', bool)
_module_typeBindings.bool = bool

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}string
class string (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'string')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 183, 2)
    _Documentation = None
string._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'string', string)
_module_typeBindings.string = string

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}int
class int (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'int')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 187, 2)
    _Documentation = None
int._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'int', int)
_module_typeBindings.int = int

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}GuidString
class GuidString (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GuidString')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1300, 2)
    _Documentation = None
GuidString._CF_pattern = pyxb.binding.facets.CF_pattern()
GuidString._CF_pattern.addPattern(pattern='([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})|(\\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\})')
GuidString._InitializeFacetMap(GuidString._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'GuidString', GuidString)
_module_typeBindings.GuidString = GuidString

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}DateTime
class DateTime (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTime')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1308, 2)
    _Documentation = None
DateTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DateTime', DateTime)
_module_typeBindings.DateTime = DateTime

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}SourceChangeKindType
class SourceChangeKindType (string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourceChangeKindType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 208, 2)
    _Documentation = None
SourceChangeKindType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SourceChangeKindType, enum_prefix=None)
SourceChangeKindType.NotChanged = SourceChangeKindType._CF_enumeration.addEnumeration(unicode_value='NotChanged', tag='NotChanged')
SourceChangeKindType.AddedLines = SourceChangeKindType._CF_enumeration.addEnumeration(unicode_value='AddedLines', tag='AddedLines')
SourceChangeKindType.Rewritten = SourceChangeKindType._CF_enumeration.addEnumeration(unicode_value='Rewritten', tag='Rewritten')
SourceChangeKindType.FileRemoved = SourceChangeKindType._CF_enumeration.addEnumeration(unicode_value='FileRemoved', tag='FileRemoved')
SourceChangeKindType.FileAdded = SourceChangeKindType._CF_enumeration.addEnumeration(unicode_value='FileAdded', tag='FileAdded')
SourceChangeKindType.Renamed = SourceChangeKindType._CF_enumeration.addEnumeration(unicode_value='Renamed', tag='Renamed')
SourceChangeKindType._InitializeFacetMap(SourceChangeKindType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SourceChangeKindType', SourceChangeKindType)
_module_typeBindings.SourceChangeKindType = SourceChangeKindType

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}TagMatchingModeType
class TagMatchingModeType (string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagMatchingModeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 361, 2)
    _Documentation = None
TagMatchingModeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TagMatchingModeType, enum_prefix=None)
TagMatchingModeType.ByTree = TagMatchingModeType._CF_enumeration.addEnumeration(unicode_value='ByTree', tag='ByTree')
TagMatchingModeType.ByTerms = TagMatchingModeType._CF_enumeration.addEnumeration(unicode_value='ByTerms', tag='ByTerms')
TagMatchingModeType.ByAllTerms = TagMatchingModeType._CF_enumeration.addEnumeration(unicode_value='ByAllTerms', tag='ByAllTerms')
TagMatchingModeType._InitializeFacetMap(TagMatchingModeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TagMatchingModeType', TagMatchingModeType)
_module_typeBindings.TagMatchingModeType = TagMatchingModeType

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}StringMatchingModeType
class StringMatchingModeType (string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StringMatchingModeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 676, 2)
    _Documentation = None
StringMatchingModeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StringMatchingModeType, enum_prefix=None)
StringMatchingModeType.String = StringMatchingModeType._CF_enumeration.addEnumeration(unicode_value='String', tag='String')
StringMatchingModeType.Regex = StringMatchingModeType._CF_enumeration.addEnumeration(unicode_value='Regex', tag='Regex')
StringMatchingModeType._InitializeFacetMap(StringMatchingModeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StringMatchingModeType', StringMatchingModeType)
_module_typeBindings.StringMatchingModeType = StringMatchingModeType

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyValueType
class TagInstanceKeyValueType (string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceKeyValueType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 683, 2)
    _Documentation = None
TagInstanceKeyValueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TagInstanceKeyValueType, enum_prefix=None)
TagInstanceKeyValueType.String = TagInstanceKeyValueType._CF_enumeration.addEnumeration(unicode_value='String', tag='String')
TagInstanceKeyValueType.Integer = TagInstanceKeyValueType._CF_enumeration.addEnumeration(unicode_value='Integer', tag='Integer')
TagInstanceKeyValueType.DateTime = TagInstanceKeyValueType._CF_enumeration.addEnumeration(unicode_value='DateTime', tag='DateTime')
TagInstanceKeyValueType.Decimal = TagInstanceKeyValueType._CF_enumeration.addEnumeration(unicode_value='Decimal', tag='Decimal')
TagInstanceKeyValueType._InitializeFacetMap(TagInstanceKeyValueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TagInstanceKeyValueType', TagInstanceKeyValueType)
_module_typeBindings.TagInstanceKeyValueType = TagInstanceKeyValueType

# Atomic simple type: {EventsGraphNavigator.Interaction.Entities}TaskStateType
class TaskStateType (string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaskStateType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1262, 2)
    _Documentation = None
TaskStateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TaskStateType, enum_prefix=None)
TaskStateType.Queued = TaskStateType._CF_enumeration.addEnumeration(unicode_value='Queued', tag='Queued')
TaskStateType.Running = TaskStateType._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
TaskStateType.Finised = TaskStateType._CF_enumeration.addEnumeration(unicode_value='Finised', tag='Finised')
TaskStateType._InitializeFacetMap(TaskStateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaskStateType', TaskStateType)
_module_typeBindings.TaskStateType = TaskStateType

# Complex type {EventsGraphNavigator.Interaction.Entities}BaseType with content type EMPTY
class BaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {EventsGraphNavigator.Interaction.Entities}BaseType with content type EMPTY"""
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcBaseType with content type EMPTY
class RpcBaseType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcBaseType with content type EMPTY"""
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


# Complex type {EventsGraphNavigator.Interaction.Entities}AnyRootEntitiesType with content type ELEMENT_ONLY
class AnyRootEntitiesType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}AnyRootEntitiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyRootEntitiesType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 18, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}EntityIds uses Python identifier EntityIds
    __EntityIds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EntityIds'), 'EntityIds', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesEntityIds', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 14, 2), )

    
    EntityIds = property(__EntityIds.value, __EntityIds.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourcesFolder uses Python identifier SourcesFolder
    __SourcesFolder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourcesFolder'), 'SourcesFolder', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesSourcesFolder', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 89, 2), )

    
    SourcesFolder = property(__SourcesFolder.value, __SourcesFolder.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourcesSource uses Python identifier SourcesSource
    __SourcesSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourcesSource'), 'SourcesSource', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesSourcesSource', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 90, 2), )

    
    SourcesSource = property(__SourcesSource.value, __SourcesSource.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceInfo uses Python identifier SourceInfo
    __SourceInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceInfo'), 'SourceInfo', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesSourceInfo', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 92, 2), )

    
    SourceInfo = property(__SourceInfo.value, __SourceInfo.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternsFolder uses Python identifier PatternsFolder
    __PatternsFolder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternsFolder'), 'PatternsFolder', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesPatternsFolder', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 224, 2), )

    
    PatternsFolder = property(__PatternsFolder.value, __PatternsFolder.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternsRegex uses Python identifier PatternsRegex
    __PatternsRegex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternsRegex'), 'PatternsRegex', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesPatternsRegex', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 225, 2), )

    
    PatternsRegex = property(__PatternsRegex.value, __PatternsRegex.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternsTag uses Python identifier PatternsTag
    __PatternsTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternsTag'), 'PatternsTag', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesPatternsTag', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 226, 2), )

    
    PatternsTag = property(__PatternsTag.value, __PatternsTag.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternsLine uses Python identifier PatternsLine
    __PatternsLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternsLine'), 'PatternsLine', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesPatternsLine', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 227, 2), )

    
    PatternsLine = property(__PatternsLine.value, __PatternsLine.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagPatternInfo uses Python identifier TagPatternInfo
    __TagPatternInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagPatternInfo'), 'TagPatternInfo', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesTagPatternInfo', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 229, 2), )

    
    TagPatternInfo = property(__TagPatternInfo.value, __TagPatternInfo.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LinePatternInfo uses Python identifier LinePatternInfo
    __LinePatternInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LinePatternInfo'), 'LinePatternInfo', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesLinePatternInfo', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 230, 2), )

    
    LinePatternInfo = property(__LinePatternInfo.value, __LinePatternInfo.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LogMessage uses Python identifier LogMessage
    __LogMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogMessage'), 'LogMessage', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesLogMessage', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 486, 2), )

    
    LogMessage = property(__LogMessage.value, __LogMessage.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LogMessages uses Python identifier LogMessages
    __LogMessages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogMessages'), 'LogMessages', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesLogMessages', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 487, 2), )

    
    LogMessages = property(__LogMessages.value, __LogMessages.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstance uses Python identifier TagInstance
    __TagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), 'TagInstance', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesTagInstance', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 542, 2), )

    
    TagInstance = property(__TagInstance.value, __TagInstance.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstances uses Python identifier TagInstances
    __TagInstances = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstances'), 'TagInstances', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesTagInstances', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 543, 2), )

    
    TagInstances = property(__TagInstances.value, __TagInstances.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LogMessagesContainingTextFromSourceFixedQuery uses Python identifier LogMessagesContainingTextFromSourceFixedQuery
    __LogMessagesContainingTextFromSourceFixedQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesContainingTextFromSourceFixedQuery'), 'LogMessagesContainingTextFromSourceFixedQuery', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesLogMessagesContainingTextFromSourceFixedQuery', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 716, 2), )

    
    LogMessagesContainingTextFromSourceFixedQuery = property(__LogMessagesContainingTextFromSourceFixedQuery.value, __LogMessagesContainingTextFromSourceFixedQuery.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LogMessagesCustomQuery uses Python identifier LogMessagesCustomQuery
    __LogMessagesCustomQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesCustomQuery'), 'LogMessagesCustomQuery', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesLogMessagesCustomQuery', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 739, 2), )

    
    LogMessagesCustomQuery = property(__LogMessagesCustomQuery.value, __LogMessagesCustomQuery.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstancesCustomQuery uses Python identifier TagInstancesCustomQuery
    __TagInstancesCustomQuery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstancesCustomQuery'), 'TagInstancesCustomQuery', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesTagInstancesCustomQuery', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 741, 2), )

    
    TagInstancesCustomQuery = property(__TagInstancesCustomQuery.value, __TagInstancesCustomQuery.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TaskEntity uses Python identifier TaskEntity
    __TaskEntity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TaskEntity'), 'TaskEntity', '__EventsGraphNavigator_Interaction_Entities_AnyRootEntitiesType_EventsGraphNavigator_Interaction_EntitiesTaskEntity', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1245, 2), )

    
    TaskEntity = property(__TaskEntity.value, __TaskEntity.set, None, None)

    _ElementMap.update({
        __EntityIds.name() : __EntityIds,
        __SourcesFolder.name() : __SourcesFolder,
        __SourcesSource.name() : __SourcesSource,
        __SourceInfo.name() : __SourceInfo,
        __PatternsFolder.name() : __PatternsFolder,
        __PatternsRegex.name() : __PatternsRegex,
        __PatternsTag.name() : __PatternsTag,
        __PatternsLine.name() : __PatternsLine,
        __TagPatternInfo.name() : __TagPatternInfo,
        __LinePatternInfo.name() : __LinePatternInfo,
        __LogMessage.name() : __LogMessage,
        __LogMessages.name() : __LogMessages,
        __TagInstance.name() : __TagInstance,
        __TagInstances.name() : __TagInstances,
        __LogMessagesContainingTextFromSourceFixedQuery.name() : __LogMessagesContainingTextFromSourceFixedQuery,
        __LogMessagesCustomQuery.name() : __LogMessagesCustomQuery,
        __TagInstancesCustomQuery.name() : __TagInstancesCustomQuery,
        __TaskEntity.name() : __TaskEntity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AnyRootEntitiesType = AnyRootEntitiesType
Namespace.addCategoryObject('typeBinding', 'AnyRootEntitiesType', AnyRootEntitiesType)


# Complex type {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType with content type EMPTY
class IdentifiedEntityBaseType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifiedEntityBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 62, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Attribute IdString uses Python identifier IdString
    __IdString = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IdString'), 'IdString', '__EventsGraphNavigator_Interaction_Entities_IdentifiedEntityBaseType_IdString', _module_typeBindings.GuidString, required=True)
    __IdString._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 65, 8)
    __IdString._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 65, 8)
    
    IdString = property(__IdString.value, __IdString.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __IdString.name() : __IdString
    })
_module_typeBindings.IdentifiedEntityBaseType = IdentifiedEntityBaseType
Namespace.addCategoryObject('typeBinding', 'IdentifiedEntityBaseType', IdentifiedEntityBaseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 109, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Folder uses Python identifier Folder
    __Folder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Folder'), 'Folder', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_EventsGraphNavigator_Interaction_EntitiesFolder', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 113, 20), )

    
    Folder = property(__Folder.value, __Folder.set, None, None)

    _ElementMap.update({
        __Folder.name() : __Folder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 120, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Source'), 'Source', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON__EventsGraphNavigator_Interaction_EntitiesSource', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 124, 20), )

    
    Source = property(__Source.value, __Source.set, None, None)

    _ElementMap.update({
        __Source.name() : __Source
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 142, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Source'), 'Source', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_2_EventsGraphNavigator_Interaction_EntitiesSource', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 146, 20), )

    
    Source = property(__Source.value, __Source.set, None, None)

    _ElementMap.update({
        __Source.name() : __Source
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {EventsGraphNavigator.Interaction.Entities}SourceControlOptionsInfoType with content type EMPTY
class SourceControlOptionsInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourceControlOptionsInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourceControlOptionsInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 171, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Attribute IsLive uses Python identifier IsLive
    __IsLive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsLive'), 'IsLive', '__EventsGraphNavigator_Interaction_Entities_SourceControlOptionsInfoType_IsLive', _module_typeBindings.bool, required=True)
    __IsLive._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 176, 8)
    __IsLive._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 176, 8)
    
    IsLive = property(__IsLive.value, __IsLive.set, None, None)

    
    # Attribute IsUserMaintained uses Python identifier IsUserMaintained
    __IsUserMaintained = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsUserMaintained'), 'IsUserMaintained', '__EventsGraphNavigator_Interaction_Entities_SourceControlOptionsInfoType_IsUserMaintained', _module_typeBindings.bool, required=True)
    __IsUserMaintained._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 177, 8)
    __IsUserMaintained._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 177, 8)
    
    IsUserMaintained = property(__IsUserMaintained.value, __IsUserMaintained.set, None, None)

    
    # Attribute IsEnabled uses Python identifier IsEnabled
    __IsEnabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsEnabled'), 'IsEnabled', '__EventsGraphNavigator_Interaction_Entities_SourceControlOptionsInfoType_IsEnabled', _module_typeBindings.bool, required=True)
    __IsEnabled._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 178, 8)
    __IsEnabled._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 178, 8)
    
    IsEnabled = property(__IsEnabled.value, __IsEnabled.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __IsLive.name() : __IsLive,
        __IsUserMaintained.name() : __IsUserMaintained,
        __IsEnabled.name() : __IsEnabled
    })
_module_typeBindings.SourceControlOptionsInfoType = SourceControlOptionsInfoType
Namespace.addCategoryObject('typeBinding', 'SourceControlOptionsInfoType', SourceControlOptionsInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}SourceFilterOptionsInfoType with content type ELEMENT_ONLY
class SourceFilterOptionsInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourceFilterOptionsInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourceFilterOptionsInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 183, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}BaseFolders uses Python identifier BaseFolders
    __BaseFolders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BaseFolders'), 'BaseFolders', '__EventsGraphNavigator_Interaction_Entities_SourceFilterOptionsInfoType_EventsGraphNavigator_Interaction_EntitiesBaseFolders', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 187, 10), )

    
    BaseFolders = property(__BaseFolders.value, __BaseFolders.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}FilesWildcard uses Python identifier FilesWildcard
    __FilesWildcard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FilesWildcard'), 'FilesWildcard', '__EventsGraphNavigator_Interaction_Entities_SourceFilterOptionsInfoType_EventsGraphNavigator_Interaction_EntitiesFilesWildcard', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 188, 10), )

    
    FilesWildcard = property(__FilesWildcard.value, __FilesWildcard.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}FoldersWildcard uses Python identifier FoldersWildcard
    __FoldersWildcard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FoldersWildcard'), 'FoldersWildcard', '__EventsGraphNavigator_Interaction_Entities_SourceFilterOptionsInfoType_EventsGraphNavigator_Interaction_EntitiesFoldersWildcard', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 189, 10), )

    
    FoldersWildcard = property(__FoldersWildcard.value, __FoldersWildcard.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ExcludedFiles uses Python identifier ExcludedFiles
    __ExcludedFiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExcludedFiles'), 'ExcludedFiles', '__EventsGraphNavigator_Interaction_Entities_SourceFilterOptionsInfoType_EventsGraphNavigator_Interaction_EntitiesExcludedFiles', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 190, 10), )

    
    ExcludedFiles = property(__ExcludedFiles.value, __ExcludedFiles.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ExcludedFolders uses Python identifier ExcludedFolders
    __ExcludedFolders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExcludedFolders'), 'ExcludedFolders', '__EventsGraphNavigator_Interaction_Entities_SourceFilterOptionsInfoType_EventsGraphNavigator_Interaction_EntitiesExcludedFolders', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 191, 10), )

    
    ExcludedFolders = property(__ExcludedFolders.value, __ExcludedFolders.set, None, None)

    _ElementMap.update({
        __BaseFolders.name() : __BaseFolders,
        __FilesWildcard.name() : __FilesWildcard,
        __FoldersWildcard.name() : __FoldersWildcard,
        __ExcludedFiles.name() : __ExcludedFiles,
        __ExcludedFolders.name() : __ExcludedFolders
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SourceFilterOptionsInfoType = SourceFilterOptionsInfoType
Namespace.addCategoryObject('typeBinding', 'SourceFilterOptionsInfoType', SourceFilterOptionsInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}SourcePostFilterActionInfoType with content type ELEMENT_ONLY
class SourcePostFilterActionInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourcePostFilterActionInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourcePostFilterActionInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 197, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}CommandLine uses Python identifier CommandLine
    __CommandLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommandLine'), 'CommandLine', '__EventsGraphNavigator_Interaction_Entities_SourcePostFilterActionInfoType_EventsGraphNavigator_Interaction_EntitiesCommandLine', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 201, 10), )

    
    CommandLine = property(__CommandLine.value, __CommandLine.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SubFilterSource uses Python identifier SubFilterSource
    __SubFilterSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubFilterSource'), 'SubFilterSource', '__EventsGraphNavigator_Interaction_Entities_SourcePostFilterActionInfoType_EventsGraphNavigator_Interaction_EntitiesSubFilterSource', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 202, 10), )

    
    SubFilterSource = property(__SubFilterSource.value, __SubFilterSource.set, None, None)

    _ElementMap.update({
        __CommandLine.name() : __CommandLine,
        __SubFilterSource.name() : __SubFilterSource
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SourcePostFilterActionInfoType = SourcePostFilterActionInfoType
Namespace.addCategoryObject('typeBinding', 'SourcePostFilterActionInfoType', SourcePostFilterActionInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 247, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Folder uses Python identifier Folder
    __Folder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Folder'), 'Folder', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_3_EventsGraphNavigator_Interaction_EntitiesFolder', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 251, 20), )

    
    Folder = property(__Folder.value, __Folder.set, None, None)

    _ElementMap.update({
        __Folder.name() : __Folder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 258, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Regex uses Python identifier Regex
    __Regex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Regex'), 'Regex', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_4_EventsGraphNavigator_Interaction_EntitiesRegex', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 262, 20), )

    
    Regex = property(__Regex.value, __Regex.set, None, None)

    _ElementMap.update({
        __Regex.name() : __Regex
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 269, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Tag uses Python identifier Tag
    __Tag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tag'), 'Tag', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_5_EventsGraphNavigator_Interaction_EntitiesTag', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 273, 20), )

    
    Tag = property(__Tag.value, __Tag.set, None, None)

    _ElementMap.update({
        __Tag.name() : __Tag
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (BaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 280, 12)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Line uses Python identifier Line
    __Line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Line'), 'Line', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_6_EventsGraphNavigator_Interaction_EntitiesLine', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 284, 20), )

    
    Line = property(__Line.value, __Line.set, None, None)

    _ElementMap.update({
        __Line.name() : __Line
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelNodeInfoType with content type EMPTY
class TagModelNodeInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 369, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelNodeInfoType = TagModelNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelNodeInfoType', TagModelNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesEntityType with content type ELEMENT_ONLY
class LogMessagesEntityType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessagesEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 489, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}LogMessage uses Python identifier LogMessage
    __LogMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LogMessage'), 'LogMessage', '__EventsGraphNavigator_Interaction_Entities_LogMessagesEntityType_EventsGraphNavigator_Interaction_EntitiesLogMessage', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 494, 12), )

    
    LogMessage = property(__LogMessage.value, __LogMessage.set, None, None)

    _ElementMap.update({
        __LogMessage.name() : __LogMessage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogMessagesEntityType = LogMessagesEntityType
Namespace.addCategoryObject('typeBinding', 'LogMessagesEntityType', LogMessagesEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessageTagEntriesInfoType with content type ELEMENT_ONLY
class LogMessageTagEntriesInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessageTagEntriesInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessageTagEntriesInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 514, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TagEntry uses Python identifier TagEntry
    __TagEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagEntry'), 'TagEntry', '__EventsGraphNavigator_Interaction_Entities_LogMessageTagEntriesInfoType_EventsGraphNavigator_Interaction_EntitiesTagEntry', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 519, 12), )

    
    TagEntry = property(__TagEntry.value, __TagEntry.set, None, None)

    _ElementMap.update({
        __TagEntry.name() : __TagEntry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogMessageTagEntriesInfoType = LogMessageTagEntriesInfoType
Namespace.addCategoryObject('typeBinding', 'LogMessageTagEntriesInfoType', LogMessageTagEntriesInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessageTagEntryInfoType with content type ELEMENT_ONLY
class LogMessageTagEntryInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessageTagEntryInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessageTagEntryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 526, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstance uses Python identifier TagInstance
    __TagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), 'TagInstance', '__EventsGraphNavigator_Interaction_Entities_LogMessageTagEntryInfoType_EventsGraphNavigator_Interaction_EntitiesTagInstance', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 530, 10), )

    
    TagInstance = property(__TagInstance.value, __TagInstance.set, None, None)

    
    # Attribute Column uses Python identifier Column
    __Column = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Column'), 'Column', '__EventsGraphNavigator_Interaction_Entities_LogMessageTagEntryInfoType_Column', _module_typeBindings.int, required=True)
    __Column._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 532, 8)
    __Column._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 532, 8)
    
    Column = property(__Column.value, __Column.set, None, None)

    
    # Attribute Length uses Python identifier Length
    __Length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Length'), 'Length', '__EventsGraphNavigator_Interaction_Entities_LogMessageTagEntryInfoType_Length', _module_typeBindings.int, required=True)
    __Length._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 533, 8)
    __Length._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 533, 8)
    
    Length = property(__Length.value, __Length.set, None, None)

    _ElementMap.update({
        __TagInstance.name() : __TagInstance
    })
    _AttributeMap.update({
        __Column.name() : __Column,
        __Length.name() : __Length
    })
_module_typeBindings.LogMessageTagEntryInfoType = LogMessageTagEntryInfoType
Namespace.addCategoryObject('typeBinding', 'LogMessageTagEntryInfoType', LogMessageTagEntryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstancesEntityType with content type ELEMENT_ONLY
class TagInstancesEntityType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstancesEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstancesEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 545, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstance uses Python identifier TagInstance
    __TagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), 'TagInstance', '__EventsGraphNavigator_Interaction_Entities_TagInstancesEntityType_EventsGraphNavigator_Interaction_EntitiesTagInstance', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 550, 12), )

    
    TagInstance = property(__TagInstance.value, __TagInstance.set, None, None)

    _ElementMap.update({
        __TagInstance.name() : __TagInstance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstancesEntityType = TagInstancesEntityType
Namespace.addCategoryObject('typeBinding', 'TagInstancesEntityType', TagInstancesEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeysInfoType with content type ELEMENT_ONLY
class TagInstanceKeysInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeysInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceKeysInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 569, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Key uses Python identifier Key
    __Key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Key'), 'Key', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeysInfoType_EventsGraphNavigator_Interaction_EntitiesKey', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 574, 12), )

    
    Key = property(__Key.value, __Key.set, None, None)

    _ElementMap.update({
        __Key.name() : __Key
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstanceKeysInfoType = TagInstanceKeysInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceKeysInfoType', TagInstanceKeysInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyInfoType with content type ELEMENT_ONLY
class TagInstanceKeyInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceKeyInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 581, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ValuePattern uses Python identifier ValuePattern
    __ValuePattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuePattern'), 'ValuePattern', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyInfoType_EventsGraphNavigator_Interaction_EntitiesValuePattern', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 585, 10), )

    
    ValuePattern = property(__ValuePattern.value, __ValuePattern.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PlainValue uses Python identifier PlainValue
    __PlainValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlainValue'), 'PlainValue', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyInfoType_EventsGraphNavigator_Interaction_EntitiesPlainValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 587, 12), )

    
    PlainValue = property(__PlainValue.value, __PlainValue.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ComplexValue uses Python identifier ComplexValue
    __ComplexValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComplexValue'), 'ComplexValue', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyInfoType_EventsGraphNavigator_Interaction_EntitiesComplexValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 588, 12), )

    
    ComplexValue = property(__ComplexValue.value, __ComplexValue.set, None, None)

    
    # Attribute Order uses Python identifier Order
    __Order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Order'), 'Order', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyInfoType_Order', _module_typeBindings.int, required=True)
    __Order._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 591, 8)
    __Order._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 591, 8)
    
    Order = property(__Order.value, __Order.set, None, None)

    _ElementMap.update({
        __ValuePattern.name() : __ValuePattern,
        __PlainValue.name() : __PlainValue,
        __ComplexValue.name() : __ComplexValue
    })
    _AttributeMap.update({
        __Order.name() : __Order
    })
_module_typeBindings.TagInstanceKeyInfoType = TagInstanceKeyInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceKeyInfoType', TagInstanceKeyInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyValueInfoType with content type EMPTY
class TagInstanceKeyValueInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyValueInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceKeyValueInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 596, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstanceKeyValueInfoType = TagInstanceKeyValueInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceKeyValueInfoType', TagInstanceKeyValueInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceEntriesInfoType with content type ELEMENT_ONLY
class TagInstanceEntriesInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceEntriesInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceEntriesInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 633, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Entry uses Python identifier Entry
    __Entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Entry'), 'Entry', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntriesInfoType_EventsGraphNavigator_Interaction_EntitiesEntry', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 638, 12), )

    
    Entry = property(__Entry.value, __Entry.set, None, None)

    _ElementMap.update({
        __Entry.name() : __Entry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstanceEntriesInfoType = TagInstanceEntriesInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceEntriesInfoType', TagInstanceEntriesInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceEntryInfoType with content type ELEMENT_ONLY
class TagInstanceEntryInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceEntryInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceEntryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 645, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Message uses Python identifier Message
    __Message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Message'), 'Message', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntryInfoType_EventsGraphNavigator_Interaction_EntitiesMessage', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 649, 10), )

    
    Message = property(__Message.value, __Message.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Source'), 'Source', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntryInfoType_EventsGraphNavigator_Interaction_EntitiesSource', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 650, 10), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Line uses Python identifier Line
    __Line = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Line'), 'Line', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntryInfoType_Line', _module_typeBindings.int, required=True)
    __Line._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 652, 8)
    __Line._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 652, 8)
    
    Line = property(__Line.value, __Line.set, None, None)

    
    # Attribute Column uses Python identifier Column
    __Column = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Column'), 'Column', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntryInfoType_Column', _module_typeBindings.int, required=True)
    __Column._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 653, 8)
    __Column._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 653, 8)
    
    Column = property(__Column.value, __Column.set, None, None)

    
    # Attribute Length uses Python identifier Length
    __Length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Length'), 'Length', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntryInfoType_Length', _module_typeBindings.int, required=True)
    __Length._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 654, 8)
    __Length._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 654, 8)
    
    Length = property(__Length.value, __Length.set, None, None)

    _ElementMap.update({
        __Message.name() : __Message,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Line.name() : __Line,
        __Column.name() : __Column,
        __Length.name() : __Length
    })
_module_typeBindings.TagInstanceEntryInfoType = TagInstanceEntryInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceEntryInfoType', TagInstanceEntryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryInfoType with content type EMPTY
class QueryInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 692, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__EventsGraphNavigator_Interaction_Entities_QueryInfoType_Name', _module_typeBindings.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 695, 8)
    __Name._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 695, 8)
    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name
    })
_module_typeBindings.QueryInfoType = QueryInfoType
Namespace.addCategoryObject('typeBinding', 'QueryInfoType', QueryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType with content type EMPTY
class QueryNodeInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 787, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Attribute Invert uses Python identifier Invert
    __Invert = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Invert'), 'Invert', '__EventsGraphNavigator_Interaction_Entities_QueryNodeInfoType_Invert', _module_typeBindings.bool)
    __Invert._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 792, 8)
    __Invert._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 792, 8)
    
    Invert = property(__Invert.value, __Invert.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Invert.name() : __Invert
    })
_module_typeBindings.QueryNodeInfoType = QueryNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryNodeInfoType', QueryNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}NumberMatchingSpecInfoType with content type ELEMENT_ONLY
class NumberMatchingSpecInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}NumberMatchingSpecInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumberMatchingSpecInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1228, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_NumberMatchingSpecInfoType_EventsGraphNavigator_Interaction_EntitiesValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1233, 10), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NumberMatchingSpecInfoType = NumberMatchingSpecInfoType
Namespace.addCategoryObject('typeBinding', 'NumberMatchingSpecInfoType', NumberMatchingSpecInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}StringsList with content type ELEMENT_ONLY
class StringsList (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}StringsList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StringsList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1274, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Item uses Python identifier Item
    __Item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Item'), 'Item', '__EventsGraphNavigator_Interaction_Entities_StringsList_EventsGraphNavigator_Interaction_EntitiesItem', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1278, 10), )

    
    Item = property(__Item.value, __Item.set, None, None)

    _ElementMap.update({
        __Item.name() : __Item
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StringsList = StringsList
Namespace.addCategoryObject('typeBinding', 'StringsList', StringsList)


# Complex type {EventsGraphNavigator.Interaction.Entities}GuidsList with content type ELEMENT_ONLY
class GuidsList (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}GuidsList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GuidsList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1284, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Item uses Python identifier Item
    __Item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Item'), 'Item', '__EventsGraphNavigator_Interaction_Entities_GuidsList_EventsGraphNavigator_Interaction_EntitiesItem', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1288, 10), )

    
    Item = property(__Item.value, __Item.set, None, None)

    _ElementMap.update({
        __Item.name() : __Item
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GuidsList = GuidsList
Namespace.addCategoryObject('typeBinding', 'GuidsList', GuidsList)


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcCommandInfoType with content type ELEMENT_ONLY
class RpcCommandInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 29, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Call uses Python identifier Call
    __Call = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Call'), 'Call', '__EventsGraphNavigator_Interaction_Entities_RpcCommandInfoType_EventsGraphNavigator_Interaction_EntitiesCall', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 33, 10), )

    
    Call = property(__Call.value, __Call.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Result uses Python identifier Result
    __Result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Result'), 'Result', '__EventsGraphNavigator_Interaction_Entities_RpcCommandInfoType_EventsGraphNavigator_Interaction_EntitiesResult', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 34, 10), )

    
    Result = property(__Result.value, __Result.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Release uses Python identifier Release
    __Release = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Release'), 'Release', '__EventsGraphNavigator_Interaction_Entities_RpcCommandInfoType_EventsGraphNavigator_Interaction_EntitiesRelease', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 35, 10), )

    
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcCommandContentInfoType with content type EMPTY
class RpcCommandContentInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcCommandContentInfoType with content type EMPTY"""
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcSharedObjectKeyInfoType with content type ELEMENT_ONLY
class RpcSharedObjectKeyInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcSharedObjectKeyInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcSharedObjectKeyInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 86, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_RpcSharedObjectKeyInfoType_EventsGraphNavigator_Interaction_EntitiesValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 90, 10), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcSharedObjectKeyInfoType = RpcSharedObjectKeyInfoType
Namespace.addCategoryObject('typeBinding', 'RpcSharedObjectKeyInfoType', RpcSharedObjectKeyInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcMethodReferencInfoType with content type ELEMENT_ONLY
class RpcMethodReferencInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcMethodReferencInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcMethodReferencInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 96, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}GenericSignatureTypes uses Python identifier GenericSignatureTypes
    __GenericSignatureTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GenericSignatureTypes'), 'GenericSignatureTypes', '__EventsGraphNavigator_Interaction_Entities_RpcMethodReferencInfoType_EventsGraphNavigator_Interaction_EntitiesGenericSignatureTypes', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10), )

    
    GenericSignatureTypes = property(__GenericSignatureTypes.value, __GenericSignatureTypes.set, None, None)

    
    # Attribute DeclaringTypeName uses Python identifier DeclaringTypeName
    __DeclaringTypeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DeclaringTypeName'), 'DeclaringTypeName', '__EventsGraphNavigator_Interaction_Entities_RpcMethodReferencInfoType_DeclaringTypeName', _module_typeBindings.string, required=True)
    __DeclaringTypeName._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 102, 8)
    __DeclaringTypeName._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 102, 8)
    
    DeclaringTypeName = property(__DeclaringTypeName.value, __DeclaringTypeName.set, None, None)

    
    # Attribute MethodName uses Python identifier MethodName
    __MethodName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MethodName'), 'MethodName', '__EventsGraphNavigator_Interaction_Entities_RpcMethodReferencInfoType_MethodName', _module_typeBindings.string, required=True)
    __MethodName._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 103, 8)
    __MethodName._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 103, 8)
    
    MethodName = property(__MethodName.value, __MethodName.set, None, None)

    
    # Attribute MetadataToken uses Python identifier MetadataToken
    __MetadataToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MetadataToken'), 'MetadataToken', '__EventsGraphNavigator_Interaction_Entities_RpcMethodReferencInfoType_MetadataToken', _module_typeBindings.int, required=True)
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcMethodReferenceGenericTypesInfoType with content type ELEMENT_ONLY
class RpcMethodReferenceGenericTypesInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcMethodReferenceGenericTypesInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcMethodReferenceGenericTypesInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 109, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TypeName uses Python identifier TypeName
    __TypeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TypeName'), 'TypeName', '__EventsGraphNavigator_Interaction_Entities_RpcMethodReferenceGenericTypesInfoType_EventsGraphNavigator_Interaction_EntitiesTypeName', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10), )

    
    TypeName = property(__TypeName.value, __TypeName.set, None, None)

    _ElementMap.update({
        __TypeName.name() : __TypeName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcMethodReferenceGenericTypesInfoType = RpcMethodReferenceGenericTypesInfoType
Namespace.addCategoryObject('typeBinding', 'RpcMethodReferenceGenericTypesInfoType', RpcMethodReferenceGenericTypesInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcValueContainersListType with content type ELEMENT_ONLY
class RpcValueContainersListType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcValueContainersListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcValueContainersListType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 119, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_RpcValueContainersListType_EventsGraphNavigator_Interaction_EntitiesValue', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 123, 10), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcValueContainersListType = RpcValueContainersListType
Namespace.addCategoryObject('typeBinding', 'RpcValueContainersListType', RpcValueContainersListType)


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcValueContainerType with content type ELEMENT_ONLY
class RpcValueContainerType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcValueContainerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcValueContainerType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 129, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Instance uses Python identifier Instance
    __Instance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Instance'), 'Instance', '__EventsGraphNavigator_Interaction_Entities_RpcValueContainerType_EventsGraphNavigator_Interaction_EntitiesInstance', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 134, 12), )

    
    Instance = property(__Instance.value, __Instance.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}String uses Python identifier String
    __String = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'String'), 'String', '__EventsGraphNavigator_Interaction_Entities_RpcValueContainerType_EventsGraphNavigator_Interaction_EntitiesString', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 135, 12), )

    
    String = property(__String.value, __String.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Int32 uses Python identifier Int32
    __Int32 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Int32'), 'Int32', '__EventsGraphNavigator_Interaction_Entities_RpcValueContainerType_EventsGraphNavigator_Interaction_EntitiesInt32', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 136, 12), )

    
    Int32 = property(__Int32.value, __Int32.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Boolean uses Python identifier Boolean
    __Boolean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Boolean'), 'Boolean', '__EventsGraphNavigator_Interaction_Entities_RpcValueContainerType_EventsGraphNavigator_Interaction_EntitiesBoolean', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 137, 12), )

    
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcExceptionDescriptionInfoType with content type ELEMENT_ONLY
class RpcExceptionDescriptionInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcExceptionDescriptionInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcExceptionDescriptionInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 144, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Message uses Python identifier Message
    __Message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Message'), 'Message', '__EventsGraphNavigator_Interaction_Entities_RpcExceptionDescriptionInfoType_EventsGraphNavigator_Interaction_EntitiesMessage', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 148, 10), )

    
    Message = property(__Message.value, __Message.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}StackTrace uses Python identifier StackTrace
    __StackTrace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StackTrace'), 'StackTrace', '__EventsGraphNavigator_Interaction_Entities_RpcExceptionDescriptionInfoType_EventsGraphNavigator_Interaction_EntitiesStackTrace', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 149, 10), )

    
    StackTrace = property(__StackTrace.value, __StackTrace.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}InnerException uses Python identifier InnerException
    __InnerException = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InnerException'), 'InnerException', '__EventsGraphNavigator_Interaction_Entities_RpcExceptionDescriptionInfoType_EventsGraphNavigator_Interaction_EntitiesInnerException', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10), )

    
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcRemoteObjectReferenceInfoType with content type ELEMENT_ONLY
class RpcRemoteObjectReferenceInfoType (RpcBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcRemoteObjectReferenceInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcRemoteObjectReferenceInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 156, 2)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}RemoteInstanceId uses Python identifier RemoteInstanceId
    __RemoteInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId'), 'RemoteInstanceId', '__EventsGraphNavigator_Interaction_Entities_RpcRemoteObjectReferenceInfoType_EventsGraphNavigator_Interaction_EntitiesRemoteInstanceId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 160, 10), )

    
    RemoteInstanceId = property(__RemoteInstanceId.value, __RemoteInstanceId.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}InterfaceTypes uses Python identifier InterfaceTypes
    __InterfaceTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterfaceTypes'), 'InterfaceTypes', '__EventsGraphNavigator_Interaction_Entities_RpcRemoteObjectReferenceInfoType_EventsGraphNavigator_Interaction_EntitiesInterfaceTypes', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 161, 10), )

    
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
class CTD_ANON_7 (RpcBaseType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 162, 12)
    _ElementMap = RpcBaseType._ElementMap.copy()
    _AttributeMap = RpcBaseType._AttributeMap.copy()
    # Base type is RpcBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Type'), 'Type', '__EventsGraphNavigator_Interaction_Entities_CTD_ANON_7_EventsGraphNavigator_Interaction_EntitiesType', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 166, 20), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType with content type EMPTY
class NamedEntityBaseType (IdentifiedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NamedEntityBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 70, 2)
    _ElementMap = IdentifiedEntityBaseType._ElementMap.copy()
    _AttributeMap = IdentifiedEntityBaseType._AttributeMap.copy()
    # Base type is IdentifiedEntityBaseType
    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__EventsGraphNavigator_Interaction_Entities_NamedEntityBaseType_Name', _module_typeBindings.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 73, 8)
    __Name._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 73, 8)
    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name
    })
_module_typeBindings.NamedEntityBaseType = NamedEntityBaseType
Namespace.addCategoryObject('typeBinding', 'NamedEntityBaseType', NamedEntityBaseType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType with content type ELEMENT_ONLY
class TagModelUnaryNodeInfoType (TagModelNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelUnaryNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 378, 2)
    _ElementMap = TagModelNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelNodeInfoType._AttributeMap.copy()
    # Base type is TagModelNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Pattern uses Python identifier Pattern
    __Pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pattern'), 'Pattern', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesPattern', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12), )

    
    Pattern = property(__Pattern.value, __Pattern.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Alternatives uses Python identifier Alternatives
    __Alternatives = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Alternatives'), 'Alternatives', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAlternatives', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12), )

    
    Alternatives = property(__Alternatives.value, __Alternatives.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Sequence uses Python identifier Sequence
    __Sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sequence'), 'Sequence', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSequence', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12), )

    
    Sequence = property(__Sequence.value, __Sequence.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Number uses Python identifier Number
    __Number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Number'), 'Number', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesNumber', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12), )

    
    Number = property(__Number.value, __Number.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Contains uses Python identifier Contains
    __Contains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contains'), 'Contains', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12), )

    
    Contains = property(__Contains.value, __Contains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}NotContains uses Python identifier NotContains
    __NotContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotContains'), 'NotContains', '__EventsGraphNavigator_Interaction_Entities_TagModelUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesNotContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12), )

    
    NotContains = property(__NotContains.value, __NotContains.set, None, None)

    _ElementMap.update({
        __Text.name() : __Text,
        __Pattern.name() : __Pattern,
        __Alternatives.name() : __Alternatives,
        __Sequence.name() : __Sequence,
        __Number.name() : __Number,
        __Contains.name() : __Contains,
        __NotContains.name() : __NotContains
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelUnaryNodeInfoType = TagModelUnaryNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelUnaryNodeInfoType', TagModelUnaryNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType with content type ELEMENT_ONLY
class TagModelGroupNodeInfoType (TagModelNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelGroupNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 397, 2)
    _ElementMap = TagModelNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelNodeInfoType._AttributeMap.copy()
    # Base type is TagModelNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 403, 12), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Pattern uses Python identifier Pattern
    __Pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pattern'), 'Pattern', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesPattern', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 404, 12), )

    
    Pattern = property(__Pattern.value, __Pattern.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Alternatives uses Python identifier Alternatives
    __Alternatives = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Alternatives'), 'Alternatives', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAlternatives', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 405, 12), )

    
    Alternatives = property(__Alternatives.value, __Alternatives.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Sequence uses Python identifier Sequence
    __Sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sequence'), 'Sequence', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSequence', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 406, 12), )

    
    Sequence = property(__Sequence.value, __Sequence.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Number uses Python identifier Number
    __Number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Number'), 'Number', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesNumber', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 407, 12), )

    
    Number = property(__Number.value, __Number.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Contains uses Python identifier Contains
    __Contains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contains'), 'Contains', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 408, 12), )

    
    Contains = property(__Contains.value, __Contains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}NotContains uses Python identifier NotContains
    __NotContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NotContains'), 'NotContains', '__EventsGraphNavigator_Interaction_Entities_TagModelGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesNotContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 409, 12), )

    
    NotContains = property(__NotContains.value, __NotContains.set, None, None)

    _ElementMap.update({
        __Text.name() : __Text,
        __Pattern.name() : __Pattern,
        __Alternatives.name() : __Alternatives,
        __Sequence.name() : __Sequence,
        __Number.name() : __Number,
        __Contains.name() : __Contains,
        __NotContains.name() : __NotContains
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelGroupNodeInfoType = TagModelGroupNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelGroupNodeInfoType', TagModelGroupNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelTextNodeInfoType with content type EMPTY
class TagModelTextNodeInfoType (TagModelNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelTextNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelTextNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 428, 2)
    _ElementMap = TagModelNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelNodeInfoType._AttributeMap.copy()
    # Base type is TagModelNodeInfoType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_TagModelTextNodeInfoType_Value', _module_typeBindings.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 431, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 431, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute MatchCase uses Python identifier MatchCase
    __MatchCase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MatchCase'), 'MatchCase', '__EventsGraphNavigator_Interaction_Entities_TagModelTextNodeInfoType_MatchCase', _module_typeBindings.bool, required=True)
    __MatchCase._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 432, 8)
    __MatchCase._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 432, 8)
    
    MatchCase = property(__MatchCase.value, __MatchCase.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value,
        __MatchCase.name() : __MatchCase
    })
_module_typeBindings.TagModelTextNodeInfoType = TagModelTextNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelTextNodeInfoType', TagModelTextNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelPatternNodeInfoType with content type EMPTY
class TagModelPatternNodeInfoType (TagModelNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelPatternNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelPatternNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 437, 2)
    _ElementMap = TagModelNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelNodeInfoType._AttributeMap.copy()
    # Base type is TagModelNodeInfoType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__EventsGraphNavigator_Interaction_Entities_TagModelPatternNodeInfoType_Name', _module_typeBindings.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 440, 8)
    __Name._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 440, 8)
    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name
    })
_module_typeBindings.TagModelPatternNodeInfoType = TagModelPatternNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelPatternNodeInfoType', TagModelPatternNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessageEntityType with content type ELEMENT_ONLY
class LogMessageEntityType (IdentifiedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessageEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessageEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 501, 2)
    _ElementMap = IdentifiedEntityBaseType._ElementMap.copy()
    _AttributeMap = IdentifiedEntityBaseType._AttributeMap.copy()
    # Base type is IdentifiedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Source'), 'Source', '__EventsGraphNavigator_Interaction_Entities_LogMessageEntityType_EventsGraphNavigator_Interaction_EntitiesSource', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 505, 10), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_LogMessageEntityType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 506, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagEntries uses Python identifier TagEntries
    __TagEntries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagEntries'), 'TagEntries', '__EventsGraphNavigator_Interaction_Entities_LogMessageEntityType_EventsGraphNavigator_Interaction_EntitiesTagEntries', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 507, 10), )

    
    TagEntries = property(__TagEntries.value, __TagEntries.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Line uses Python identifier Line
    __Line = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Line'), 'Line', '__EventsGraphNavigator_Interaction_Entities_LogMessageEntityType_Line', _module_typeBindings.int, required=True)
    __Line._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 509, 8)
    __Line._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 509, 8)
    
    Line = property(__Line.value, __Line.set, None, None)

    _ElementMap.update({
        __Source.name() : __Source,
        __Text.name() : __Text,
        __TagEntries.name() : __TagEntries
    })
    _AttributeMap.update({
        __Line.name() : __Line
    })
_module_typeBindings.LogMessageEntityType = LogMessageEntityType
Namespace.addCategoryObject('typeBinding', 'LogMessageEntityType', LogMessageEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceEntityType with content type ELEMENT_ONLY
class TagInstanceEntityType (IdentifiedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 557, 2)
    _ElementMap = IdentifiedEntityBaseType._ElementMap.copy()
    _AttributeMap = IdentifiedEntityBaseType._AttributeMap.copy()
    # Base type is IdentifiedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TagPattern uses Python identifier TagPattern
    __TagPattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagPattern'), 'TagPattern', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntityType_EventsGraphNavigator_Interaction_EntitiesTagPattern', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 561, 10), )

    
    TagPattern = property(__TagPattern.value, __TagPattern.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Keys uses Python identifier Keys
    __Keys = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Keys'), 'Keys', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntityType_EventsGraphNavigator_Interaction_EntitiesKeys', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 562, 10), )

    
    Keys = property(__Keys.value, __Keys.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Entries uses Python identifier Entries
    __Entries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Entries'), 'Entries', '__EventsGraphNavigator_Interaction_Entities_TagInstanceEntityType_EventsGraphNavigator_Interaction_EntitiesEntries', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 563, 10), )

    
    Entries = property(__Entries.value, __Entries.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    _ElementMap.update({
        __TagPattern.name() : __TagPattern,
        __Keys.name() : __Keys,
        __Entries.name() : __Entries
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstanceEntityType = TagInstanceEntityType
Namespace.addCategoryObject('typeBinding', 'TagInstanceEntityType', TagInstanceEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyPlainValueInfoType with content type ELEMENT_ONLY
class TagInstanceKeyPlainValueInfoType (TagInstanceKeyValueInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyPlainValueInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceKeyPlainValueInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 605, 2)
    _ElementMap = TagInstanceKeyValueInfoType._ElementMap.copy()
    _AttributeMap = TagInstanceKeyValueInfoType._AttributeMap.copy()
    # Base type is TagInstanceKeyValueInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}String uses Python identifier String
    __String = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'String'), 'String', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyPlainValueInfoType_EventsGraphNavigator_Interaction_EntitiesString', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 610, 12), )

    
    String = property(__String.value, __String.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Integer uses Python identifier Integer
    __Integer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Integer'), 'Integer', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyPlainValueInfoType_EventsGraphNavigator_Interaction_EntitiesInteger', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 611, 12), )

    
    Integer = property(__Integer.value, __Integer.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DateTime'), 'DateTime', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyPlainValueInfoType_EventsGraphNavigator_Interaction_EntitiesDateTime', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 612, 12), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Decimal uses Python identifier Decimal
    __Decimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Decimal'), 'Decimal', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyPlainValueInfoType_EventsGraphNavigator_Interaction_EntitiesDecimal', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 613, 12), )

    
    Decimal = property(__Decimal.value, __Decimal.set, None, None)

    
    # Attribute ValueType uses Python identifier ValueType
    __ValueType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ValueType'), 'ValueType', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyPlainValueInfoType_ValueType', _module_typeBindings.TagInstanceKeyValueType, required=True)
    __ValueType._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 616, 8)
    __ValueType._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 616, 8)
    
    ValueType = property(__ValueType.value, __ValueType.set, None, None)

    _ElementMap.update({
        __String.name() : __String,
        __Integer.name() : __Integer,
        __DateTime.name() : __DateTime,
        __Decimal.name() : __Decimal
    })
    _AttributeMap.update({
        __ValueType.name() : __ValueType
    })
_module_typeBindings.TagInstanceKeyPlainValueInfoType = TagInstanceKeyPlainValueInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceKeyPlainValueInfoType', TagInstanceKeyPlainValueInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyComplexValueInfoType with content type ELEMENT_ONLY
class TagInstanceKeyComplexValueInfoType (TagInstanceKeyValueInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstanceKeyComplexValueInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstanceKeyComplexValueInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 621, 2)
    _ElementMap = TagInstanceKeyValueInfoType._ElementMap.copy()
    _AttributeMap = TagInstanceKeyValueInfoType._AttributeMap.copy()
    # Base type is TagInstanceKeyValueInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstance uses Python identifier TagInstance
    __TagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), 'TagInstance', '__EventsGraphNavigator_Interaction_Entities_TagInstanceKeyComplexValueInfoType_EventsGraphNavigator_Interaction_EntitiesTagInstance', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 626, 12), )

    
    TagInstance = property(__TagInstance.value, __TagInstance.set, None, None)

    _ElementMap.update({
        __TagInstance.name() : __TagInstance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstanceKeyComplexValueInfoType = TagInstanceKeyComplexValueInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstanceKeyComplexValueInfoType', TagInstanceKeyComplexValueInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}StringMatchingSpecInfoType with content type ELEMENT_ONLY
class StringMatchingSpecInfoType (BaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}StringMatchingSpecInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StringMatchingSpecInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 663, 2)
    _ElementMap = BaseType._ElementMap.copy()
    _AttributeMap = BaseType._AttributeMap.copy()
    # Base type is BaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Pattern uses Python identifier Pattern
    __Pattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pattern'), 'Pattern', '__EventsGraphNavigator_Interaction_Entities_StringMatchingSpecInfoType_EventsGraphNavigator_Interaction_EntitiesPattern', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 667, 10), )

    
    Pattern = property(__Pattern.value, __Pattern.set, None, None)

    
    # Attribute MatchWholeWord uses Python identifier MatchWholeWord
    __MatchWholeWord = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MatchWholeWord'), 'MatchWholeWord', '__EventsGraphNavigator_Interaction_Entities_StringMatchingSpecInfoType_MatchWholeWord', _module_typeBindings.bool, required=True)
    __MatchWholeWord._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 669, 8)
    __MatchWholeWord._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 669, 8)
    
    MatchWholeWord = property(__MatchWholeWord.value, __MatchWholeWord.set, None, None)

    
    # Attribute MatchCase uses Python identifier MatchCase
    __MatchCase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MatchCase'), 'MatchCase', '__EventsGraphNavigator_Interaction_Entities_StringMatchingSpecInfoType_MatchCase', _module_typeBindings.bool, required=True)
    __MatchCase._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 670, 8)
    __MatchCase._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 670, 8)
    
    MatchCase = property(__MatchCase.value, __MatchCase.set, None, None)

    
    # Attribute MatchingMode uses Python identifier MatchingMode
    __MatchingMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MatchingMode'), 'MatchingMode', '__EventsGraphNavigator_Interaction_Entities_StringMatchingSpecInfoType_MatchingMode', _module_typeBindings.StringMatchingModeType, required=True)
    __MatchingMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 671, 8)
    __MatchingMode._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 671, 8)
    
    MatchingMode = property(__MatchingMode.value, __MatchingMode.set, None, None)

    _ElementMap.update({
        __Pattern.name() : __Pattern
    })
    _AttributeMap.update({
        __MatchWholeWord.name() : __MatchWholeWord,
        __MatchCase.name() : __MatchCase,
        __MatchingMode.name() : __MatchingMode
    })
_module_typeBindings.StringMatchingSpecInfoType = StringMatchingSpecInfoType
Namespace.addCategoryObject('typeBinding', 'StringMatchingSpecInfoType', StringMatchingSpecInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesQueryInfoType with content type EMPTY
class LogMessagesQueryInfoType (QueryInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesQueryInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessagesQueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 700, 2)
    _ElementMap = QueryInfoType._ElementMap.copy()
    _AttributeMap = QueryInfoType._AttributeMap.copy()
    # Base type is QueryInfoType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}QueryInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogMessagesQueryInfoType = LogMessagesQueryInfoType
Namespace.addCategoryObject('typeBinding', 'LogMessagesQueryInfoType', LogMessagesQueryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstancesQueryInfoType with content type EMPTY
class TagInstancesQueryInfoType (QueryInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstancesQueryInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstancesQueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 707, 2)
    _ElementMap = QueryInfoType._ElementMap.copy()
    _AttributeMap = QueryInfoType._AttributeMap.copy()
    # Base type is QueryInfoType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}QueryInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstancesQueryInfoType = TagInstancesQueryInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstancesQueryInfoType', TagInstancesQueryInfoType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (IdentifiedEntityBaseType):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 723, 12)
    _ElementMap = IdentifiedEntityBaseType._ElementMap.copy()
    _AttributeMap = IdentifiedEntityBaseType._AttributeMap.copy()
    # Base type is IdentifiedEntityBaseType
    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageNodeInfoType with content type EMPTY
class QueryLogMessageNodeInfoType (QueryNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 801, 2)
    _ElementMap = QueryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryNodeInfoType._AttributeMap.copy()
    # Base type is QueryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageNodeInfoType = QueryLogMessageNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageNodeInfoType', QueryLogMessageNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceNodeInfoType with content type EMPTY
class QueryTagInstanceNodeInfoType (QueryNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 949, 2)
    _ElementMap = QueryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryNodeInfoType._AttributeMap.copy()
    # Base type is QueryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceNodeInfoType = QueryTagInstanceNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceNodeInfoType', QueryTagInstanceNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyNodeInfoType with content type EMPTY
class QueryTagInstanceKeyNodeInfoType (QueryNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1082, 2)
    _ElementMap = QueryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryNodeInfoType._AttributeMap.copy()
    # Base type is QueryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyNodeInfoType = QueryTagInstanceKeyNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyNodeInfoType', QueryTagInstanceKeyNodeInfoType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (IdentifiedEntityBaseType):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1289, 12)
    _ElementMap = IdentifiedEntityBaseType._ElementMap.copy()
    _AttributeMap = IdentifiedEntityBaseType._AttributeMap.copy()
    # Base type is IdentifiedEntityBaseType
    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcCallCommandInfoType with content type ELEMENT_ONLY
class RpcCallCommandInfoType (RpcCommandContentInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcCallCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcCallCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 50, 2)
    _ElementMap = RpcCommandContentInfoType._ElementMap.copy()
    _AttributeMap = RpcCommandContentInfoType._AttributeMap.copy()
    # Base type is RpcCommandContentInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}RemoteInstanceId uses Python identifier RemoteInstanceId
    __RemoteInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId'), 'RemoteInstanceId', '__EventsGraphNavigator_Interaction_Entities_RpcCallCommandInfoType_EventsGraphNavigator_Interaction_EntitiesRemoteInstanceId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 54, 10), )

    
    RemoteInstanceId = property(__RemoteInstanceId.value, __RemoteInstanceId.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}MethodId uses Python identifier MethodId
    __MethodId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MethodId'), 'MethodId', '__EventsGraphNavigator_Interaction_Entities_RpcCallCommandInfoType_EventsGraphNavigator_Interaction_EntitiesMethodId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 55, 10), )

    
    MethodId = property(__MethodId.value, __MethodId.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Arguments uses Python identifier Arguments
    __Arguments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Arguments'), 'Arguments', '__EventsGraphNavigator_Interaction_Entities_RpcCallCommandInfoType_EventsGraphNavigator_Interaction_EntitiesArguments', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 56, 10), )

    
    Arguments = property(__Arguments.value, __Arguments.set, None, None)

    
    # Attribute CallId uses Python identifier CallId
    __CallId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CallId'), 'CallId', '__EventsGraphNavigator_Interaction_Entities_RpcCallCommandInfoType_CallId', _module_typeBindings.int, required=True)
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcResultCommandInfoType with content type ELEMENT_ONLY
class RpcResultCommandInfoType (RpcCommandContentInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcResultCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcResultCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 63, 2)
    _ElementMap = RpcCommandContentInfoType._ElementMap.copy()
    _AttributeMap = RpcCommandContentInfoType._AttributeMap.copy()
    # Base type is RpcCommandContentInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ReturnValue uses Python identifier ReturnValue
    __ReturnValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReturnValue'), 'ReturnValue', '__EventsGraphNavigator_Interaction_Entities_RpcResultCommandInfoType_EventsGraphNavigator_Interaction_EntitiesReturnValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 67, 10), )

    
    ReturnValue = property(__ReturnValue.value, __ReturnValue.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}OutArguments uses Python identifier OutArguments
    __OutArguments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutArguments'), 'OutArguments', '__EventsGraphNavigator_Interaction_Entities_RpcResultCommandInfoType_EventsGraphNavigator_Interaction_EntitiesOutArguments', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 68, 10), )

    
    OutArguments = property(__OutArguments.value, __OutArguments.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Exception'), 'Exception', '__EventsGraphNavigator_Interaction_Entities_RpcResultCommandInfoType_EventsGraphNavigator_Interaction_EntitiesException', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 69, 10), )

    
    Exception = property(__Exception.value, __Exception.set, None, None)

    
    # Attribute CallId uses Python identifier CallId
    __CallId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CallId'), 'CallId', '__EventsGraphNavigator_Interaction_Entities_RpcResultCommandInfoType_CallId', _module_typeBindings.int, required=True)
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


# Complex type {EventsGraphNavigator.Interaction.Entities}RpcReleaseCommandInfoType with content type ELEMENT_ONLY
class RpcReleaseCommandInfoType (RpcCommandContentInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}RpcReleaseCommandInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RpcReleaseCommandInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 76, 2)
    _ElementMap = RpcCommandContentInfoType._ElementMap.copy()
    _AttributeMap = RpcCommandContentInfoType._AttributeMap.copy()
    # Base type is RpcCommandContentInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}RemoteInstanceId uses Python identifier RemoteInstanceId
    __RemoteInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId'), 'RemoteInstanceId', '__EventsGraphNavigator_Interaction_Entities_RpcReleaseCommandInfoType_EventsGraphNavigator_Interaction_EntitiesRemoteInstanceId', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 80, 10), )

    
    RemoteInstanceId = property(__RemoteInstanceId.value, __RemoteInstanceId.set, None, None)

    _ElementMap.update({
        __RemoteInstanceId.name() : __RemoteInstanceId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RpcReleaseCommandInfoType = RpcReleaseCommandInfoType
Namespace.addCategoryObject('typeBinding', 'RpcReleaseCommandInfoType', RpcReleaseCommandInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}ReferenceEntityType with content type EMPTY
class ReferenceEntityType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}ReferenceEntityType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 78, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceEntityType = ReferenceEntityType
Namespace.addCategoryObject('typeBinding', 'ReferenceEntityType', ReferenceEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}SourcesItemBaseType with content type ELEMENT_ONLY
class SourcesItemBaseType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourcesItemBaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourcesItemBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 94, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__EventsGraphNavigator_Interaction_Entities_SourcesItemBaseType_EventsGraphNavigator_Interaction_EntitiesDescription', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 98, 10), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __Description.name() : __Description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SourcesItemBaseType = SourcesItemBaseType
Namespace.addCategoryObject('typeBinding', 'SourcesItemBaseType', SourcesItemBaseType)


# Complex type {EventsGraphNavigator.Interaction.Entities}SourceInfoType with content type ELEMENT_ONLY
class SourceInfoType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourceInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourceInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 157, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ControlOptions uses Python identifier ControlOptions
    __ControlOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlOptions'), 'ControlOptions', '__EventsGraphNavigator_Interaction_Entities_SourceInfoType_EventsGraphNavigator_Interaction_EntitiesControlOptions', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 161, 10), )

    
    ControlOptions = property(__ControlOptions.value, __ControlOptions.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}FilterOptions uses Python identifier FilterOptions
    __FilterOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FilterOptions'), 'FilterOptions', '__EventsGraphNavigator_Interaction_Entities_SourceInfoType_EventsGraphNavigator_Interaction_EntitiesFilterOptions', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 162, 10), )

    
    FilterOptions = property(__FilterOptions.value, __FilterOptions.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PostFilterAction uses Python identifier PostFilterAction
    __PostFilterAction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostFilterAction'), 'PostFilterAction', '__EventsGraphNavigator_Interaction_Entities_SourceInfoType_EventsGraphNavigator_Interaction_EntitiesPostFilterAction', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 163, 10), )

    
    PostFilterAction = property(__PostFilterAction.value, __PostFilterAction.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    
    # Attribute IsFile uses Python identifier IsFile
    __IsFile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsFile'), 'IsFile', '__EventsGraphNavigator_Interaction_Entities_SourceInfoType_IsFile', _module_typeBindings.bool, required=True)
    __IsFile._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 165, 8)
    __IsFile._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 165, 8)
    
    IsFile = property(__IsFile.value, __IsFile.set, None, None)

    
    # Attribute IsObsolete uses Python identifier IsObsolete
    __IsObsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsObsolete'), 'IsObsolete', '__EventsGraphNavigator_Interaction_Entities_SourceInfoType_IsObsolete', _module_typeBindings.bool, required=True)
    __IsObsolete._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 166, 8)
    __IsObsolete._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 166, 8)
    
    IsObsolete = property(__IsObsolete.value, __IsObsolete.set, None, None)

    _ElementMap.update({
        __ControlOptions.name() : __ControlOptions,
        __FilterOptions.name() : __FilterOptions,
        __PostFilterAction.name() : __PostFilterAction
    })
    _AttributeMap.update({
        __IsFile.name() : __IsFile,
        __IsObsolete.name() : __IsObsolete
    })
_module_typeBindings.SourceInfoType = SourceInfoType
Namespace.addCategoryObject('typeBinding', 'SourceInfoType', SourceInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}PatternsItemBaseType with content type ELEMENT_ONLY
class PatternsItemBaseType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}PatternsItemBaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PatternsItemBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 232, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__EventsGraphNavigator_Interaction_Entities_PatternsItemBaseType_EventsGraphNavigator_Interaction_EntitiesDescription', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __Description.name() : __Description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PatternsItemBaseType = PatternsItemBaseType
Namespace.addCategoryObject('typeBinding', 'PatternsItemBaseType', PatternsItemBaseType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagPatternInfoType with content type ELEMENT_ONLY
class TagPatternInfoType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagPatternInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagPatternInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 327, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__EventsGraphNavigator_Interaction_Entities_TagPatternInfoType_EventsGraphNavigator_Interaction_EntitiesModel', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    
    # Attribute MatchingMode uses Python identifier MatchingMode
    __MatchingMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MatchingMode'), 'MatchingMode', '__EventsGraphNavigator_Interaction_Entities_TagPatternInfoType_MatchingMode', _module_typeBindings.TagMatchingModeType, required=True)
    __MatchingMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 333, 8)
    __MatchingMode._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 333, 8)
    
    MatchingMode = property(__MatchingMode.value, __MatchingMode.set, None, None)

    
    # Attribute OrderSpecific uses Python identifier OrderSpecific
    __OrderSpecific = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'OrderSpecific'), 'OrderSpecific', '__EventsGraphNavigator_Interaction_Entities_TagPatternInfoType_OrderSpecific', _module_typeBindings.bool, required=True)
    __OrderSpecific._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 334, 8)
    __OrderSpecific._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 334, 8)
    
    OrderSpecific = property(__OrderSpecific.value, __OrderSpecific.set, None, None)

    _ElementMap.update({
        __Model.name() : __Model
    })
    _AttributeMap.update({
        __MatchingMode.name() : __MatchingMode,
        __OrderSpecific.name() : __OrderSpecific
    })
_module_typeBindings.TagPatternInfoType = TagPatternInfoType
Namespace.addCategoryObject('typeBinding', 'TagPatternInfoType', TagPatternInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LinePatternInfoType with content type ELEMENT_ONLY
class LinePatternInfoType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LinePatternInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinePatternInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 339, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__EventsGraphNavigator_Interaction_Entities_LinePatternInfoType_EventsGraphNavigator_Interaction_EntitiesModel', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __Model.name() : __Model
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LinePatternInfoType = LinePatternInfoType
Namespace.addCategoryObject('typeBinding', 'LinePatternInfoType', LinePatternInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (TagModelUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 352, 8)
    _ElementMap = TagModelUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelUnaryNodeInfoType._AttributeMap.copy()
    # Base type is TagModelUnaryNodeInfoType
    
    # Element Text ({EventsGraphNavigator.Interaction.Entities}Text) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Pattern ({EventsGraphNavigator.Interaction.Entities}Pattern) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Alternatives ({EventsGraphNavigator.Interaction.Entities}Alternatives) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Sequence ({EventsGraphNavigator.Interaction.Entities}Sequence) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Number ({EventsGraphNavigator.Interaction.Entities}Number) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Contains ({EventsGraphNavigator.Interaction.Entities}Contains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element NotContains ({EventsGraphNavigator.Interaction.Entities}NotContains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelAlternativesNodeInfoType with content type ELEMENT_ONLY
class TagModelAlternativesNodeInfoType (TagModelGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelAlternativesNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelAlternativesNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 445, 2)
    _ElementMap = TagModelGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelGroupNodeInfoType._AttributeMap.copy()
    # Base type is TagModelGroupNodeInfoType
    
    # Element Text ({EventsGraphNavigator.Interaction.Entities}Text) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Pattern ({EventsGraphNavigator.Interaction.Entities}Pattern) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Alternatives ({EventsGraphNavigator.Interaction.Entities}Alternatives) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Sequence ({EventsGraphNavigator.Interaction.Entities}Sequence) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Number ({EventsGraphNavigator.Interaction.Entities}Number) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Contains ({EventsGraphNavigator.Interaction.Entities}Contains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element NotContains ({EventsGraphNavigator.Interaction.Entities}NotContains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelAlternativesNodeInfoType = TagModelAlternativesNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelAlternativesNodeInfoType', TagModelAlternativesNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelSequenceNodeInfoType with content type ELEMENT_ONLY
class TagModelSequenceNodeInfoType (TagModelGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelSequenceNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelSequenceNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 452, 2)
    _ElementMap = TagModelGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelGroupNodeInfoType._AttributeMap.copy()
    # Base type is TagModelGroupNodeInfoType
    
    # Element Text ({EventsGraphNavigator.Interaction.Entities}Text) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Pattern ({EventsGraphNavigator.Interaction.Entities}Pattern) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Alternatives ({EventsGraphNavigator.Interaction.Entities}Alternatives) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Sequence ({EventsGraphNavigator.Interaction.Entities}Sequence) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Number ({EventsGraphNavigator.Interaction.Entities}Number) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element Contains ({EventsGraphNavigator.Interaction.Entities}Contains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    
    # Element NotContains ({EventsGraphNavigator.Interaction.Entities}NotContains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelGroupNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelSequenceNodeInfoType = TagModelSequenceNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelSequenceNodeInfoType', TagModelSequenceNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelNumberNodeInfoType with content type ELEMENT_ONLY
class TagModelNumberNodeInfoType (TagModelUnaryNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelNumberNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelNumberNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 459, 2)
    _ElementMap = TagModelUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelUnaryNodeInfoType._AttributeMap.copy()
    # Base type is TagModelUnaryNodeInfoType
    
    # Element Text ({EventsGraphNavigator.Interaction.Entities}Text) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Pattern ({EventsGraphNavigator.Interaction.Entities}Pattern) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Alternatives ({EventsGraphNavigator.Interaction.Entities}Alternatives) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Sequence ({EventsGraphNavigator.Interaction.Entities}Sequence) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Number ({EventsGraphNavigator.Interaction.Entities}Number) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Contains ({EventsGraphNavigator.Interaction.Entities}Contains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element NotContains ({EventsGraphNavigator.Interaction.Entities}NotContains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Attribute From uses Python identifier From
    __From = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'From'), 'From', '__EventsGraphNavigator_Interaction_Entities_TagModelNumberNodeInfoType_From', _module_typeBindings.int)
    __From._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 462, 8)
    __From._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 462, 8)
    
    From = property(__From.value, __From.set, None, None)

    
    # Attribute To uses Python identifier To
    __To = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'To'), 'To', '__EventsGraphNavigator_Interaction_Entities_TagModelNumberNodeInfoType_To', _module_typeBindings.int)
    __To._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 463, 8)
    __To._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 463, 8)
    
    To = property(__To.value, __To.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __From.name() : __From,
        __To.name() : __To
    })
_module_typeBindings.TagModelNumberNodeInfoType = TagModelNumberNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelNumberNodeInfoType', TagModelNumberNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelContainsNodeInfoType with content type ELEMENT_ONLY
class TagModelContainsNodeInfoType (TagModelUnaryNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 468, 2)
    _ElementMap = TagModelUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelUnaryNodeInfoType._AttributeMap.copy()
    # Base type is TagModelUnaryNodeInfoType
    
    # Element Text ({EventsGraphNavigator.Interaction.Entities}Text) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Pattern ({EventsGraphNavigator.Interaction.Entities}Pattern) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Alternatives ({EventsGraphNavigator.Interaction.Entities}Alternatives) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Sequence ({EventsGraphNavigator.Interaction.Entities}Sequence) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Number ({EventsGraphNavigator.Interaction.Entities}Number) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Contains ({EventsGraphNavigator.Interaction.Entities}Contains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element NotContains ({EventsGraphNavigator.Interaction.Entities}NotContains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelContainsNodeInfoType = TagModelContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelContainsNodeInfoType', TagModelContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagModelNotContainsNodeInfoType with content type ELEMENT_ONLY
class TagModelNotContainsNodeInfoType (TagModelUnaryNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagModelNotContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagModelNotContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 475, 2)
    _ElementMap = TagModelUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = TagModelUnaryNodeInfoType._AttributeMap.copy()
    # Base type is TagModelUnaryNodeInfoType
    
    # Element Text ({EventsGraphNavigator.Interaction.Entities}Text) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Pattern ({EventsGraphNavigator.Interaction.Entities}Pattern) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Alternatives ({EventsGraphNavigator.Interaction.Entities}Alternatives) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Sequence ({EventsGraphNavigator.Interaction.Entities}Sequence) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Number ({EventsGraphNavigator.Interaction.Entities}Number) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element Contains ({EventsGraphNavigator.Interaction.Entities}Contains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    
    # Element NotContains ({EventsGraphNavigator.Interaction.Entities}NotContains) inherited from {EventsGraphNavigator.Interaction.Entities}TagModelUnaryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagModelNotContainsNodeInfoType = TagModelNotContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'TagModelNotContainsNodeInfoType', TagModelNotContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesContainingTextFromSourceQueryInfoType with content type ELEMENT_ONLY
class LogMessagesContainingTextFromSourceQueryInfoType (LogMessagesQueryInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesContainingTextFromSourceQueryInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessagesContainingTextFromSourceQueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 718, 2)
    _ElementMap = LogMessagesQueryInfoType._ElementMap.copy()
    _AttributeMap = LogMessagesQueryInfoType._AttributeMap.copy()
    # Base type is LogMessagesQueryInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Source'), 'Source', '__EventsGraphNavigator_Interaction_Entities_LogMessagesContainingTextFromSourceQueryInfoType_EventsGraphNavigator_Interaction_EntitiesSource', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 722, 10), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_LogMessagesContainingTextFromSourceQueryInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 729, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}QueryInfoType
    _ElementMap.update({
        __Source.name() : __Source,
        __Text.name() : __Text
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogMessagesContainingTextFromSourceQueryInfoType = LogMessagesContainingTextFromSourceQueryInfoType
Namespace.addCategoryObject('typeBinding', 'LogMessagesContainingTextFromSourceQueryInfoType', LogMessagesContainingTextFromSourceQueryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesCustomQueryInfoType with content type ELEMENT_ONLY
class LogMessagesCustomQueryInfoType (LogMessagesQueryInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesCustomQueryInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessagesCustomQueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 743, 2)
    _ElementMap = LogMessagesQueryInfoType._ElementMap.copy()
    _AttributeMap = LogMessagesQueryInfoType._AttributeMap.copy()
    # Base type is LogMessagesQueryInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}IncludeObsoleteSources uses Python identifier IncludeObsoleteSources
    __IncludeObsoleteSources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncludeObsoleteSources'), 'IncludeObsoleteSources', '__EventsGraphNavigator_Interaction_Entities_LogMessagesCustomQueryInfoType_EventsGraphNavigator_Interaction_EntitiesIncludeObsoleteSources', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 747, 10), )

    
    IncludeObsoleteSources = property(__IncludeObsoleteSources.value, __IncludeObsoleteSources.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__EventsGraphNavigator_Interaction_Entities_LogMessagesCustomQueryInfoType_EventsGraphNavigator_Interaction_EntitiesModel', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 748, 10), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}QueryInfoType
    _ElementMap.update({
        __IncludeObsoleteSources.name() : __IncludeObsoleteSources,
        __Model.name() : __Model
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogMessagesCustomQueryInfoType = LogMessagesCustomQueryInfoType
Namespace.addCategoryObject('typeBinding', 'LogMessagesCustomQueryInfoType', LogMessagesCustomQueryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesFullTextQueryInfoType with content type ELEMENT_ONLY
class LogMessagesFullTextQueryInfoType (LogMessagesQueryInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}LogMessagesFullTextQueryInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogMessagesFullTextQueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 760, 2)
    _ElementMap = LogMessagesQueryInfoType._ElementMap.copy()
    _AttributeMap = LogMessagesQueryInfoType._AttributeMap.copy()
    # Base type is LogMessagesQueryInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}IncludeObsoleteSources uses Python identifier IncludeObsoleteSources
    __IncludeObsoleteSources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncludeObsoleteSources'), 'IncludeObsoleteSources', '__EventsGraphNavigator_Interaction_Entities_LogMessagesFullTextQueryInfoType_EventsGraphNavigator_Interaction_EntitiesIncludeObsoleteSources', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 764, 10), )

    
    IncludeObsoleteSources = property(__IncludeObsoleteSources.value, __IncludeObsoleteSources.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}QueryString uses Python identifier QueryString
    __QueryString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QueryString'), 'QueryString', '__EventsGraphNavigator_Interaction_Entities_LogMessagesFullTextQueryInfoType_EventsGraphNavigator_Interaction_EntitiesQueryString', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 765, 10), )

    
    QueryString = property(__QueryString.value, __QueryString.set, None, None)

    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}QueryInfoType
    _ElementMap.update({
        __IncludeObsoleteSources.name() : __IncludeObsoleteSources,
        __QueryString.name() : __QueryString
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LogMessagesFullTextQueryInfoType = LogMessagesFullTextQueryInfoType
Namespace.addCategoryObject('typeBinding', 'LogMessagesFullTextQueryInfoType', LogMessagesFullTextQueryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TagInstancesCustomQueryInfoType with content type ELEMENT_ONLY
class TagInstancesCustomQueryInfoType (TagInstancesQueryInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TagInstancesCustomQueryInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TagInstancesCustomQueryInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 771, 2)
    _ElementMap = TagInstancesQueryInfoType._ElementMap.copy()
    _AttributeMap = TagInstancesQueryInfoType._AttributeMap.copy()
    # Base type is TagInstancesQueryInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__EventsGraphNavigator_Interaction_Entities_TagInstancesCustomQueryInfoType_EventsGraphNavigator_Interaction_EntitiesModel', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 775, 10), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}QueryInfoType
    _ElementMap.update({
        __Model.name() : __Model
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TagInstancesCustomQueryInfoType = TagInstancesCustomQueryInfoType
Namespace.addCategoryObject('typeBinding', 'TagInstancesCustomQueryInfoType', TagInstancesCustomQueryInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageUnaryNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageUnaryNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 808, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TextContains uses Python identifier TextContains
    __TextContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TextContains'), 'TextContains', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesTextContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 814, 12), )

    
    TextContains = property(__TextContains.value, __TextContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LineNumberIs uses Python identifier LineNumberIs
    __LineNumberIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs'), 'LineNumberIs', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesLineNumberIs', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 815, 12), )

    
    LineNumberIs = property(__LineNumberIs.value, __LineNumberIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceNameContains uses Python identifier SourceNameContains
    __SourceNameContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains'), 'SourceNameContains', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSourceNameContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 816, 12), )

    
    SourceNameContains = property(__SourceNameContains.value, __SourceNameContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceIdIs uses Python identifier SourceIdIs
    __SourceIdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs'), 'SourceIdIs', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSourceIdIs', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 817, 12), )

    
    SourceIdIs = property(__SourceIdIs.value, __SourceIdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceHasMessage uses Python identifier SourceHasMessage
    __SourceHasMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage'), 'SourceHasMessage', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSourceHasMessage', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 818, 12), )

    
    SourceHasMessage = property(__SourceHasMessage.value, __SourceHasMessage.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance uses Python identifier MessageHasTagInstance
    __MessageHasTagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance'), 'MessageHasTagInstance', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesMessageHasTagInstance', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 819, 12), )

    
    MessageHasTagInstance = property(__MessageHasTagInstance.value, __MessageHasTagInstance.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}All uses Python identifier All
    __All = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'All'), 'All', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAll', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 820, 12), )

    
    All = property(__All.value, __All.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Any uses Python identifier Any
    __Any = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Any'), 'Any', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAny', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 821, 12), )

    
    Any = property(__Any.value, __Any.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __TextContains.name() : __TextContains,
        __LineNumberIs.name() : __LineNumberIs,
        __SourceNameContains.name() : __SourceNameContains,
        __SourceIdIs.name() : __SourceIdIs,
        __SourceHasMessage.name() : __SourceHasMessage,
        __MessageHasTagInstance.name() : __MessageHasTagInstance,
        __All.name() : __All,
        __Any.name() : __Any
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageUnaryNodeInfoType = QueryLogMessageUnaryNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageUnaryNodeInfoType', QueryLogMessageUnaryNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageGroupNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageGroupNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 828, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}TextContains uses Python identifier TextContains
    __TextContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TextContains'), 'TextContains', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesTextContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 834, 12), )

    
    TextContains = property(__TextContains.value, __TextContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}LineNumberIs uses Python identifier LineNumberIs
    __LineNumberIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs'), 'LineNumberIs', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesLineNumberIs', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 835, 12), )

    
    LineNumberIs = property(__LineNumberIs.value, __LineNumberIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceNameContains uses Python identifier SourceNameContains
    __SourceNameContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains'), 'SourceNameContains', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSourceNameContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 836, 12), )

    
    SourceNameContains = property(__SourceNameContains.value, __SourceNameContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceIdIs uses Python identifier SourceIdIs
    __SourceIdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs'), 'SourceIdIs', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSourceIdIs', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 837, 12), )

    
    SourceIdIs = property(__SourceIdIs.value, __SourceIdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}SourceHasMessage uses Python identifier SourceHasMessage
    __SourceHasMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage'), 'SourceHasMessage', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesSourceHasMessage', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 838, 12), )

    
    SourceHasMessage = property(__SourceHasMessage.value, __SourceHasMessage.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance uses Python identifier MessageHasTagInstance
    __MessageHasTagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance'), 'MessageHasTagInstance', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesMessageHasTagInstance', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 839, 12), )

    
    MessageHasTagInstance = property(__MessageHasTagInstance.value, __MessageHasTagInstance.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}All uses Python identifier All
    __All = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'All'), 'All', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAll', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 840, 12), )

    
    All = property(__All.value, __All.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Any uses Python identifier Any
    __Any = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Any'), 'Any', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAny', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 841, 12), )

    
    Any = property(__Any.value, __Any.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __TextContains.name() : __TextContains,
        __LineNumberIs.name() : __LineNumberIs,
        __SourceNameContains.name() : __SourceNameContains,
        __SourceIdIs.name() : __SourceIdIs,
        __SourceHasMessage.name() : __SourceHasMessage,
        __MessageHasTagInstance.name() : __MessageHasTagInstance,
        __All.name() : __All,
        __Any.name() : __Any
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageGroupNodeInfoType = QueryLogMessageGroupNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageGroupNodeInfoType', QueryLogMessageGroupNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageTextContainsNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageTextContainsNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageTextContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageTextContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 861, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageTextContainsNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 865, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Text.name() : __Text
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageTextContainsNodeInfoType = QueryLogMessageTextContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageTextContainsNodeInfoType', QueryLogMessageTextContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageLineNumberIsNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageLineNumberIsNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageLineNumberIsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageLineNumberIsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 871, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageLineNumberIsNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValue', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 875, 10), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageLineNumberIsNodeInfoType = QueryLogMessageLineNumberIsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageLineNumberIsNodeInfoType', QueryLogMessageLineNumberIsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageSourceNameContainsNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageSourceNameContainsNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageSourceNameContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageSourceNameContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 881, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageSourceNameContainsNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 885, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Text.name() : __Text
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageSourceNameContainsNodeInfoType = QueryLogMessageSourceNameContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageSourceNameContainsNodeInfoType', QueryLogMessageSourceNameContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageSourceIdIsNodeInfoType with content type EMPTY
class QueryLogMessageSourceIdIsNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageSourceIdIsNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageSourceIdIsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 891, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageSourceIdIsNodeInfoType_Value', _module_typeBindings.GuidString, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 894, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 894, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })
_module_typeBindings.QueryLogMessageSourceIdIsNodeInfoType = QueryLogMessageSourceIdIsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageSourceIdIsNodeInfoType', QueryLogMessageSourceIdIsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageSourceHasMessageNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageSourceHasMessageNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageSourceHasMessageNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageSourceHasMessageNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 899, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Where uses Python identifier Where
    __Where = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Where'), 'Where', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageSourceHasMessageNodeInfoType_EventsGraphNavigator_Interaction_EntitiesWhere', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 903, 10), )

    
    Where = property(__Where.value, __Where.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Where.name() : __Where
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageSourceHasMessageNodeInfoType = QueryLogMessageSourceHasMessageNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageSourceHasMessageNodeInfoType', QueryLogMessageSourceHasMessageNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageHasTagInstanceNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageHasTagInstanceNodeInfoType (QueryLogMessageNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageHasTagInstanceNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageHasTagInstanceNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 915, 2)
    _ElementMap = QueryLogMessageNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Where uses Python identifier Where
    __Where = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Where'), 'Where', '__EventsGraphNavigator_Interaction_Entities_QueryLogMessageHasTagInstanceNodeInfoType_EventsGraphNavigator_Interaction_EntitiesWhere', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 919, 10), )

    
    Where = property(__Where.value, __Where.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Where.name() : __Where
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageHasTagInstanceNodeInfoType = QueryLogMessageHasTagInstanceNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageHasTagInstanceNodeInfoType', QueryLogMessageHasTagInstanceNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceUnaryNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceUnaryNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 956, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternNameContains uses Python identifier PatternNameContains
    __PatternNameContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains'), 'PatternNameContains', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesPatternNameContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12), )

    
    PatternNameContains = property(__PatternNameContains.value, __PatternNameContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternIdIs uses Python identifier PatternIdIs
    __PatternIdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs'), 'PatternIdIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesPatternIdIs', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12), )

    
    PatternIdIs = property(__PatternIdIs.value, __PatternIdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}IdIs uses Python identifier IdIs
    __IdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdIs'), 'IdIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesIdIs', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12), )

    
    IdIs = property(__IdIs.value, __IdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey uses Python identifier TagInstanceHasKey
    __TagInstanceHasKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey'), 'TagInstanceHasKey', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesTagInstanceHasKey', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12), )

    
    TagInstanceHasKey = property(__TagInstanceHasKey.value, __TagInstanceHasKey.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage uses Python identifier TagInstanceIsInMessage
    __TagInstanceIsInMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage'), 'TagInstanceIsInMessage', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesTagInstanceIsInMessage', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12), )

    
    TagInstanceIsInMessage = property(__TagInstanceIsInMessage.value, __TagInstanceIsInMessage.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}All uses Python identifier All
    __All = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'All'), 'All', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAll', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12), )

    
    All = property(__All.value, __All.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Any uses Python identifier Any
    __Any = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Any'), 'Any', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAny', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12), )

    
    Any = property(__Any.value, __Any.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __PatternNameContains.name() : __PatternNameContains,
        __PatternIdIs.name() : __PatternIdIs,
        __IdIs.name() : __IdIs,
        __TagInstanceHasKey.name() : __TagInstanceHasKey,
        __TagInstanceIsInMessage.name() : __TagInstanceIsInMessage,
        __All.name() : __All,
        __Any.name() : __Any
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceUnaryNodeInfoType = QueryTagInstanceUnaryNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceUnaryNodeInfoType', QueryTagInstanceUnaryNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceGroupNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceGroupNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 975, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternNameContains uses Python identifier PatternNameContains
    __PatternNameContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains'), 'PatternNameContains', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesPatternNameContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 981, 12), )

    
    PatternNameContains = property(__PatternNameContains.value, __PatternNameContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}PatternIdIs uses Python identifier PatternIdIs
    __PatternIdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs'), 'PatternIdIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesPatternIdIs', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 982, 12), )

    
    PatternIdIs = property(__PatternIdIs.value, __PatternIdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}IdIs uses Python identifier IdIs
    __IdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdIs'), 'IdIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesIdIs', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 983, 12), )

    
    IdIs = property(__IdIs.value, __IdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey uses Python identifier TagInstanceHasKey
    __TagInstanceHasKey = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey'), 'TagInstanceHasKey', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesTagInstanceHasKey', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 984, 12), )

    
    TagInstanceHasKey = property(__TagInstanceHasKey.value, __TagInstanceHasKey.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage uses Python identifier TagInstanceIsInMessage
    __TagInstanceIsInMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage'), 'TagInstanceIsInMessage', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesTagInstanceIsInMessage', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 985, 12), )

    
    TagInstanceIsInMessage = property(__TagInstanceIsInMessage.value, __TagInstanceIsInMessage.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}All uses Python identifier All
    __All = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'All'), 'All', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAll', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 986, 12), )

    
    All = property(__All.value, __All.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Any uses Python identifier Any
    __Any = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Any'), 'Any', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAny', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 987, 12), )

    
    Any = property(__Any.value, __Any.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __PatternNameContains.name() : __PatternNameContains,
        __PatternIdIs.name() : __PatternIdIs,
        __IdIs.name() : __IdIs,
        __TagInstanceHasKey.name() : __TagInstanceHasKey,
        __TagInstanceIsInMessage.name() : __TagInstanceIsInMessage,
        __All.name() : __All,
        __Any.name() : __Any
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceGroupNodeInfoType = QueryTagInstanceGroupNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceGroupNodeInfoType', QueryTagInstanceGroupNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstancePatternNameContainsNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstancePatternNameContainsNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstancePatternNameContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstancePatternNameContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1006, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstancePatternNameContainsNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1010, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Text.name() : __Text
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstancePatternNameContainsNodeInfoType = QueryTagInstancePatternNameContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstancePatternNameContainsNodeInfoType', QueryTagInstancePatternNameContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceIsInMessageNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceIsInMessageNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceIsInMessageNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceIsInMessageNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1030, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Where uses Python identifier Where
    __Where = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Where'), 'Where', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceIsInMessageNodeInfoType_EventsGraphNavigator_Interaction_EntitiesWhere', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1034, 10), )

    
    Where = property(__Where.value, __Where.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Where.name() : __Where
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceIsInMessageNodeInfoType = QueryTagInstanceIsInMessageNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceIsInMessageNodeInfoType', QueryTagInstanceIsInMessageNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstancePatternIdIsNodeInfoType with content type EMPTY
class QueryTagInstancePatternIdIsNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstancePatternIdIsNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstancePatternIdIsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1046, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstancePatternIdIsNodeInfoType_Value', _module_typeBindings.GuidString, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1049, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1049, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })
_module_typeBindings.QueryTagInstancePatternIdIsNodeInfoType = QueryTagInstancePatternIdIsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstancePatternIdIsNodeInfoType', QueryTagInstancePatternIdIsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceIdIsNodeInfoType with content type EMPTY
class QueryTagInstanceIdIsNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceIdIsNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceIdIsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1054, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceIdIsNodeInfoType_Value', _module_typeBindings.GuidString, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1057, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1057, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })
_module_typeBindings.QueryTagInstanceIdIsNodeInfoType = QueryTagInstanceIdIsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceIdIsNodeInfoType', QueryTagInstanceIdIsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceHasKeyNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceHasKeyNodeInfoType (QueryTagInstanceNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceHasKeyNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceHasKeyNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1062, 2)
    _ElementMap = QueryTagInstanceNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Where uses Python identifier Where
    __Where = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Where'), 'Where', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceHasKeyNodeInfoType_EventsGraphNavigator_Interaction_EntitiesWhere', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1066, 10), )

    
    Where = property(__Where.value, __Where.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Where.name() : __Where
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceHasKeyNodeInfoType = QueryTagInstanceHasKeyNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceHasKeyNodeInfoType', QueryTagInstanceHasKeyNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyUnaryNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyUnaryNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1089, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ValuePatternNameContains uses Python identifier ValuePatternNameContains
    __ValuePatternNameContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains'), 'ValuePatternNameContains', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValuePatternNameContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1095, 12), )

    
    ValuePatternNameContains = property(__ValuePatternNameContains.value, __ValuePatternNameContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ValuePatternIdIs uses Python identifier ValuePatternIdIs
    __ValuePatternIdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs'), 'ValuePatternIdIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValuePatternIdIs', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1096, 12), )

    
    ValuePatternIdIs = property(__ValuePatternIdIs.value, __ValuePatternIdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ValueContains uses Python identifier ValueContains
    __ValueContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueContains'), 'ValueContains', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValueContains', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1097, 12), )

    
    ValueContains = property(__ValueContains.value, __ValueContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ValueContainsTag uses Python identifier ValueContainsTag
    __ValueContainsTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag'), 'ValueContainsTag', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValueContainsTag', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1098, 12), )

    
    ValueContainsTag = property(__ValueContainsTag.value, __ValueContainsTag.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}KeyIsInTagInstance uses Python identifier KeyIsInTagInstance
    __KeyIsInTagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance'), 'KeyIsInTagInstance', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesKeyIsInTagInstance', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1099, 12), )

    
    KeyIsInTagInstance = property(__KeyIsInTagInstance.value, __KeyIsInTagInstance.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}OrderIs uses Python identifier OrderIs
    __OrderIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrderIs'), 'OrderIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesOrderIs', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1100, 12), )

    
    OrderIs = property(__OrderIs.value, __OrderIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}All uses Python identifier All
    __All = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'All'), 'All', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAll', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1101, 12), )

    
    All = property(__All.value, __All.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Any uses Python identifier Any
    __Any = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Any'), 'Any', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyUnaryNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAny', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1102, 12), )

    
    Any = property(__Any.value, __Any.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __ValuePatternNameContains.name() : __ValuePatternNameContains,
        __ValuePatternIdIs.name() : __ValuePatternIdIs,
        __ValueContains.name() : __ValueContains,
        __ValueContainsTag.name() : __ValueContainsTag,
        __KeyIsInTagInstance.name() : __KeyIsInTagInstance,
        __OrderIs.name() : __OrderIs,
        __All.name() : __All,
        __Any.name() : __Any
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyUnaryNodeInfoType = QueryTagInstanceKeyUnaryNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyUnaryNodeInfoType', QueryTagInstanceKeyUnaryNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyGroupNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyGroupNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1109, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ValuePatternNameContains uses Python identifier ValuePatternNameContains
    __ValuePatternNameContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains'), 'ValuePatternNameContains', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValuePatternNameContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1115, 12), )

    
    ValuePatternNameContains = property(__ValuePatternNameContains.value, __ValuePatternNameContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ValuePatternIdIs uses Python identifier ValuePatternIdIs
    __ValuePatternIdIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs'), 'ValuePatternIdIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValuePatternIdIs', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1116, 12), )

    
    ValuePatternIdIs = property(__ValuePatternIdIs.value, __ValuePatternIdIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ValueContains uses Python identifier ValueContains
    __ValueContains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueContains'), 'ValueContains', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValueContains', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1117, 12), )

    
    ValueContains = property(__ValueContains.value, __ValueContains.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ValueContainsTag uses Python identifier ValueContainsTag
    __ValueContainsTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag'), 'ValueContainsTag', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesValueContainsTag', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1118, 12), )

    
    ValueContainsTag = property(__ValueContainsTag.value, __ValueContainsTag.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}KeyIsInTagInstance uses Python identifier KeyIsInTagInstance
    __KeyIsInTagInstance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance'), 'KeyIsInTagInstance', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesKeyIsInTagInstance', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1119, 12), )

    
    KeyIsInTagInstance = property(__KeyIsInTagInstance.value, __KeyIsInTagInstance.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}OrderIs uses Python identifier OrderIs
    __OrderIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrderIs'), 'OrderIs', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesOrderIs', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1120, 12), )

    
    OrderIs = property(__OrderIs.value, __OrderIs.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}All uses Python identifier All
    __All = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'All'), 'All', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAll', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1121, 12), )

    
    All = property(__All.value, __All.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Any uses Python identifier Any
    __Any = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Any'), 'Any', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyGroupNodeInfoType_EventsGraphNavigator_Interaction_EntitiesAny', True, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1122, 12), )

    
    Any = property(__Any.value, __Any.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __ValuePatternNameContains.name() : __ValuePatternNameContains,
        __ValuePatternIdIs.name() : __ValuePatternIdIs,
        __ValueContains.name() : __ValueContains,
        __ValueContainsTag.name() : __ValueContainsTag,
        __KeyIsInTagInstance.name() : __KeyIsInTagInstance,
        __OrderIs.name() : __OrderIs,
        __All.name() : __All,
        __Any.name() : __Any
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyGroupNodeInfoType = QueryTagInstanceKeyGroupNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyGroupNodeInfoType', QueryTagInstanceKeyGroupNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValuePatternNameContainsNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyValuePatternNameContainsNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValuePatternNameContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyValuePatternNameContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1142, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyValuePatternNameContainsNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1146, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Text.name() : __Text
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyValuePatternNameContainsNodeInfoType = QueryTagInstanceKeyValuePatternNameContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyValuePatternNameContainsNodeInfoType', QueryTagInstanceKeyValuePatternNameContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValueContainsNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyValueContainsNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValueContainsNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyValueContainsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1152, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Text uses Python identifier Text
    __Text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Text'), 'Text', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyValueContainsNodeInfoType_EventsGraphNavigator_Interaction_EntitiesText', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1156, 10), )

    
    Text = property(__Text.value, __Text.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Text.name() : __Text
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyValueContainsNodeInfoType = QueryTagInstanceKeyValueContainsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyValueContainsNodeInfoType', QueryTagInstanceKeyValueContainsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1162, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Where uses Python identifier Where
    __Where = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Where'), 'Where', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType_EventsGraphNavigator_Interaction_EntitiesWhere', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1166, 10), )

    
    Where = property(__Where.value, __Where.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Where.name() : __Where
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType = QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType', QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValuePatternIdIsNodeInfoType with content type EMPTY
class QueryTagInstanceKeyValuePatternIdIsNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyValuePatternIdIsNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyValuePatternIdIsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1178, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyValuePatternIdIsNodeInfoType_Value', _module_typeBindings.GuidString, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1181, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1181, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })
_module_typeBindings.QueryTagInstanceKeyValuePatternIdIsNodeInfoType = QueryTagInstanceKeyValuePatternIdIsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyValuePatternIdIsNodeInfoType', QueryTagInstanceKeyValuePatternIdIsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyIsInTagInstanceNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyIsInTagInstanceNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyIsInTagInstanceNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyIsInTagInstanceNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1186, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Where uses Python identifier Where
    __Where = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Where'), 'Where', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyIsInTagInstanceNodeInfoType_EventsGraphNavigator_Interaction_EntitiesWhere', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1190, 10), )

    
    Where = property(__Where.value, __Where.set, None, None)

    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        __Where.name() : __Where
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyIsInTagInstanceNodeInfoType = QueryTagInstanceKeyIsInTagInstanceNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyIsInTagInstanceNodeInfoType', QueryTagInstanceKeyIsInTagInstanceNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyOrderIsNodeInfoType with content type EMPTY
class QueryTagInstanceKeyOrderIsNodeInfoType (QueryTagInstanceKeyNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyOrderIsNodeInfoType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyOrderIsNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1202, 2)
    _ElementMap = QueryTagInstanceKeyNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__EventsGraphNavigator_Interaction_Entities_QueryTagInstanceKeyOrderIsNodeInfoType_Value', _module_typeBindings.int, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1205, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1205, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })
_module_typeBindings.QueryTagInstanceKeyOrderIsNodeInfoType = QueryTagInstanceKeyOrderIsNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyOrderIsNodeInfoType', QueryTagInstanceKeyOrderIsNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}TaskEntityType with content type ELEMENT_ONLY
class TaskEntityType (NamedEntityBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}TaskEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaskEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1247, 2)
    _ElementMap = NamedEntityBaseType._ElementMap.copy()
    _AttributeMap = NamedEntityBaseType._AttributeMap.copy()
    # Base type is NamedEntityBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__EventsGraphNavigator_Interaction_Entities_TaskEntityType_EventsGraphNavigator_Interaction_EntitiesStatus', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1251, 10), )

    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    
    # Attribute State uses Python identifier State
    __State = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'State'), 'State', '__EventsGraphNavigator_Interaction_Entities_TaskEntityType_State', _module_typeBindings.TaskStateType, required=True)
    __State._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1253, 8)
    __State._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1253, 8)
    
    State = property(__State.value, __State.set, None, None)

    
    # Attribute Progress uses Python identifier Progress
    __Progress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Progress'), 'Progress', '__EventsGraphNavigator_Interaction_Entities_TaskEntityType_Progress', _module_typeBindings.int, required=True)
    __Progress._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1254, 8)
    __Progress._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1254, 8)
    
    Progress = property(__Progress.value, __Progress.set, None, None)

    
    # Attribute CreationTime uses Python identifier CreationTime
    __CreationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreationTime'), 'CreationTime', '__EventsGraphNavigator_Interaction_Entities_TaskEntityType_CreationTime', _module_typeBindings.DateTime, required=True)
    __CreationTime._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1255, 8)
    __CreationTime._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1255, 8)
    
    CreationTime = property(__CreationTime.value, __CreationTime.set, None, None)

    
    # Attribute StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'StartTime'), 'StartTime', '__EventsGraphNavigator_Interaction_Entities_TaskEntityType_StartTime', _module_typeBindings.DateTime, required=True)
    __StartTime._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1256, 8)
    __StartTime._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1256, 8)
    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Attribute EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'EndTime'), 'EndTime', '__EventsGraphNavigator_Interaction_Entities_TaskEntityType_EndTime', _module_typeBindings.DateTime, required=True)
    __EndTime._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1257, 8)
    __EndTime._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1257, 8)
    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    _ElementMap.update({
        __Status.name() : __Status
    })
    _AttributeMap.update({
        __State.name() : __State,
        __Progress.name() : __Progress,
        __CreationTime.name() : __CreationTime,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime
    })
_module_typeBindings.TaskEntityType = TaskEntityType
Namespace.addCategoryObject('typeBinding', 'TaskEntityType', TaskEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}SourcesFolderEntityType with content type ELEMENT_ONLY
class SourcesFolderEntityType (SourcesItemBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourcesFolderEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourcesFolderEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 104, 2)
    _ElementMap = SourcesItemBaseType._ElementMap.copy()
    _AttributeMap = SourcesItemBaseType._AttributeMap.copy()
    # Base type is SourcesItemBaseType
    
    # Element Description ({EventsGraphNavigator.Interaction.Entities}Description) inherited from {EventsGraphNavigator.Interaction.Entities}SourcesItemBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ChildFolders uses Python identifier ChildFolders
    __ChildFolders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChildFolders'), 'ChildFolders', '__EventsGraphNavigator_Interaction_Entities_SourcesFolderEntityType_EventsGraphNavigator_Interaction_EntitiesChildFolders', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 108, 10), )

    
    ChildFolders = property(__ChildFolders.value, __ChildFolders.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ChildSources uses Python identifier ChildSources
    __ChildSources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChildSources'), 'ChildSources', '__EventsGraphNavigator_Interaction_Entities_SourcesFolderEntityType_EventsGraphNavigator_Interaction_EntitiesChildSources', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 119, 10), )

    
    ChildSources = property(__ChildSources.value, __ChildSources.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __ChildFolders.name() : __ChildFolders,
        __ChildSources.name() : __ChildSources
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SourcesFolderEntityType = SourcesFolderEntityType
Namespace.addCategoryObject('typeBinding', 'SourcesFolderEntityType', SourcesFolderEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}SourcesSourceEntityType with content type ELEMENT_ONLY
class SourcesSourceEntityType (SourcesItemBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}SourcesSourceEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SourcesSourceEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 135, 2)
    _ElementMap = SourcesItemBaseType._ElementMap.copy()
    _AttributeMap = SourcesItemBaseType._AttributeMap.copy()
    # Base type is SourcesItemBaseType
    
    # Element Description ({EventsGraphNavigator.Interaction.Entities}Description) inherited from {EventsGraphNavigator.Interaction.Entities}SourcesItemBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}IsObsolete uses Python identifier IsObsolete
    __IsObsolete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IsObsolete'), 'IsObsolete', '__EventsGraphNavigator_Interaction_Entities_SourcesSourceEntityType_EventsGraphNavigator_Interaction_EntitiesIsObsolete', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 139, 10), )

    
    IsObsolete = property(__IsObsolete.value, __IsObsolete.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ControlOptions uses Python identifier ControlOptions
    __ControlOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlOptions'), 'ControlOptions', '__EventsGraphNavigator_Interaction_Entities_SourcesSourceEntityType_EventsGraphNavigator_Interaction_EntitiesControlOptions', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 140, 10), )

    
    ControlOptions = property(__ControlOptions.value, __ControlOptions.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}Childs uses Python identifier Childs
    __Childs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Childs'), 'Childs', '__EventsGraphNavigator_Interaction_Entities_SourcesSourceEntityType_EventsGraphNavigator_Interaction_EntitiesChilds', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 141, 10), )

    
    Childs = property(__Childs.value, __Childs.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __IsObsolete.name() : __IsObsolete,
        __ControlOptions.name() : __ControlOptions,
        __Childs.name() : __Childs
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SourcesSourceEntityType = SourcesSourceEntityType
Namespace.addCategoryObject('typeBinding', 'SourcesSourceEntityType', SourcesSourceEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}PatternsFolderEntityType with content type ELEMENT_ONLY
class PatternsFolderEntityType (PatternsItemBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}PatternsFolderEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PatternsFolderEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 242, 2)
    _ElementMap = PatternsItemBaseType._ElementMap.copy()
    _AttributeMap = PatternsItemBaseType._AttributeMap.copy()
    # Base type is PatternsItemBaseType
    
    # Element Description ({EventsGraphNavigator.Interaction.Entities}Description) inherited from {EventsGraphNavigator.Interaction.Entities}PatternsItemBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}ChildFolders uses Python identifier ChildFolders
    __ChildFolders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChildFolders'), 'ChildFolders', '__EventsGraphNavigator_Interaction_Entities_PatternsFolderEntityType_EventsGraphNavigator_Interaction_EntitiesChildFolders', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 246, 10), )

    
    ChildFolders = property(__ChildFolders.value, __ChildFolders.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ChildRegexPatterns uses Python identifier ChildRegexPatterns
    __ChildRegexPatterns = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChildRegexPatterns'), 'ChildRegexPatterns', '__EventsGraphNavigator_Interaction_Entities_PatternsFolderEntityType_EventsGraphNavigator_Interaction_EntitiesChildRegexPatterns', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 257, 10), )

    
    ChildRegexPatterns = property(__ChildRegexPatterns.value, __ChildRegexPatterns.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ChildTagPatterns uses Python identifier ChildTagPatterns
    __ChildTagPatterns = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChildTagPatterns'), 'ChildTagPatterns', '__EventsGraphNavigator_Interaction_Entities_PatternsFolderEntityType_EventsGraphNavigator_Interaction_EntitiesChildTagPatterns', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 268, 10), )

    
    ChildTagPatterns = property(__ChildTagPatterns.value, __ChildTagPatterns.set, None, None)

    
    # Element {EventsGraphNavigator.Interaction.Entities}ChildLinePatterns uses Python identifier ChildLinePatterns
    __ChildLinePatterns = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChildLinePatterns'), 'ChildLinePatterns', '__EventsGraphNavigator_Interaction_Entities_PatternsFolderEntityType_EventsGraphNavigator_Interaction_EntitiesChildLinePatterns', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 279, 10), )

    
    ChildLinePatterns = property(__ChildLinePatterns.value, __ChildLinePatterns.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __ChildFolders.name() : __ChildFolders,
        __ChildRegexPatterns.name() : __ChildRegexPatterns,
        __ChildTagPatterns.name() : __ChildTagPatterns,
        __ChildLinePatterns.name() : __ChildLinePatterns
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PatternsFolderEntityType = PatternsFolderEntityType
Namespace.addCategoryObject('typeBinding', 'PatternsFolderEntityType', PatternsFolderEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}PatternsRegexPatternEntityType with content type ELEMENT_ONLY
class PatternsRegexPatternEntityType (PatternsItemBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}PatternsRegexPatternEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PatternsRegexPatternEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 295, 2)
    _ElementMap = PatternsItemBaseType._ElementMap.copy()
    _AttributeMap = PatternsItemBaseType._AttributeMap.copy()
    # Base type is PatternsItemBaseType
    
    # Element Description ({EventsGraphNavigator.Interaction.Entities}Description) inherited from {EventsGraphNavigator.Interaction.Entities}PatternsItemBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Expression uses Python identifier Expression
    __Expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Expression'), 'Expression', '__EventsGraphNavigator_Interaction_Entities_PatternsRegexPatternEntityType_EventsGraphNavigator_Interaction_EntitiesExpression', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 299, 10), )

    
    Expression = property(__Expression.value, __Expression.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __Expression.name() : __Expression
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PatternsRegexPatternEntityType = PatternsRegexPatternEntityType
Namespace.addCategoryObject('typeBinding', 'PatternsRegexPatternEntityType', PatternsRegexPatternEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}PatternsTagPatternEntityType with content type ELEMENT_ONLY
class PatternsTagPatternEntityType (PatternsItemBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}PatternsTagPatternEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PatternsTagPatternEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 305, 2)
    _ElementMap = PatternsItemBaseType._ElementMap.copy()
    _AttributeMap = PatternsItemBaseType._AttributeMap.copy()
    # Base type is PatternsItemBaseType
    
    # Element Description ({EventsGraphNavigator.Interaction.Entities}Description) inherited from {EventsGraphNavigator.Interaction.Entities}PatternsItemBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__EventsGraphNavigator_Interaction_Entities_PatternsTagPatternEntityType_EventsGraphNavigator_Interaction_EntitiesModel', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    
    # Attribute MatchingMode uses Python identifier MatchingMode
    __MatchingMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MatchingMode'), 'MatchingMode', '__EventsGraphNavigator_Interaction_Entities_PatternsTagPatternEntityType_MatchingMode', _module_typeBindings.TagMatchingModeType, required=True)
    __MatchingMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 311, 8)
    __MatchingMode._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 311, 8)
    
    MatchingMode = property(__MatchingMode.value, __MatchingMode.set, None, None)

    
    # Attribute OrderSpecific uses Python identifier OrderSpecific
    __OrderSpecific = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'OrderSpecific'), 'OrderSpecific', '__EventsGraphNavigator_Interaction_Entities_PatternsTagPatternEntityType_OrderSpecific', _module_typeBindings.bool, required=True)
    __OrderSpecific._DeclarationLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 312, 8)
    __OrderSpecific._UseLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 312, 8)
    
    OrderSpecific = property(__OrderSpecific.value, __OrderSpecific.set, None, None)

    _ElementMap.update({
        __Model.name() : __Model
    })
    _AttributeMap.update({
        __MatchingMode.name() : __MatchingMode,
        __OrderSpecific.name() : __OrderSpecific
    })
_module_typeBindings.PatternsTagPatternEntityType = PatternsTagPatternEntityType
Namespace.addCategoryObject('typeBinding', 'PatternsTagPatternEntityType', PatternsTagPatternEntityType)


# Complex type {EventsGraphNavigator.Interaction.Entities}PatternsLinePatternEntityType with content type ELEMENT_ONLY
class PatternsLinePatternEntityType (PatternsItemBaseType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}PatternsLinePatternEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PatternsLinePatternEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 317, 2)
    _ElementMap = PatternsItemBaseType._ElementMap.copy()
    _AttributeMap = PatternsItemBaseType._AttributeMap.copy()
    # Base type is PatternsItemBaseType
    
    # Element Description ({EventsGraphNavigator.Interaction.Entities}Description) inherited from {EventsGraphNavigator.Interaction.Entities}PatternsItemBaseType
    
    # Element {EventsGraphNavigator.Interaction.Entities}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__EventsGraphNavigator_Interaction_Entities_PatternsLinePatternEntityType_EventsGraphNavigator_Interaction_EntitiesModel', False, pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute IdString inherited from {EventsGraphNavigator.Interaction.Entities}IdentifiedEntityBaseType
    
    # Attribute Name inherited from {EventsGraphNavigator.Interaction.Entities}NamedEntityBaseType
    _ElementMap.update({
        __Model.name() : __Model
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PatternsLinePatternEntityType = PatternsLinePatternEntityType
Namespace.addCategoryObject('typeBinding', 'PatternsLinePatternEntityType', PatternsLinePatternEntityType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (QueryLogMessageUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 749, 12)
    _ElementMap = QueryLogMessageUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageUnaryNodeInfoType
    
    # Element TextContains ({EventsGraphNavigator.Interaction.Entities}TextContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element LineNumberIs ({EventsGraphNavigator.Interaction.Entities}LineNumberIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceNameContains ({EventsGraphNavigator.Interaction.Entities}SourceNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceIdIs ({EventsGraphNavigator.Interaction.Entities}SourceIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceHasMessage ({EventsGraphNavigator.Interaction.Entities}SourceHasMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element MessageHasTagInstance ({EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (QueryTagInstanceUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 776, 12)
    _ElementMap = QueryTagInstanceUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternNameContains ({EventsGraphNavigator.Interaction.Entities}PatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternIdIs ({EventsGraphNavigator.Interaction.Entities}PatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element IdIs ({EventsGraphNavigator.Interaction.Entities}IdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceHasKey ({EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceIsInMessage ({EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (QueryLogMessageUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 904, 12)
    _ElementMap = QueryLogMessageUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageUnaryNodeInfoType
    
    # Element TextContains ({EventsGraphNavigator.Interaction.Entities}TextContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element LineNumberIs ({EventsGraphNavigator.Interaction.Entities}LineNumberIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceNameContains ({EventsGraphNavigator.Interaction.Entities}SourceNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceIdIs ({EventsGraphNavigator.Interaction.Entities}SourceIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceHasMessage ({EventsGraphNavigator.Interaction.Entities}SourceHasMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element MessageHasTagInstance ({EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (QueryTagInstanceUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 920, 12)
    _ElementMap = QueryTagInstanceUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternNameContains ({EventsGraphNavigator.Interaction.Entities}PatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternIdIs ({EventsGraphNavigator.Interaction.Entities}PatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element IdIs ({EventsGraphNavigator.Interaction.Entities}IdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceHasKey ({EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceIsInMessage ({EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageAllNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageAllNodeInfoType (QueryLogMessageGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageAllNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageAllNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 931, 2)
    _ElementMap = QueryLogMessageGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageGroupNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageGroupNodeInfoType
    
    # Element TextContains ({EventsGraphNavigator.Interaction.Entities}TextContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element LineNumberIs ({EventsGraphNavigator.Interaction.Entities}LineNumberIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element SourceNameContains ({EventsGraphNavigator.Interaction.Entities}SourceNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element SourceIdIs ({EventsGraphNavigator.Interaction.Entities}SourceIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element SourceHasMessage ({EventsGraphNavigator.Interaction.Entities}SourceHasMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element MessageHasTagInstance ({EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageAllNodeInfoType = QueryLogMessageAllNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageAllNodeInfoType', QueryLogMessageAllNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageAnyNodeInfoType with content type ELEMENT_ONLY
class QueryLogMessageAnyNodeInfoType (QueryLogMessageGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryLogMessageAnyNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryLogMessageAnyNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 938, 2)
    _ElementMap = QueryLogMessageGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageGroupNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageGroupNodeInfoType
    
    # Element TextContains ({EventsGraphNavigator.Interaction.Entities}TextContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element LineNumberIs ({EventsGraphNavigator.Interaction.Entities}LineNumberIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element SourceNameContains ({EventsGraphNavigator.Interaction.Entities}SourceNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element SourceIdIs ({EventsGraphNavigator.Interaction.Entities}SourceIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element SourceHasMessage ({EventsGraphNavigator.Interaction.Entities}SourceHasMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element MessageHasTagInstance ({EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageGroupNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryLogMessageAnyNodeInfoType = QueryLogMessageAnyNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryLogMessageAnyNodeInfoType', QueryLogMessageAnyNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceAllNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceAllNodeInfoType (QueryTagInstanceGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceAllNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceAllNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1016, 2)
    _ElementMap = QueryTagInstanceGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceGroupNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceGroupNodeInfoType
    
    # Element PatternNameContains ({EventsGraphNavigator.Interaction.Entities}PatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element PatternIdIs ({EventsGraphNavigator.Interaction.Entities}PatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element IdIs ({EventsGraphNavigator.Interaction.Entities}IdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element TagInstanceHasKey ({EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element TagInstanceIsInMessage ({EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceAllNodeInfoType = QueryTagInstanceAllNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceAllNodeInfoType', QueryTagInstanceAllNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceAnyNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceAnyNodeInfoType (QueryTagInstanceGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceAnyNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceAnyNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1023, 2)
    _ElementMap = QueryTagInstanceGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceGroupNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceGroupNodeInfoType
    
    # Element PatternNameContains ({EventsGraphNavigator.Interaction.Entities}PatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element PatternIdIs ({EventsGraphNavigator.Interaction.Entities}PatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element IdIs ({EventsGraphNavigator.Interaction.Entities}IdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element TagInstanceHasKey ({EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element TagInstanceIsInMessage ({EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceGroupNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceAnyNodeInfoType = QueryTagInstanceAnyNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceAnyNodeInfoType', QueryTagInstanceAnyNodeInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (QueryLogMessageUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1035, 12)
    _ElementMap = QueryLogMessageUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryLogMessageUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryLogMessageUnaryNodeInfoType
    
    # Element TextContains ({EventsGraphNavigator.Interaction.Entities}TextContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element LineNumberIs ({EventsGraphNavigator.Interaction.Entities}LineNumberIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceNameContains ({EventsGraphNavigator.Interaction.Entities}SourceNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceIdIs ({EventsGraphNavigator.Interaction.Entities}SourceIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element SourceHasMessage ({EventsGraphNavigator.Interaction.Entities}SourceHasMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element MessageHasTagInstance ({EventsGraphNavigator.Interaction.Entities}MessageHasTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryLogMessageUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (QueryTagInstanceKeyUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1067, 12)
    _ElementMap = QueryTagInstanceKeyUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element ValuePatternNameContains ({EventsGraphNavigator.Interaction.Entities}ValuePatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element ValuePatternIdIs ({EventsGraphNavigator.Interaction.Entities}ValuePatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element ValueContains ({EventsGraphNavigator.Interaction.Entities}ValueContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element ValueContainsTag ({EventsGraphNavigator.Interaction.Entities}ValueContainsTag) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element KeyIsInTagInstance ({EventsGraphNavigator.Interaction.Entities}KeyIsInTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element OrderIs ({EventsGraphNavigator.Interaction.Entities}OrderIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (QueryTagInstanceUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1167, 12)
    _ElementMap = QueryTagInstanceUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternNameContains ({EventsGraphNavigator.Interaction.Entities}PatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternIdIs ({EventsGraphNavigator.Interaction.Entities}PatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element IdIs ({EventsGraphNavigator.Interaction.Entities}IdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceHasKey ({EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceIsInMessage ({EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (QueryTagInstanceUnaryNodeInfoType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1191, 12)
    _ElementMap = QueryTagInstanceUnaryNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceUnaryNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternNameContains ({EventsGraphNavigator.Interaction.Entities}PatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element PatternIdIs ({EventsGraphNavigator.Interaction.Entities}PatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element IdIs ({EventsGraphNavigator.Interaction.Entities}IdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceHasKey ({EventsGraphNavigator.Interaction.Entities}TagInstanceHasKey) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element TagInstanceIsInMessage ({EventsGraphNavigator.Interaction.Entities}TagInstanceIsInMessage) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceUnaryNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyAllNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyAllNodeInfoType (QueryTagInstanceKeyGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyAllNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyAllNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1210, 2)
    _ElementMap = QueryTagInstanceKeyGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyGroupNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValuePatternNameContains ({EventsGraphNavigator.Interaction.Entities}ValuePatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValuePatternIdIs ({EventsGraphNavigator.Interaction.Entities}ValuePatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValueContains ({EventsGraphNavigator.Interaction.Entities}ValueContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValueContainsTag ({EventsGraphNavigator.Interaction.Entities}ValueContainsTag) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element KeyIsInTagInstance ({EventsGraphNavigator.Interaction.Entities}KeyIsInTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element OrderIs ({EventsGraphNavigator.Interaction.Entities}OrderIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyAllNodeInfoType = QueryTagInstanceKeyAllNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyAllNodeInfoType', QueryTagInstanceKeyAllNodeInfoType)


# Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyAnyNodeInfoType with content type ELEMENT_ONLY
class QueryTagInstanceKeyAnyNodeInfoType (QueryTagInstanceKeyGroupNodeInfoType):
    """Complex type {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyAnyNodeInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QueryTagInstanceKeyAnyNodeInfoType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1217, 2)
    _ElementMap = QueryTagInstanceKeyGroupNodeInfoType._ElementMap.copy()
    _AttributeMap = QueryTagInstanceKeyGroupNodeInfoType._AttributeMap.copy()
    # Base type is QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValuePatternNameContains ({EventsGraphNavigator.Interaction.Entities}ValuePatternNameContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValuePatternIdIs ({EventsGraphNavigator.Interaction.Entities}ValuePatternIdIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValueContains ({EventsGraphNavigator.Interaction.Entities}ValueContains) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element ValueContainsTag ({EventsGraphNavigator.Interaction.Entities}ValueContainsTag) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element KeyIsInTagInstance ({EventsGraphNavigator.Interaction.Entities}KeyIsInTagInstance) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element OrderIs ({EventsGraphNavigator.Interaction.Entities}OrderIs) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element All ({EventsGraphNavigator.Interaction.Entities}All) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Element Any ({EventsGraphNavigator.Interaction.Entities}Any) inherited from {EventsGraphNavigator.Interaction.Entities}QueryTagInstanceKeyGroupNodeInfoType
    
    # Attribute Invert inherited from {EventsGraphNavigator.Interaction.Entities}QueryNodeInfoType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.QueryTagInstanceKeyAnyNodeInfoType = QueryTagInstanceKeyAnyNodeInfoType
Namespace.addCategoryObject('typeBinding', 'QueryTagInstanceKeyAnyNodeInfoType', QueryTagInstanceKeyAnyNodeInfoType)


EntityIds = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntityIds'), GuidsList, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 14, 2))
Namespace.addCategoryObject('elementBinding', EntityIds.name().localName(), EntityIds)

AnyEntities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnyEntities'), AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 16, 2))
Namespace.addCategoryObject('elementBinding', AnyEntities.name().localName(), AnyEntities)

SourceChangeKind = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceChangeKind'), SourceChangeKindType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 91, 2))
Namespace.addCategoryObject('elementBinding', SourceChangeKind.name().localName(), SourceChangeKind)

LogMessages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessages'), LogMessagesEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 487, 2))
Namespace.addCategoryObject('elementBinding', LogMessages.name().localName(), LogMessages)

TagInstances = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstances'), TagInstancesEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 543, 2))
Namespace.addCategoryObject('elementBinding', TagInstances.name().localName(), TagInstances)

RpcCommand = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RpcCommand'), RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 15, 2))
Namespace.addCategoryObject('elementBinding', RpcCommand.name().localName(), RpcCommand)

LogMessage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessage'), LogMessageEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 486, 2))
Namespace.addCategoryObject('elementBinding', LogMessage.name().localName(), LogMessage)

TagInstance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), TagInstanceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 542, 2))
Namespace.addCategoryObject('elementBinding', TagInstance.name().localName(), TagInstance)

SourceInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceInfo'), SourceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 92, 2))
Namespace.addCategoryObject('elementBinding', SourceInfo.name().localName(), SourceInfo)

TagPatternInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagPatternInfo'), TagPatternInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 229, 2))
Namespace.addCategoryObject('elementBinding', TagPatternInfo.name().localName(), TagPatternInfo)

LinePatternInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LinePatternInfo'), LinePatternInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 230, 2))
Namespace.addCategoryObject('elementBinding', LinePatternInfo.name().localName(), LinePatternInfo)

LogMessagesContainingTextFromSourceFixedQuery = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesContainingTextFromSourceFixedQuery'), LogMessagesContainingTextFromSourceQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 716, 2))
Namespace.addCategoryObject('elementBinding', LogMessagesContainingTextFromSourceFixedQuery.name().localName(), LogMessagesContainingTextFromSourceFixedQuery)

LogMessagesCustomQuery = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesCustomQuery'), LogMessagesCustomQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 739, 2))
Namespace.addCategoryObject('elementBinding', LogMessagesCustomQuery.name().localName(), LogMessagesCustomQuery)

LogMessagesFullTextQuery = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesFullTextQuery'), LogMessagesFullTextQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 740, 2))
Namespace.addCategoryObject('elementBinding', LogMessagesFullTextQuery.name().localName(), LogMessagesFullTextQuery)

TagInstancesCustomQuery = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstancesCustomQuery'), TagInstancesCustomQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 741, 2))
Namespace.addCategoryObject('elementBinding', TagInstancesCustomQuery.name().localName(), TagInstancesCustomQuery)

TaskEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaskEntity'), TaskEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1245, 2))
Namespace.addCategoryObject('elementBinding', TaskEntity.name().localName(), TaskEntity)

SourcesFolder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourcesFolder'), SourcesFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 89, 2))
Namespace.addCategoryObject('elementBinding', SourcesFolder.name().localName(), SourcesFolder)

SourcesSource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourcesSource'), SourcesSourceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 90, 2))
Namespace.addCategoryObject('elementBinding', SourcesSource.name().localName(), SourcesSource)

PatternsFolder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsFolder'), PatternsFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 224, 2))
Namespace.addCategoryObject('elementBinding', PatternsFolder.name().localName(), PatternsFolder)

PatternsRegex = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsRegex'), PatternsRegexPatternEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 225, 2))
Namespace.addCategoryObject('elementBinding', PatternsRegex.name().localName(), PatternsRegex)

PatternsTag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsTag'), PatternsTagPatternEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 226, 2))
Namespace.addCategoryObject('elementBinding', PatternsTag.name().localName(), PatternsTag)

PatternsLine = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsLine'), PatternsLinePatternEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 227, 2))
Namespace.addCategoryObject('elementBinding', PatternsLine.name().localName(), PatternsLine)



AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EntityIds'), GuidsList, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 14, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourcesFolder'), SourcesFolderEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 89, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourcesSource'), SourcesSourceEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 90, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceInfo'), SourceInfoType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 92, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsFolder'), PatternsFolderEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 224, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsRegex'), PatternsRegexPatternEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 225, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsTag'), PatternsTagPatternEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 226, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternsLine'), PatternsLinePatternEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 227, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagPatternInfo'), TagPatternInfoType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 229, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LinePatternInfo'), LinePatternInfoType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 230, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessage'), LogMessageEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 486, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessages'), LogMessagesEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 487, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), TagInstanceEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 542, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstances'), TagInstancesEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 543, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesContainingTextFromSourceFixedQuery'), LogMessagesContainingTextFromSourceQueryInfoType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 716, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesCustomQuery'), LogMessagesCustomQueryInfoType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 739, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstancesCustomQuery'), TagInstancesCustomQueryInfoType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 741, 2)))

AnyRootEntitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TaskEntity'), TaskEntityType, scope=AnyRootEntitiesType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1245, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 21, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EntityIds')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourcesFolder')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 33, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourcesSource')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 34, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceInfo')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 35, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternsFolder')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 37, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternsLine')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 38, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternsTag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 39, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternsRegex')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 40, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LinePatternInfo')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 41, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagPatternInfo')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 42, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogMessages')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 44, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 45, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstances')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 47, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 48, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesContainingTextFromSourceFixedQuery')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 50, 6))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogMessagesCustomQuery')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 52, 6))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstancesCustomQuery')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 53, 6))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnyRootEntitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TaskEntity')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 55, 6))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnyRootEntitiesType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Folder'), ReferenceEntityType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 113, 20)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 112, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Folder')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 113, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Source'), ReferenceEntityType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 124, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 123, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Source')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 124, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Source'), ReferenceEntityType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 146, 20)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 145, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Source')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 146, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




SourceFilterOptionsInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BaseFolders'), StringsList, scope=SourceFilterOptionsInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 187, 10)))

SourceFilterOptionsInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FilesWildcard'), StringsList, scope=SourceFilterOptionsInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 188, 10)))

SourceFilterOptionsInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FoldersWildcard'), StringsList, scope=SourceFilterOptionsInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 189, 10)))

SourceFilterOptionsInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExcludedFiles'), StringsList, scope=SourceFilterOptionsInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 190, 10)))

SourceFilterOptionsInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExcludedFolders'), StringsList, scope=SourceFilterOptionsInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 191, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourceFilterOptionsInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BaseFolders')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 187, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourceFilterOptionsInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FilesWildcard')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 188, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourceFilterOptionsInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FoldersWildcard')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 189, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourceFilterOptionsInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExcludedFiles')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 190, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SourceFilterOptionsInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExcludedFolders')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 191, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SourceFilterOptionsInfoType._Automaton = _BuildAutomaton_4()




SourcePostFilterActionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommandLine'), string, scope=SourcePostFilterActionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 201, 10)))

SourcePostFilterActionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubFilterSource'), ReferenceEntityType, scope=SourcePostFilterActionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 202, 10)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourcePostFilterActionInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommandLine')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 201, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SourcePostFilterActionInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubFilterSource')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 202, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SourcePostFilterActionInfoType._Automaton = _BuildAutomaton_5()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Folder'), ReferenceEntityType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 251, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 250, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Folder')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 251, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_6()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Regex'), ReferenceEntityType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 262, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 261, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Regex')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 262, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_7()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tag'), ReferenceEntityType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 273, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 272, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 273, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_8()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Line'), ReferenceEntityType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 284, 20)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 283, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Line')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 284, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_9()




LogMessagesEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LogMessage'), LogMessageEntityType, scope=LogMessagesEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 494, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 493, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LogMessagesEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LogMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 494, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LogMessagesEntityType._Automaton = _BuildAutomaton_10()




LogMessageTagEntriesInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagEntry'), LogMessageTagEntryInfoType, scope=LogMessageTagEntriesInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 519, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 518, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LogMessageTagEntriesInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagEntry')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 519, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LogMessageTagEntriesInfoType._Automaton = _BuildAutomaton_11()




LogMessageTagEntryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), ReferenceEntityType, scope=LogMessageTagEntryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 530, 10)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogMessageTagEntryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 530, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogMessageTagEntryInfoType._Automaton = _BuildAutomaton_12()




TagInstancesEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), TagInstanceEntityType, scope=TagInstancesEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 550, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 549, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagInstancesEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 550, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TagInstancesEntityType._Automaton = _BuildAutomaton_13()




TagInstanceKeysInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Key'), TagInstanceKeyInfoType, scope=TagInstanceKeysInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 574, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 573, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeysInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Key')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 574, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TagInstanceKeysInfoType._Automaton = _BuildAutomaton_14()




TagInstanceKeyInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuePattern'), ReferenceEntityType, scope=TagInstanceKeyInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 585, 10)))

TagInstanceKeyInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlainValue'), TagInstanceKeyPlainValueInfoType, scope=TagInstanceKeyInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 587, 12)))

TagInstanceKeyInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplexValue'), TagInstanceKeyComplexValueInfoType, scope=TagInstanceKeyInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 588, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 585, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlainValue')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 587, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComplexValue')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 588, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagInstanceKeyInfoType._Automaton = _BuildAutomaton_15()




TagInstanceEntriesInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Entry'), TagInstanceEntryInfoType, scope=TagInstanceEntriesInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 638, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 637, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagInstanceEntriesInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Entry')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 638, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TagInstanceEntriesInfoType._Automaton = _BuildAutomaton_16()




TagInstanceEntryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Message'), ReferenceEntityType, scope=TagInstanceEntryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 649, 10)))

TagInstanceEntryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Source'), ReferenceEntityType, scope=TagInstanceEntryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 650, 10)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TagInstanceEntryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Message')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 649, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceEntryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Source')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 650, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagInstanceEntryInfoType._Automaton = _BuildAutomaton_17()




NumberMatchingSpecInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.double, scope=NumberMatchingSpecInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1233, 10)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NumberMatchingSpecInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1233, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NumberMatchingSpecInfoType._Automaton = _BuildAutomaton_18()




StringsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Item'), string, scope=StringsList, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1278, 10)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1277, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StringsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Item')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1278, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StringsList._Automaton = _BuildAutomaton_19()




GuidsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Item'), CTD_ANON_9, scope=GuidsList, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1288, 10)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1287, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GuidsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Item')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1288, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GuidsList._Automaton = _BuildAutomaton_20()




RpcCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Call'), RpcCallCommandInfoType, scope=RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 33, 10)))

RpcCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Result'), RpcResultCommandInfoType, scope=RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 34, 10)))

RpcCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Release'), RpcReleaseCommandInfoType, scope=RpcCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 35, 10)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Call')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 33, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Result')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 34, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Release')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 35, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcCommandInfoType._Automaton = _BuildAutomaton_21()




RpcSharedObjectKeyInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), string, scope=RpcSharedObjectKeyInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 90, 10)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcSharedObjectKeyInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 90, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcSharedObjectKeyInfoType._Automaton = _BuildAutomaton_22()




RpcMethodReferencInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GenericSignatureTypes'), RpcMethodReferenceGenericTypesInfoType, scope=RpcMethodReferencInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcMethodReferencInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GenericSignatureTypes')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 100, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RpcMethodReferencInfoType._Automaton = _BuildAutomaton_23()




RpcMethodReferenceGenericTypesInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TypeName'), string, scope=RpcMethodReferenceGenericTypesInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcMethodReferenceGenericTypesInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TypeName')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 113, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RpcMethodReferenceGenericTypesInfoType._Automaton = _BuildAutomaton_24()




RpcValueContainersListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), RpcValueContainerType, scope=RpcValueContainersListType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 123, 10)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 122, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcValueContainersListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 123, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RpcValueContainersListType._Automaton = _BuildAutomaton_25()




RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Instance'), BaseType, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 134, 12)))

RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'String'), string, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 135, 12)))

RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Int32'), int, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 136, 12)))

RpcValueContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Boolean'), bool, scope=RpcValueContainerType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 137, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Instance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 134, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'String')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 135, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Int32')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 136, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcValueContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Boolean')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 137, 12))
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
RpcValueContainerType._Automaton = _BuildAutomaton_26()




RpcExceptionDescriptionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Message'), string, scope=RpcExceptionDescriptionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 148, 10)))

RpcExceptionDescriptionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StackTrace'), string, scope=RpcExceptionDescriptionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 149, 10)))

RpcExceptionDescriptionInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InnerException'), RpcExceptionDescriptionInfoType, scope=RpcExceptionDescriptionInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcExceptionDescriptionInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Message')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 148, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcExceptionDescriptionInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StackTrace')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 149, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RpcExceptionDescriptionInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InnerException')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 150, 10))
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
RpcExceptionDescriptionInfoType._Automaton = _BuildAutomaton_27()




RpcRemoteObjectReferenceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId'), RpcSharedObjectKeyInfoType, scope=RpcRemoteObjectReferenceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 160, 10)))

RpcRemoteObjectReferenceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterfaceTypes'), CTD_ANON_7, scope=RpcRemoteObjectReferenceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 161, 10)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcRemoteObjectReferenceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 160, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcRemoteObjectReferenceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterfaceTypes')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 161, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcRemoteObjectReferenceInfoType._Automaton = _BuildAutomaton_28()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Type'), string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 166, 20)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 165, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Type')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 166, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_29()




TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), TagModelTextNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12)))

TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pattern'), TagModelPatternNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12)))

TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Alternatives'), TagModelAlternativesNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12)))

TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sequence'), TagModelSequenceNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12)))

TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Number'), TagModelNumberNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12)))

TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contains'), TagModelContainsNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12)))

TagModelUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotContains'), TagModelNotContainsNodeInfoType, scope=TagModelUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelUnaryNodeInfoType._Automaton = _BuildAutomaton_30()




TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), TagModelTextNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 403, 12)))

TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pattern'), TagModelPatternNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 404, 12)))

TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Alternatives'), TagModelAlternativesNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 405, 12)))

TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sequence'), TagModelSequenceNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 406, 12)))

TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Number'), TagModelNumberNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 407, 12)))

TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contains'), TagModelContainsNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 408, 12)))

TagModelGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NotContains'), TagModelNotContainsNodeInfoType, scope=TagModelGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 409, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 402, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 406, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 407, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 408, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 409, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelGroupNodeInfoType._Automaton = _BuildAutomaton_31()




LogMessageEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Source'), ReferenceEntityType, scope=LogMessageEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 505, 10)))

LogMessageEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), string, scope=LogMessageEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 506, 10)))

LogMessageEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagEntries'), LogMessageTagEntriesInfoType, scope=LogMessageEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 507, 10)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 507, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogMessageEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Source')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 505, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogMessageEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 506, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LogMessageEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagEntries')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 507, 10))
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
LogMessageEntityType._Automaton = _BuildAutomaton_32()




TagInstanceEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagPattern'), ReferenceEntityType, scope=TagInstanceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 561, 10)))

TagInstanceEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Keys'), TagInstanceKeysInfoType, scope=TagInstanceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 562, 10)))

TagInstanceEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Entries'), TagInstanceEntriesInfoType, scope=TagInstanceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 563, 10)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TagInstanceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagPattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 561, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TagInstanceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Keys')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 562, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Entries')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 563, 10))
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
TagInstanceEntityType._Automaton = _BuildAutomaton_33()




TagInstanceKeyPlainValueInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'String'), string, scope=TagInstanceKeyPlainValueInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 610, 12)))

TagInstanceKeyPlainValueInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Integer'), int, scope=TagInstanceKeyPlainValueInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 611, 12)))

TagInstanceKeyPlainValueInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DateTime'), DateTime, scope=TagInstanceKeyPlainValueInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 612, 12)))

TagInstanceKeyPlainValueInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Decimal'), pyxb.binding.datatypes.decimal, scope=TagInstanceKeyPlainValueInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 613, 12)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyPlainValueInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'String')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 610, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyPlainValueInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Integer')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 611, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyPlainValueInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DateTime')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 612, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyPlainValueInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Decimal')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 613, 12))
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
TagInstanceKeyPlainValueInfoType._Automaton = _BuildAutomaton_34()




TagInstanceKeyComplexValueInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstance'), ReferenceEntityType, scope=TagInstanceKeyComplexValueInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 626, 12)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstanceKeyComplexValueInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 626, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagInstanceKeyComplexValueInfoType._Automaton = _BuildAutomaton_35()




StringMatchingSpecInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pattern'), string, scope=StringMatchingSpecInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 667, 10)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringMatchingSpecInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 667, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StringMatchingSpecInfoType._Automaton = _BuildAutomaton_36()




RpcCallCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId'), RpcSharedObjectKeyInfoType, scope=RpcCallCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 54, 10)))

RpcCallCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MethodId'), RpcMethodReferencInfoType, scope=RpcCallCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 55, 10)))

RpcCallCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Arguments'), RpcValueContainersListType, scope=RpcCallCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 56, 10)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcCallCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 54, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcCallCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MethodId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 55, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcCallCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Arguments')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 56, 10))
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
RpcCallCommandInfoType._Automaton = _BuildAutomaton_37()




RpcResultCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReturnValue'), RpcValueContainerType, scope=RpcResultCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 67, 10)))

RpcResultCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutArguments'), RpcValueContainersListType, scope=RpcResultCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 68, 10)))

RpcResultCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Exception'), RpcExceptionDescriptionInfoType, scope=RpcResultCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 69, 10)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcResultCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReturnValue')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 67, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RpcResultCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutArguments')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 68, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcResultCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Exception')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 69, 10))
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
RpcResultCommandInfoType._Automaton = _BuildAutomaton_38()




RpcReleaseCommandInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId'), RpcSharedObjectKeyInfoType, scope=RpcReleaseCommandInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 80, 10)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RpcReleaseCommandInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RemoteInstanceId')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Channel.xsd', 80, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RpcReleaseCommandInfoType._Automaton = _BuildAutomaton_39()




SourcesItemBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), string, scope=SourcesItemBaseType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 98, 10)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SourcesItemBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 98, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SourcesItemBaseType._Automaton = _BuildAutomaton_40()




SourceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlOptions'), SourceControlOptionsInfoType, scope=SourceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 161, 10)))

SourceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FilterOptions'), SourceFilterOptionsInfoType, scope=SourceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 162, 10)))

SourceInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostFilterAction'), SourcePostFilterActionInfoType, scope=SourceInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 163, 10)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlOptions')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 161, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FilterOptions')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 162, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SourceInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostFilterAction')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 163, 10))
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
SourceInfoType._Automaton = _BuildAutomaton_41()




PatternsItemBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), string, scope=PatternsItemBaseType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PatternsItemBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PatternsItemBaseType._Automaton = _BuildAutomaton_42()




TagPatternInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_10, scope=TagPatternInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagPatternInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TagPatternInfoType._Automaton = _BuildAutomaton_43()




LinePatternInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_10, scope=LinePatternInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LinePatternInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LinePatternInfoType._Automaton = _BuildAutomaton_44()




def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_45()




def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 402, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 406, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 407, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 408, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelAlternativesNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 409, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelAlternativesNodeInfoType._Automaton = _BuildAutomaton_46()




def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 402, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 406, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 407, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 408, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TagModelSequenceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 409, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelSequenceNodeInfoType._Automaton = _BuildAutomaton_47()




def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNumberNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelNumberNodeInfoType._Automaton = _BuildAutomaton_48()




def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelContainsNodeInfoType._Automaton = _BuildAutomaton_49()




def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 384, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pattern')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 385, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Alternatives')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 386, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sequence')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 387, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 388, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 389, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagModelNotContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NotContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 390, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagModelNotContainsNodeInfoType._Automaton = _BuildAutomaton_50()




LogMessagesContainingTextFromSourceQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Source'), CTD_ANON_8, scope=LogMessagesContainingTextFromSourceQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 722, 10)))

LogMessagesContainingTextFromSourceQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), StringMatchingSpecInfoType, scope=LogMessagesContainingTextFromSourceQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 729, 10)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogMessagesContainingTextFromSourceQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Source')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 722, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogMessagesContainingTextFromSourceQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 729, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogMessagesContainingTextFromSourceQueryInfoType._Automaton = _BuildAutomaton_51()




LogMessagesCustomQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncludeObsoleteSources'), bool, scope=LogMessagesCustomQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 747, 10)))

LogMessagesCustomQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_11, scope=LogMessagesCustomQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 748, 10)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogMessagesCustomQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncludeObsoleteSources')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 747, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogMessagesCustomQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 748, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogMessagesCustomQueryInfoType._Automaton = _BuildAutomaton_52()




LogMessagesFullTextQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncludeObsoleteSources'), bool, scope=LogMessagesFullTextQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 764, 10)))

LogMessagesFullTextQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryString'), string, scope=LogMessagesFullTextQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 765, 10)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LogMessagesFullTextQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncludeObsoleteSources')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 764, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogMessagesFullTextQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QueryString')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 765, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogMessagesFullTextQueryInfoType._Automaton = _BuildAutomaton_53()




TagInstancesCustomQueryInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_12, scope=TagInstancesCustomQueryInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 775, 10)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TagInstancesCustomQueryInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 775, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TagInstancesCustomQueryInfoType._Automaton = _BuildAutomaton_54()




QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TextContains'), QueryLogMessageTextContainsNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 814, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs'), QueryLogMessageLineNumberIsNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 815, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains'), QueryLogMessageSourceNameContainsNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 816, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs'), QueryLogMessageSourceIdIsNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 817, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage'), QueryLogMessageSourceHasMessageNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 818, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance'), QueryLogMessageHasTagInstanceNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 819, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'All'), QueryLogMessageAllNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 820, 12)))

QueryLogMessageUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), QueryLogMessageAnyNodeInfoType, scope=QueryLogMessageUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 821, 12)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 814, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 815, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 816, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 817, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 818, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 819, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 820, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 821, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageUnaryNodeInfoType._Automaton = _BuildAutomaton_55()




QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TextContains'), QueryLogMessageTextContainsNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 834, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs'), QueryLogMessageLineNumberIsNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 835, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains'), QueryLogMessageSourceNameContainsNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 836, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs'), QueryLogMessageSourceIdIsNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 837, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage'), QueryLogMessageSourceHasMessageNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 838, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance'), QueryLogMessageHasTagInstanceNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 839, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'All'), QueryLogMessageAllNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 840, 12)))

QueryLogMessageGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), QueryLogMessageAnyNodeInfoType, scope=QueryLogMessageGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 841, 12)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 833, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 834, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 835, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 836, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 837, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 838, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 839, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 840, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 841, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageGroupNodeInfoType._Automaton = _BuildAutomaton_56()




QueryLogMessageTextContainsNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), StringMatchingSpecInfoType, scope=QueryLogMessageTextContainsNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 865, 10)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageTextContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 865, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageTextContainsNodeInfoType._Automaton = _BuildAutomaton_57()




QueryLogMessageLineNumberIsNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), NumberMatchingSpecInfoType, scope=QueryLogMessageLineNumberIsNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 875, 10)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageLineNumberIsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 875, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageLineNumberIsNodeInfoType._Automaton = _BuildAutomaton_58()




QueryLogMessageSourceNameContainsNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), StringMatchingSpecInfoType, scope=QueryLogMessageSourceNameContainsNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 885, 10)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageSourceNameContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 885, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageSourceNameContainsNodeInfoType._Automaton = _BuildAutomaton_59()




QueryLogMessageSourceHasMessageNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Where'), CTD_ANON_13, scope=QueryLogMessageSourceHasMessageNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 903, 10)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageSourceHasMessageNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Where')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 903, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageSourceHasMessageNodeInfoType._Automaton = _BuildAutomaton_60()




QueryLogMessageHasTagInstanceNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Where'), CTD_ANON_14, scope=QueryLogMessageHasTagInstanceNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 919, 10)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageHasTagInstanceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Where')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 919, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageHasTagInstanceNodeInfoType._Automaton = _BuildAutomaton_61()




QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains'), QueryTagInstancePatternNameContainsNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12)))

QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs'), QueryTagInstancePatternIdIsNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12)))

QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdIs'), QueryTagInstanceIdIsNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12)))

QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey'), QueryTagInstanceHasKeyNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12)))

QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage'), QueryTagInstanceIsInMessageNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12)))

QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'All'), QueryTagInstanceAllNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12)))

QueryTagInstanceUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), QueryTagInstanceAnyNodeInfoType, scope=QueryTagInstanceUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceUnaryNodeInfoType._Automaton = _BuildAutomaton_62()




QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains'), QueryTagInstancePatternNameContainsNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 981, 12)))

QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs'), QueryTagInstancePatternIdIsNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 982, 12)))

QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdIs'), QueryTagInstanceIdIsNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 983, 12)))

QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey'), QueryTagInstanceHasKeyNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 984, 12)))

QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage'), QueryTagInstanceIsInMessageNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 985, 12)))

QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'All'), QueryTagInstanceAllNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 986, 12)))

QueryTagInstanceGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), QueryTagInstanceAnyNodeInfoType, scope=QueryTagInstanceGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 987, 12)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 980, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 981, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 982, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 983, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 984, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 985, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 986, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 987, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceGroupNodeInfoType._Automaton = _BuildAutomaton_63()




QueryTagInstancePatternNameContainsNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), StringMatchingSpecInfoType, scope=QueryTagInstancePatternNameContainsNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1010, 10)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstancePatternNameContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1010, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstancePatternNameContainsNodeInfoType._Automaton = _BuildAutomaton_64()




QueryTagInstanceIsInMessageNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Where'), CTD_ANON_15, scope=QueryTagInstanceIsInMessageNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1034, 10)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceIsInMessageNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Where')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1034, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceIsInMessageNodeInfoType._Automaton = _BuildAutomaton_65()




QueryTagInstanceHasKeyNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Where'), CTD_ANON_16, scope=QueryTagInstanceHasKeyNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1066, 10)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceHasKeyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Where')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1066, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceHasKeyNodeInfoType._Automaton = _BuildAutomaton_66()




QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains'), QueryTagInstanceKeyValuePatternNameContainsNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1095, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs'), QueryTagInstanceKeyValuePatternIdIsNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1096, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueContains'), QueryTagInstanceKeyValueContainsNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1097, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag'), QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1098, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance'), QueryTagInstanceKeyIsInTagInstanceNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1099, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrderIs'), QueryTagInstanceKeyOrderIsNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1100, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'All'), QueryTagInstanceKeyAllNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1101, 12)))

QueryTagInstanceKeyUnaryNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), QueryTagInstanceKeyAnyNodeInfoType, scope=QueryTagInstanceKeyUnaryNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1102, 12)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1095, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1096, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1097, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1098, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1099, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrderIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1100, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1101, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyUnaryNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1102, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyUnaryNodeInfoType._Automaton = _BuildAutomaton_67()




QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains'), QueryTagInstanceKeyValuePatternNameContainsNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1115, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs'), QueryTagInstanceKeyValuePatternIdIsNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1116, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueContains'), QueryTagInstanceKeyValueContainsNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1117, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag'), QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1118, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance'), QueryTagInstanceKeyIsInTagInstanceNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1119, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrderIs'), QueryTagInstanceKeyOrderIsNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1120, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'All'), QueryTagInstanceKeyAllNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1121, 12)))

QueryTagInstanceKeyGroupNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Any'), QueryTagInstanceKeyAnyNodeInfoType, scope=QueryTagInstanceKeyGroupNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1122, 12)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1114, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1115, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1116, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1117, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1118, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1119, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrderIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1120, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1121, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyGroupNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1122, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyGroupNodeInfoType._Automaton = _BuildAutomaton_68()




QueryTagInstanceKeyValuePatternNameContainsNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), StringMatchingSpecInfoType, scope=QueryTagInstanceKeyValuePatternNameContainsNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1146, 10)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyValuePatternNameContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1146, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyValuePatternNameContainsNodeInfoType._Automaton = _BuildAutomaton_69()




QueryTagInstanceKeyValueContainsNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Text'), StringMatchingSpecInfoType, scope=QueryTagInstanceKeyValueContainsNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1156, 10)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyValueContainsNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Text')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1156, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyValueContainsNodeInfoType._Automaton = _BuildAutomaton_70()




QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Where'), CTD_ANON_17, scope=QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1166, 10)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Where')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1166, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyValueContainsTagInstanceNodeInfoType._Automaton = _BuildAutomaton_71()




QueryTagInstanceKeyIsInTagInstanceNodeInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Where'), CTD_ANON_18, scope=QueryTagInstanceKeyIsInTagInstanceNodeInfoType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1190, 10)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyIsInTagInstanceNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Where')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1190, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyIsInTagInstanceNodeInfoType._Automaton = _BuildAutomaton_72()




TaskEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), string, scope=TaskEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1251, 10)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TaskEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1251, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TaskEntityType._Automaton = _BuildAutomaton_73()




SourcesFolderEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChildFolders'), CTD_ANON, scope=SourcesFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 108, 10)))

SourcesFolderEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChildSources'), CTD_ANON_, scope=SourcesFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 119, 10)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourcesFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 98, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourcesFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChildFolders')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 108, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SourcesFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChildSources')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 119, 10))
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
SourcesFolderEntityType._Automaton = _BuildAutomaton_74()




SourcesSourceEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IsObsolete'), bool, scope=SourcesSourceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 139, 10)))

SourcesSourceEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlOptions'), SourceControlOptionsInfoType, scope=SourcesSourceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 140, 10)))

SourcesSourceEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Childs'), CTD_ANON_2, scope=SourcesSourceEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 141, 10)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourcesSourceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 98, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourcesSourceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IsObsolete')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 139, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SourcesSourceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlOptions')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 140, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SourcesSourceEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Childs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 141, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SourcesSourceEntityType._Automaton = _BuildAutomaton_75()




PatternsFolderEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChildFolders'), CTD_ANON_3, scope=PatternsFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 246, 10)))

PatternsFolderEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChildRegexPatterns'), CTD_ANON_4, scope=PatternsFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 257, 10)))

PatternsFolderEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChildTagPatterns'), CTD_ANON_5, scope=PatternsFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 268, 10)))

PatternsFolderEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChildLinePatterns'), CTD_ANON_6, scope=PatternsFolderEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 279, 10)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PatternsFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PatternsFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChildFolders')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 246, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PatternsFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChildRegexPatterns')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 257, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PatternsFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChildTagPatterns')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 268, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PatternsFolderEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChildLinePatterns')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 279, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PatternsFolderEntityType._Automaton = _BuildAutomaton_76()




PatternsRegexPatternEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Expression'), string, scope=PatternsRegexPatternEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 299, 10)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PatternsRegexPatternEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PatternsRegexPatternEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Expression')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 299, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PatternsRegexPatternEntityType._Automaton = _BuildAutomaton_77()




PatternsTagPatternEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_10, scope=PatternsTagPatternEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PatternsTagPatternEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PatternsTagPatternEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PatternsTagPatternEntityType._Automaton = _BuildAutomaton_78()




PatternsLinePatternEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_10, scope=PatternsLinePatternEntityType, location=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PatternsLinePatternEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 236, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PatternsLinePatternEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 351, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PatternsLinePatternEntityType._Automaton = _BuildAutomaton_79()




def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 814, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 815, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 816, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 817, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 818, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 819, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 820, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 821, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_80()




def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_81()




def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 814, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 815, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 816, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 817, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 818, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 819, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 820, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 821, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_82()




def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_83()




def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 833, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 834, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 835, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 836, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 837, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 838, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 839, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 840, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 841, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageAllNodeInfoType._Automaton = _BuildAutomaton_84()




def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 833, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 834, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 835, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 836, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 837, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 838, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 839, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 840, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryLogMessageAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 841, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryLogMessageAnyNodeInfoType._Automaton = _BuildAutomaton_85()




def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 980, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 981, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 982, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 983, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 984, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 985, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 986, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 987, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceAllNodeInfoType._Automaton = _BuildAutomaton_86()




def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 980, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 981, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 982, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 983, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 984, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 985, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 986, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 987, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceAnyNodeInfoType._Automaton = _BuildAutomaton_87()




def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TextContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 814, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineNumberIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 815, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 816, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 817, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceHasMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 818, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MessageHasTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 819, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 820, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 821, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_88()




def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1095, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1096, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1097, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1098, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1099, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrderIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1100, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1101, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1102, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_89()




def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_90()




def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 962, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 963, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 964, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceHasKey')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 965, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TagInstanceIsInMessage')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 966, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 967, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 968, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_91()




def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1114, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1115, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1116, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1117, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1118, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1119, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrderIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1120, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1121, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAllNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1122, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyAllNodeInfoType._Automaton = _BuildAutomaton_92()




def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1114, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternNameContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1115, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValuePatternIdIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1116, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContains')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1117, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueContainsTag')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1118, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyIsInTagInstance')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1119, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrderIs')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1120, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'All')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1121, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QueryTagInstanceKeyAnyNodeInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Any')), pyxb.utils.utility.Location('/Users/thepowerfuldeez/Dropbox/Study/ifmo_labworks/informatics_1sem/Entities.xsd', 1122, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QueryTagInstanceKeyAnyNodeInfoType._Automaton = _BuildAutomaton_93()

