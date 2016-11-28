# ./schema_curitiba.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9ba128ee7a18904e1e4aaf2a1fb2c1125650aa5c
# Generated 2016-11-27 20:29:26.553074 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f41c9a26-b4f0-11e6-9ca1-406c8f42f6c5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from . import _dsig as _ImportedBinding__dsig
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dsig = _ImportedBinding__dsig.Namespace
_Namespace_dsig.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNumeroNfse
class tsNumeroNfse (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNumeroNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 11, 4)
    _Documentation = None
tsNumeroNfse._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tsNumeroNfse._InitializeFacetMap(tsNumeroNfse._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tsNumeroNfse', tsNumeroNfse)
_module_typeBindings.tsNumeroNfse = tsNumeroNfse

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoVerificacao
class tsCodigoVerificacao (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoVerificacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 16, 1)
    _Documentation = None
tsCodigoVerificacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsCodigoVerificacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsCodigoVerificacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
tsCodigoVerificacao._InitializeFacetMap(tsCodigoVerificacao._CF_whiteSpace,
   tsCodigoVerificacao._CF_minLength,
   tsCodigoVerificacao._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsCodigoVerificacao', tsCodigoVerificacao)
_module_typeBindings.tsCodigoVerificacao = tsCodigoVerificacao

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsStatusRps
class tsStatusRps (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsStatusRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 23, 1)
    _Documentation = None
tsStatusRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsStatusRps._CF_pattern.addPattern(pattern='1|2')
tsStatusRps._InitializeFacetMap(tsStatusRps._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsStatusRps', tsStatusRps)
_module_typeBindings.tsStatusRps = tsStatusRps

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsStatusNfse
class tsStatusNfse (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsStatusNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 28, 1)
    _Documentation = None
tsStatusNfse._CF_pattern = pyxb.binding.facets.CF_pattern()
tsStatusNfse._CF_pattern.addPattern(pattern='1|2')
tsStatusNfse._InitializeFacetMap(tsStatusNfse._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsStatusNfse', tsStatusNfse)
_module_typeBindings.tsStatusNfse = tsStatusNfse

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNaturezaOperacao
class tsNaturezaOperacao (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNaturezaOperacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 33, 1)
    _Documentation = None
tsNaturezaOperacao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsNaturezaOperacao._CF_pattern.addPattern(pattern='1|2|3|4|5|6')
tsNaturezaOperacao._InitializeFacetMap(tsNaturezaOperacao._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsNaturezaOperacao', tsNaturezaOperacao)
_module_typeBindings.tsNaturezaOperacao = tsNaturezaOperacao

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsRegimeEspecialTributacao
class tsRegimeEspecialTributacao (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsRegimeEspecialTributacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 38, 1)
    _Documentation = None
tsRegimeEspecialTributacao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsRegimeEspecialTributacao._CF_pattern.addPattern(pattern='1|2|3|4|5|6')
tsRegimeEspecialTributacao._InitializeFacetMap(tsRegimeEspecialTributacao._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsRegimeEspecialTributacao', tsRegimeEspecialTributacao)
_module_typeBindings.tsRegimeEspecialTributacao = tsRegimeEspecialTributacao

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsSimNao
class tsSimNao (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsSimNao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 43, 1)
    _Documentation = None
tsSimNao._CF_pattern = pyxb.binding.facets.CF_pattern()
tsSimNao._CF_pattern.addPattern(pattern='1|2')
tsSimNao._InitializeFacetMap(tsSimNao._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsSimNao', tsSimNao)
_module_typeBindings.tsSimNao = tsSimNao

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNumeroRps
class tsNumeroRps (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNumeroRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 48, 1)
    _Documentation = None
tsNumeroRps._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tsNumeroRps._InitializeFacetMap(tsNumeroRps._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tsNumeroRps', tsNumeroRps)
_module_typeBindings.tsNumeroRps = tsNumeroRps

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsSerieRps
class tsSerieRps (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsSerieRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 53, 1)
    _Documentation = None
tsSerieRps._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsSerieRps._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsSerieRps._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
tsSerieRps._InitializeFacetMap(tsSerieRps._CF_whiteSpace,
   tsSerieRps._CF_minLength,
   tsSerieRps._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsSerieRps', tsSerieRps)
_module_typeBindings.tsSerieRps = tsSerieRps

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsTipoRps
class tsTipoRps (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsTipoRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 60, 1)
    _Documentation = None
tsTipoRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsTipoRps._CF_pattern.addPattern(pattern='1|2|3')
tsTipoRps._InitializeFacetMap(tsTipoRps._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsTipoRps', tsTipoRps)
_module_typeBindings.tsTipoRps = tsTipoRps

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsOutrasInformacoes
class tsOutrasInformacoes (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsOutrasInformacoes')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 65, 1)
    _Documentation = None
tsOutrasInformacoes._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsOutrasInformacoes._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsOutrasInformacoes._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
tsOutrasInformacoes._InitializeFacetMap(tsOutrasInformacoes._CF_whiteSpace,
   tsOutrasInformacoes._CF_minLength,
   tsOutrasInformacoes._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsOutrasInformacoes', tsOutrasInformacoes)
_module_typeBindings.tsOutrasInformacoes = tsOutrasInformacoes

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsValor
class tsValor (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsValor')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 72, 1)
    _Documentation = None
tsValor._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tsValor._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tsValor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.decimal('0.0'), value_datatype=tsValor)
tsValor._InitializeFacetMap(tsValor._CF_fractionDigits,
   tsValor._CF_totalDigits,
   tsValor._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'tsValor', tsValor)
_module_typeBindings.tsValor = tsValor

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsItemListaServico
class tsItemListaServico (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsItemListaServico')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 79, 1)
    _Documentation = None
tsItemListaServico._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsItemListaServico._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsItemListaServico._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
tsItemListaServico._InitializeFacetMap(tsItemListaServico._CF_whiteSpace,
   tsItemListaServico._CF_minLength,
   tsItemListaServico._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsItemListaServico', tsItemListaServico)
_module_typeBindings.tsItemListaServico = tsItemListaServico

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoCnae
class tsCodigoCnae (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoCnae')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 86, 1)
    _Documentation = None
tsCodigoCnae._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(7))
tsCodigoCnae._InitializeFacetMap(tsCodigoCnae._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tsCodigoCnae', tsCodigoCnae)
_module_typeBindings.tsCodigoCnae = tsCodigoCnae

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoTributacao
class tsCodigoTributacao (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoTributacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 91, 1)
    _Documentation = None
tsCodigoTributacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsCodigoTributacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsCodigoTributacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
tsCodigoTributacao._InitializeFacetMap(tsCodigoTributacao._CF_whiteSpace,
   tsCodigoTributacao._CF_minLength,
   tsCodigoTributacao._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsCodigoTributacao', tsCodigoTributacao)
_module_typeBindings.tsCodigoTributacao = tsCodigoTributacao

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsAliquota
class tsAliquota (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsAliquota')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 98, 1)
    _Documentation = None
tsAliquota._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tsAliquota._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5))
tsAliquota._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.decimal('0.0'), value_datatype=tsAliquota)
tsAliquota._InitializeFacetMap(tsAliquota._CF_fractionDigits,
   tsAliquota._CF_totalDigits,
   tsAliquota._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'tsAliquota', tsAliquota)
_module_typeBindings.tsAliquota = tsAliquota

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsDiscriminacao
class tsDiscriminacao (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsDiscriminacao')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 105, 1)
    _Documentation = None
tsDiscriminacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsDiscriminacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsDiscriminacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
tsDiscriminacao._InitializeFacetMap(tsDiscriminacao._CF_whiteSpace,
   tsDiscriminacao._CF_minLength,
   tsDiscriminacao._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsDiscriminacao', tsDiscriminacao)
_module_typeBindings.tsDiscriminacao = tsDiscriminacao

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoMunicipioIbge
class tsCodigoMunicipioIbge (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoMunicipioIbge')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 112, 1)
    _Documentation = None
tsCodigoMunicipioIbge._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(7))
tsCodigoMunicipioIbge._InitializeFacetMap(tsCodigoMunicipioIbge._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tsCodigoMunicipioIbge', tsCodigoMunicipioIbge)
_module_typeBindings.tsCodigoMunicipioIbge = tsCodigoMunicipioIbge

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsInscricaoMunicipal
class tsInscricaoMunicipal (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsInscricaoMunicipal')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 117, 1)
    _Documentation = None
tsInscricaoMunicipal._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsInscricaoMunicipal._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsInscricaoMunicipal._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
tsInscricaoMunicipal._InitializeFacetMap(tsInscricaoMunicipal._CF_whiteSpace,
   tsInscricaoMunicipal._CF_minLength,
   tsInscricaoMunicipal._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsInscricaoMunicipal', tsInscricaoMunicipal)
_module_typeBindings.tsInscricaoMunicipal = tsInscricaoMunicipal

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsRazaoSocial
class tsRazaoSocial (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsRazaoSocial')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 124, 1)
    _Documentation = None
tsRazaoSocial._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsRazaoSocial._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsRazaoSocial._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(115))
tsRazaoSocial._InitializeFacetMap(tsRazaoSocial._CF_whiteSpace,
   tsRazaoSocial._CF_minLength,
   tsRazaoSocial._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsRazaoSocial', tsRazaoSocial)
_module_typeBindings.tsRazaoSocial = tsRazaoSocial

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNomeFantasia
class tsNomeFantasia (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNomeFantasia')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 131, 1)
    _Documentation = None
tsNomeFantasia._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsNomeFantasia._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsNomeFantasia._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
tsNomeFantasia._InitializeFacetMap(tsNomeFantasia._CF_whiteSpace,
   tsNomeFantasia._CF_minLength,
   tsNomeFantasia._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsNomeFantasia', tsNomeFantasia)
_module_typeBindings.tsNomeFantasia = tsNomeFantasia

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCnpj
class tsCnpj (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCnpj')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 138, 1)
    _Documentation = None
tsCnpj._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsCnpj._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(14))
tsCnpj._InitializeFacetMap(tsCnpj._CF_whiteSpace,
   tsCnpj._CF_length)
Namespace.addCategoryObject('typeBinding', 'tsCnpj', tsCnpj)
_module_typeBindings.tsCnpj = tsCnpj

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsEndereco
class tsEndereco (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 144, 1)
    _Documentation = None
tsEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(125))
tsEndereco._InitializeFacetMap(tsEndereco._CF_whiteSpace,
   tsEndereco._CF_minLength,
   tsEndereco._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsEndereco', tsEndereco)
_module_typeBindings.tsEndereco = tsEndereco

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNumeroEndereco
class tsNumeroEndereco (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNumeroEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 151, 1)
    _Documentation = None
tsNumeroEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsNumeroEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsNumeroEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
tsNumeroEndereco._InitializeFacetMap(tsNumeroEndereco._CF_whiteSpace,
   tsNumeroEndereco._CF_minLength,
   tsNumeroEndereco._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsNumeroEndereco', tsNumeroEndereco)
_module_typeBindings.tsNumeroEndereco = tsNumeroEndereco

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsComplementoEndereco
class tsComplementoEndereco (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsComplementoEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 158, 1)
    _Documentation = None
tsComplementoEndereco._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsComplementoEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsComplementoEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
tsComplementoEndereco._InitializeFacetMap(tsComplementoEndereco._CF_whiteSpace,
   tsComplementoEndereco._CF_minLength,
   tsComplementoEndereco._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsComplementoEndereco', tsComplementoEndereco)
_module_typeBindings.tsComplementoEndereco = tsComplementoEndereco

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsBairro
class tsBairro (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsBairro')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 165, 1)
    _Documentation = None
tsBairro._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsBairro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsBairro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
tsBairro._InitializeFacetMap(tsBairro._CF_whiteSpace,
   tsBairro._CF_minLength,
   tsBairro._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsBairro', tsBairro)
_module_typeBindings.tsBairro = tsBairro

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsUf
class tsUf (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsUf')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 172, 1)
    _Documentation = None
tsUf._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2))
tsUf._InitializeFacetMap(tsUf._CF_length)
Namespace.addCategoryObject('typeBinding', 'tsUf', tsUf)
_module_typeBindings.tsUf = tsUf

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCep
class tsCep (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCep')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 177, 1)
    _Documentation = None
tsCep._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(8))
tsCep._InitializeFacetMap(tsCep._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tsCep', tsCep)
_module_typeBindings.tsCep = tsCep

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsEmail
class tsEmail (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsEmail')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 182, 1)
    _Documentation = None
tsEmail._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsEmail._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsEmail._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(80))
tsEmail._InitializeFacetMap(tsEmail._CF_whiteSpace,
   tsEmail._CF_minLength,
   tsEmail._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsEmail', tsEmail)
_module_typeBindings.tsEmail = tsEmail

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsTelefone
class tsTelefone (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsTelefone')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 189, 1)
    _Documentation = None
tsTelefone._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsTelefone._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsTelefone._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(11))
tsTelefone._InitializeFacetMap(tsTelefone._CF_whiteSpace,
   tsTelefone._CF_minLength,
   tsTelefone._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsTelefone', tsTelefone)
_module_typeBindings.tsTelefone = tsTelefone

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCpf
class tsCpf (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCpf')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 196, 1)
    _Documentation = None
tsCpf._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(11))
tsCpf._InitializeFacetMap(tsCpf._CF_length)
Namespace.addCategoryObject('typeBinding', 'tsCpf', tsCpf)
_module_typeBindings.tsCpf = tsCpf

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsIndicacaoCpfCnpj
class tsIndicacaoCpfCnpj (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsIndicacaoCpfCnpj')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 201, 1)
    _Documentation = None
tsIndicacaoCpfCnpj._CF_pattern = pyxb.binding.facets.CF_pattern()
tsIndicacaoCpfCnpj._CF_pattern.addPattern(pattern='1|2|3')
tsIndicacaoCpfCnpj._InitializeFacetMap(tsIndicacaoCpfCnpj._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsIndicacaoCpfCnpj', tsIndicacaoCpfCnpj)
_module_typeBindings.tsIndicacaoCpfCnpj = tsIndicacaoCpfCnpj

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoObra
class tsCodigoObra (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoObra')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 206, 1)
    _Documentation = None
tsCodigoObra._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsCodigoObra._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsCodigoObra._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
tsCodigoObra._InitializeFacetMap(tsCodigoObra._CF_whiteSpace,
   tsCodigoObra._CF_minLength,
   tsCodigoObra._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsCodigoObra', tsCodigoObra)
_module_typeBindings.tsCodigoObra = tsCodigoObra

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsArt
class tsArt (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsArt')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 213, 1)
    _Documentation = None
tsArt._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsArt._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsArt._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
tsArt._InitializeFacetMap(tsArt._CF_whiteSpace,
   tsArt._CF_minLength,
   tsArt._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsArt', tsArt)
_module_typeBindings.tsArt = tsArt

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNumeroLote
class tsNumeroLote (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNumeroLote')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 220, 1)
    _Documentation = None
tsNumeroLote._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15))
tsNumeroLote._InitializeFacetMap(tsNumeroLote._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'tsNumeroLote', tsNumeroLote)
_module_typeBindings.tsNumeroLote = tsNumeroLote

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsNumeroProtocolo
class tsNumeroProtocolo (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsNumeroProtocolo')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 225, 1)
    _Documentation = None
tsNumeroProtocolo._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
tsNumeroProtocolo._InitializeFacetMap(tsNumeroProtocolo._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsNumeroProtocolo', tsNumeroProtocolo)
_module_typeBindings.tsNumeroProtocolo = tsNumeroProtocolo

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsSituacaoLoteRps
class tsSituacaoLoteRps (pyxb.binding.datatypes.byte):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsSituacaoLoteRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 230, 1)
    _Documentation = None
tsSituacaoLoteRps._CF_pattern = pyxb.binding.facets.CF_pattern()
tsSituacaoLoteRps._CF_pattern.addPattern(pattern='1|2|3|4')
tsSituacaoLoteRps._InitializeFacetMap(tsSituacaoLoteRps._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'tsSituacaoLoteRps', tsSituacaoLoteRps)
_module_typeBindings.tsSituacaoLoteRps = tsSituacaoLoteRps

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsQuantidadeRps
class tsQuantidadeRps (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsQuantidadeRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 235, 1)
    _Documentation = None
tsQuantidadeRps._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'tsQuantidadeRps', tsQuantidadeRps)
_module_typeBindings.tsQuantidadeRps = tsQuantidadeRps

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoMensagemAlerta
class tsCodigoMensagemAlerta (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoMensagemAlerta')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 239, 1)
    _Documentation = None
tsCodigoMensagemAlerta._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsCodigoMensagemAlerta._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsCodigoMensagemAlerta._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tsCodigoMensagemAlerta._InitializeFacetMap(tsCodigoMensagemAlerta._CF_whiteSpace,
   tsCodigoMensagemAlerta._CF_minLength,
   tsCodigoMensagemAlerta._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsCodigoMensagemAlerta', tsCodigoMensagemAlerta)
_module_typeBindings.tsCodigoMensagemAlerta = tsCodigoMensagemAlerta

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsDescricaoMensagemAlerta
class tsDescricaoMensagemAlerta (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsDescricaoMensagemAlerta')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 246, 1)
    _Documentation = None
tsDescricaoMensagemAlerta._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsDescricaoMensagemAlerta._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsDescricaoMensagemAlerta._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(200))
tsDescricaoMensagemAlerta._InitializeFacetMap(tsDescricaoMensagemAlerta._CF_whiteSpace,
   tsDescricaoMensagemAlerta._CF_minLength,
   tsDescricaoMensagemAlerta._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsDescricaoMensagemAlerta', tsDescricaoMensagemAlerta)
_module_typeBindings.tsDescricaoMensagemAlerta = tsDescricaoMensagemAlerta

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsCodigoCancelamentoNfse
class tsCodigoCancelamentoNfse (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsCodigoCancelamentoNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 253, 1)
    _Documentation = None
tsCodigoCancelamentoNfse._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
tsCodigoCancelamentoNfse._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
tsCodigoCancelamentoNfse._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
tsCodigoCancelamentoNfse._InitializeFacetMap(tsCodigoCancelamentoNfse._CF_whiteSpace,
   tsCodigoCancelamentoNfse._CF_minLength,
   tsCodigoCancelamentoNfse._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsCodigoCancelamentoNfse', tsCodigoCancelamentoNfse)
_module_typeBindings.tsCodigoCancelamentoNfse = tsCodigoCancelamentoNfse

# Atomic simple type: {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tsIdTag
class tsIdTag (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tsIdTag')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 260, 1)
    _Documentation = None
tsIdTag._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
tsIdTag._InitializeFacetMap(tsIdTag._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tsIdTag', tsIdTag)
_module_typeBindings.tsIdTag = tsIdTag

# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcCpfCnpj with content type ELEMENT_ONLY
class tcCpfCnpj (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcCpfCnpj with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcCpfCnpj')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 268, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cpf uses Python identifier Cpf
    __Cpf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cpf'), 'Cpf', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCpfCnpj_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCpf', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 270, 12), )

    
    Cpf = property(__Cpf.value, __Cpf.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), 'Cnpj', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCpfCnpj_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCnpj', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 271, 12), )

    
    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    _ElementMap.update({
        __Cpf.name() : __Cpf,
        __Cnpj.name() : __Cnpj
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcCpfCnpj = tcCpfCnpj
Namespace.addCategoryObject('typeBinding', 'tcCpfCnpj', tcCpfCnpj)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcEndereco with content type ELEMENT_ONLY
class tcEndereco (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcEndereco with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcEndereco')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 274, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Endereco'), 'Endereco', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdEndereco', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 276, 12), )

    
    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numero'), 'Numero', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumero', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 277, 12), )

    
    Numero = property(__Numero.value, __Numero.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Complemento uses Python identifier Complemento
    __Complemento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Complemento'), 'Complemento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdComplemento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 278, 12), )

    
    Complemento = property(__Complemento.value, __Complemento.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Bairro uses Python identifier Bairro
    __Bairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Bairro'), 'Bairro', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdBairro', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 279, 12), )

    
    Bairro = property(__Bairro.value, __Bairro.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), 'CodigoMunicipio', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoMunicipio', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 280, 12), )

    
    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Uf uses Python identifier Uf
    __Uf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Uf'), 'Uf', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdUf', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 281, 12), )

    
    Uf = property(__Uf.value, __Uf.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cep uses Python identifier Cep
    __Cep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cep'), 'Cep', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcEndereco_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCep', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 282, 12), )

    
    Cep = property(__Cep.value, __Cep.set, None, None)

    _ElementMap.update({
        __Endereco.name() : __Endereco,
        __Numero.name() : __Numero,
        __Complemento.name() : __Complemento,
        __Bairro.name() : __Bairro,
        __CodigoMunicipio.name() : __CodigoMunicipio,
        __Uf.name() : __Uf,
        __Cep.name() : __Cep
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcEndereco = tcEndereco
Namespace.addCategoryObject('typeBinding', 'tcEndereco', tcEndereco)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcContato with content type ELEMENT_ONLY
class tcContato (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcContato with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcContato')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 285, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Telefone uses Python identifier Telefone
    __Telefone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Telefone'), 'Telefone', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcContato_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdTelefone', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 287, 12), )

    
    Telefone = property(__Telefone.value, __Telefone.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Email'), 'Email', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcContato_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdEmail', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 288, 12), )

    
    Email = property(__Email.value, __Email.set, None, None)

    _ElementMap.update({
        __Telefone.name() : __Telefone,
        __Email.name() : __Email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcContato = tcContato
Namespace.addCategoryObject('typeBinding', 'tcContato', tcContato)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoOrgaoGerador with content type ELEMENT_ONLY
class tcIdentificacaoOrgaoGerador (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoOrgaoGerador with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcIdentificacaoOrgaoGerador')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 291, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), 'CodigoMunicipio', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoOrgaoGerador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoMunicipio', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 293, 12), )

    
    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Uf uses Python identifier Uf
    __Uf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Uf'), 'Uf', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoOrgaoGerador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdUf', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 294, 12), )

    
    Uf = property(__Uf.value, __Uf.set, None, None)

    _ElementMap.update({
        __CodigoMunicipio.name() : __CodigoMunicipio,
        __Uf.name() : __Uf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcIdentificacaoOrgaoGerador = tcIdentificacaoOrgaoGerador
Namespace.addCategoryObject('typeBinding', 'tcIdentificacaoOrgaoGerador', tcIdentificacaoOrgaoGerador)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoRps with content type ELEMENT_ONLY
class tcIdentificacaoRps (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoRps with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcIdentificacaoRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 297, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numero'), 'Numero', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumero', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 299, 12), )

    
    Numero = property(__Numero.value, __Numero.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Serie uses Python identifier Serie
    __Serie = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Serie'), 'Serie', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdSerie', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 300, 12), )

    
    Serie = property(__Serie.value, __Serie.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Tipo uses Python identifier Tipo
    __Tipo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tipo'), 'Tipo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdTipo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 301, 12), )

    
    Tipo = property(__Tipo.value, __Tipo.set, None, None)

    _ElementMap.update({
        __Numero.name() : __Numero,
        __Serie.name() : __Serie,
        __Tipo.name() : __Tipo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcIdentificacaoRps = tcIdentificacaoRps
Namespace.addCategoryObject('typeBinding', 'tcIdentificacaoRps', tcIdentificacaoRps)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoPrestador with content type ELEMENT_ONLY
class tcIdentificacaoPrestador (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoPrestador with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcIdentificacaoPrestador')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 304, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), 'Cnpj', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCnpj', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 306, 12), )

    
    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), 'InscricaoMunicipal', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInscricaoMunicipal', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 307, 12), )

    
    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update({
        __Cnpj.name() : __Cnpj,
        __InscricaoMunicipal.name() : __InscricaoMunicipal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcIdentificacaoPrestador = tcIdentificacaoPrestador
Namespace.addCategoryObject('typeBinding', 'tcIdentificacaoPrestador', tcIdentificacaoPrestador)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoTomador with content type ELEMENT_ONLY
class tcIdentificacaoTomador (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoTomador with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcIdentificacaoTomador')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 310, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CpfCnpj'), 'CpfCnpj', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoTomador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCpfCnpj', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 312, 12), )

    
    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), 'InscricaoMunicipal', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoTomador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInscricaoMunicipal', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 313, 12), )

    
    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update({
        __CpfCnpj.name() : __CpfCnpj,
        __InscricaoMunicipal.name() : __InscricaoMunicipal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcIdentificacaoTomador = tcIdentificacaoTomador
Namespace.addCategoryObject('typeBinding', 'tcIdentificacaoTomador', tcIdentificacaoTomador)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosTomador with content type ELEMENT_ONLY
class tcDadosTomador (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosTomador with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcDadosTomador')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 316, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoTomador uses Python identifier IdentificacaoTomador
    __IdentificacaoTomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoTomador'), 'IdentificacaoTomador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosTomador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoTomador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 318, 12), )

    
    IdentificacaoTomador = property(__IdentificacaoTomador.value, __IdentificacaoTomador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial'), 'RazaoSocial', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosTomador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRazaoSocial', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 319, 12), )

    
    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Endereco'), 'Endereco', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosTomador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdEndereco', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 320, 12), )

    
    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Contato uses Python identifier Contato
    __Contato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contato'), 'Contato', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosTomador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdContato', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 321, 12), )

    
    Contato = property(__Contato.value, __Contato.set, None, None)

    _ElementMap.update({
        __IdentificacaoTomador.name() : __IdentificacaoTomador,
        __RazaoSocial.name() : __RazaoSocial,
        __Endereco.name() : __Endereco,
        __Contato.name() : __Contato
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcDadosTomador = tcDadosTomador
Namespace.addCategoryObject('typeBinding', 'tcDadosTomador', tcDadosTomador)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoIntermediarioServico with content type ELEMENT_ONLY
class tcIdentificacaoIntermediarioServico (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoIntermediarioServico with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcIdentificacaoIntermediarioServico')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 324, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial'), 'RazaoSocial', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoIntermediarioServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRazaoSocial', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 326, 12), )

    
    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CpfCnpj uses Python identifier CpfCnpj
    __CpfCnpj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CpfCnpj'), 'CpfCnpj', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoIntermediarioServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCpfCnpj', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 327, 12), )

    
    CpfCnpj = property(__CpfCnpj.value, __CpfCnpj.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), 'InscricaoMunicipal', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoIntermediarioServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInscricaoMunicipal', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 328, 12), )

    
    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    _ElementMap.update({
        __RazaoSocial.name() : __RazaoSocial,
        __CpfCnpj.name() : __CpfCnpj,
        __InscricaoMunicipal.name() : __InscricaoMunicipal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcIdentificacaoIntermediarioServico = tcIdentificacaoIntermediarioServico
Namespace.addCategoryObject('typeBinding', 'tcIdentificacaoIntermediarioServico', tcIdentificacaoIntermediarioServico)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcValores with content type ELEMENT_ONLY
class tcValores (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcValores with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcValores')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 331, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorServicos uses Python identifier ValorServicos
    __ValorServicos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorServicos'), 'ValorServicos', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorServicos', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 333, 12), )

    
    ValorServicos = property(__ValorServicos.value, __ValorServicos.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorDeducoes uses Python identifier ValorDeducoes
    __ValorDeducoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorDeducoes'), 'ValorDeducoes', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorDeducoes', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 334, 12), )

    
    ValorDeducoes = property(__ValorDeducoes.value, __ValorDeducoes.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorPis uses Python identifier ValorPis
    __ValorPis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorPis'), 'ValorPis', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorPis', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 335, 12), )

    
    ValorPis = property(__ValorPis.value, __ValorPis.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorCofins uses Python identifier ValorCofins
    __ValorCofins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorCofins'), 'ValorCofins', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorCofins', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 336, 12), )

    
    ValorCofins = property(__ValorCofins.value, __ValorCofins.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorInss uses Python identifier ValorInss
    __ValorInss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorInss'), 'ValorInss', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorInss', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 337, 12), )

    
    ValorInss = property(__ValorInss.value, __ValorInss.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorIr uses Python identifier ValorIr
    __ValorIr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorIr'), 'ValorIr', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorIr', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 338, 12), )

    
    ValorIr = property(__ValorIr.value, __ValorIr.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorCsll uses Python identifier ValorCsll
    __ValorCsll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorCsll'), 'ValorCsll', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorCsll', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 339, 12), )

    
    ValorCsll = property(__ValorCsll.value, __ValorCsll.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IssRetido uses Python identifier IssRetido
    __IssRetido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IssRetido'), 'IssRetido', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIssRetido', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 340, 12), )

    
    IssRetido = property(__IssRetido.value, __IssRetido.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorIss uses Python identifier ValorIss
    __ValorIss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorIss'), 'ValorIss', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorIss', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 341, 12), )

    
    ValorIss = property(__ValorIss.value, __ValorIss.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorIssRetido uses Python identifier ValorIssRetido
    __ValorIssRetido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorIssRetido'), 'ValorIssRetido', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorIssRetido', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 342, 12), )

    
    ValorIssRetido = property(__ValorIssRetido.value, __ValorIssRetido.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}OutrasRetencoes uses Python identifier OutrasRetencoes
    __OutrasRetencoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutrasRetencoes'), 'OutrasRetencoes', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdOutrasRetencoes', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 343, 12), )

    
    OutrasRetencoes = property(__OutrasRetencoes.value, __OutrasRetencoes.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}BaseCalculo uses Python identifier BaseCalculo
    __BaseCalculo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BaseCalculo'), 'BaseCalculo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdBaseCalculo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 344, 12), )

    
    BaseCalculo = property(__BaseCalculo.value, __BaseCalculo.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Aliquota uses Python identifier Aliquota
    __Aliquota = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Aliquota'), 'Aliquota', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdAliquota', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 345, 12), )

    
    Aliquota = property(__Aliquota.value, __Aliquota.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorLiquidoNfse uses Python identifier ValorLiquidoNfse
    __ValorLiquidoNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorLiquidoNfse'), 'ValorLiquidoNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorLiquidoNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 346, 12), )

    
    ValorLiquidoNfse = property(__ValorLiquidoNfse.value, __ValorLiquidoNfse.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DescontoIncondicionado uses Python identifier DescontoIncondicionado
    __DescontoIncondicionado = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DescontoIncondicionado'), 'DescontoIncondicionado', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDescontoIncondicionado', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 347, 12), )

    
    DescontoIncondicionado = property(__DescontoIncondicionado.value, __DescontoIncondicionado.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DescontoCondicionado uses Python identifier DescontoCondicionado
    __DescontoCondicionado = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DescontoCondicionado'), 'DescontoCondicionado', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcValores_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDescontoCondicionado', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 348, 12), )

    
    DescontoCondicionado = property(__DescontoCondicionado.value, __DescontoCondicionado.set, None, None)

    _ElementMap.update({
        __ValorServicos.name() : __ValorServicos,
        __ValorDeducoes.name() : __ValorDeducoes,
        __ValorPis.name() : __ValorPis,
        __ValorCofins.name() : __ValorCofins,
        __ValorInss.name() : __ValorInss,
        __ValorIr.name() : __ValorIr,
        __ValorCsll.name() : __ValorCsll,
        __IssRetido.name() : __IssRetido,
        __ValorIss.name() : __ValorIss,
        __ValorIssRetido.name() : __ValorIssRetido,
        __OutrasRetencoes.name() : __OutrasRetencoes,
        __BaseCalculo.name() : __BaseCalculo,
        __Aliquota.name() : __Aliquota,
        __ValorLiquidoNfse.name() : __ValorLiquidoNfse,
        __DescontoIncondicionado.name() : __DescontoIncondicionado,
        __DescontoCondicionado.name() : __DescontoCondicionado
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcValores = tcValores
Namespace.addCategoryObject('typeBinding', 'tcValores', tcValores)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosServico with content type ELEMENT_ONLY
class tcDadosServico (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosServico with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcDadosServico')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 351, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Valores uses Python identifier Valores
    __Valores = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Valores'), 'Valores', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValores', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 353, 12), )

    
    Valores = property(__Valores.value, __Valores.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ItemListaServico uses Python identifier ItemListaServico
    __ItemListaServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ItemListaServico'), 'ItemListaServico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdItemListaServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 354, 12), )

    
    ItemListaServico = property(__ItemListaServico.value, __ItemListaServico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoCnae uses Python identifier CodigoCnae
    __CodigoCnae = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoCnae'), 'CodigoCnae', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoCnae', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 355, 12), )

    
    CodigoCnae = property(__CodigoCnae.value, __CodigoCnae.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoTributacaoMunicipio uses Python identifier CodigoTributacaoMunicipio
    __CodigoTributacaoMunicipio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoTributacaoMunicipio'), 'CodigoTributacaoMunicipio', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoTributacaoMunicipio', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 356, 12), )

    
    CodigoTributacaoMunicipio = property(__CodigoTributacaoMunicipio.value, __CodigoTributacaoMunicipio.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Discriminacao uses Python identifier Discriminacao
    __Discriminacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Discriminacao'), 'Discriminacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDiscriminacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 357, 12), )

    
    Discriminacao = property(__Discriminacao.value, __Discriminacao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), 'CodigoMunicipio', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosServico_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoMunicipio', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 358, 12), )

    
    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    _ElementMap.update({
        __Valores.name() : __Valores,
        __ItemListaServico.name() : __ItemListaServico,
        __CodigoCnae.name() : __CodigoCnae,
        __CodigoTributacaoMunicipio.name() : __CodigoTributacaoMunicipio,
        __Discriminacao.name() : __Discriminacao,
        __CodigoMunicipio.name() : __CodigoMunicipio
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcDadosServico = tcDadosServico
Namespace.addCategoryObject('typeBinding', 'tcDadosServico', tcDadosServico)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosConstrucaoCivil with content type ELEMENT_ONLY
class tcDadosConstrucaoCivil (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosConstrucaoCivil with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcDadosConstrucaoCivil')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 361, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoObra uses Python identifier CodigoObra
    __CodigoObra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoObra'), 'CodigoObra', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosConstrucaoCivil_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoObra', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 363, 12), )

    
    CodigoObra = property(__CodigoObra.value, __CodigoObra.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Art uses Python identifier Art
    __Art = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Art'), 'Art', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosConstrucaoCivil_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdArt', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 364, 12), )

    
    Art = property(__Art.value, __Art.set, None, None)

    _ElementMap.update({
        __CodigoObra.name() : __CodigoObra,
        __Art.name() : __Art
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcDadosConstrucaoCivil = tcDadosConstrucaoCivil
Namespace.addCategoryObject('typeBinding', 'tcDadosConstrucaoCivil', tcDadosConstrucaoCivil)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosPrestador with content type ELEMENT_ONLY
class tcDadosPrestador (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcDadosPrestador with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcDadosPrestador')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 367, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoPrestador uses Python identifier IdentificacaoPrestador
    __IdentificacaoPrestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoPrestador'), 'IdentificacaoPrestador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoPrestador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 369, 12), )

    
    IdentificacaoPrestador = property(__IdentificacaoPrestador.value, __IdentificacaoPrestador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}RazaoSocial uses Python identifier RazaoSocial
    __RazaoSocial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial'), 'RazaoSocial', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRazaoSocial', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 370, 12), )

    
    RazaoSocial = property(__RazaoSocial.value, __RazaoSocial.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NomeFantasia uses Python identifier NomeFantasia
    __NomeFantasia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NomeFantasia'), 'NomeFantasia', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNomeFantasia', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 371, 12), )

    
    NomeFantasia = property(__NomeFantasia.value, __NomeFantasia.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Endereco uses Python identifier Endereco
    __Endereco = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Endereco'), 'Endereco', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdEndereco', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 372, 12), )

    
    Endereco = property(__Endereco.value, __Endereco.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Contato uses Python identifier Contato
    __Contato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contato'), 'Contato', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcDadosPrestador_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdContato', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 373, 12), )

    
    Contato = property(__Contato.value, __Contato.set, None, None)

    _ElementMap.update({
        __IdentificacaoPrestador.name() : __IdentificacaoPrestador,
        __RazaoSocial.name() : __RazaoSocial,
        __NomeFantasia.name() : __NomeFantasia,
        __Endereco.name() : __Endereco,
        __Contato.name() : __Contato
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcDadosPrestador = tcDadosPrestador
Namespace.addCategoryObject('typeBinding', 'tcDadosPrestador', tcDadosPrestador)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcRps with content type ELEMENT_ONLY
class tcRps (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcRps with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 394, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InfRps uses Python identifier InfRps
    __InfRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InfRps'), 'InfRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInfRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 396, 12), )

    
    InfRps = property(__InfRps.value, __InfRps.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcRps_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __InfRps.name() : __InfRps,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcRps = tcRps
Namespace.addCategoryObject('typeBinding', 'tcRps', tcRps)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoNfse with content type ELEMENT_ONLY
class tcIdentificacaoNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcIdentificacaoNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcIdentificacaoNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 400, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numero'), 'Numero', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumero', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 402, 12), )

    
    Numero = property(__Numero.value, __Numero.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), 'Cnpj', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCnpj', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 403, 12), )

    
    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), 'InscricaoMunicipal', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInscricaoMunicipal', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 404, 12), )

    
    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoMunicipio uses Python identifier CodigoMunicipio
    __CodigoMunicipio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), 'CodigoMunicipio', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcIdentificacaoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoMunicipio', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 405, 12), )

    
    CodigoMunicipio = property(__CodigoMunicipio.value, __CodigoMunicipio.set, None, None)

    _ElementMap.update({
        __Numero.name() : __Numero,
        __Cnpj.name() : __Cnpj,
        __InscricaoMunicipal.name() : __InscricaoMunicipal,
        __CodigoMunicipio.name() : __CodigoMunicipio
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcIdentificacaoNfse = tcIdentificacaoNfse
Namespace.addCategoryObject('typeBinding', 'tcIdentificacaoNfse', tcIdentificacaoNfse)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcNfse with content type ELEMENT_ONLY
class tcNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 432, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InfNfse uses Python identifier InfNfse
    __InfNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InfNfse'), 'InfNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInfNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 434, 12), )

    
    InfNfse = property(__InfNfse.value, __InfNfse.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcNfse_httpwww_w3_org200009xmldsigSignature', True, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __InfNfse.name() : __InfNfse,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcNfse = tcNfse
Namespace.addCategoryObject('typeBinding', 'tcNfse', tcNfse)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcPedidoCancelamento with content type ELEMENT_ONLY
class tcPedidoCancelamento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcPedidoCancelamento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcPedidoCancelamento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 446, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InfPedidoCancelamento uses Python identifier InfPedidoCancelamento
    __InfPedidoCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InfPedidoCancelamento'), 'InfPedidoCancelamento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcPedidoCancelamento_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInfPedidoCancelamento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 448, 12), )

    
    InfPedidoCancelamento = property(__InfPedidoCancelamento.value, __InfPedidoCancelamento.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcPedidoCancelamento_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __InfPedidoCancelamento.name() : __InfPedidoCancelamento,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcPedidoCancelamento = tcPedidoCancelamento
Namespace.addCategoryObject('typeBinding', 'tcPedidoCancelamento', tcPedidoCancelamento)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcCancelamentoNfse with content type ELEMENT_ONLY
class tcCancelamentoNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcCancelamentoNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcCancelamentoNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 460, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Confirmacao uses Python identifier Confirmacao
    __Confirmacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Confirmacao'), 'Confirmacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCancelamentoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdConfirmacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 462, 12), )

    
    Confirmacao = property(__Confirmacao.value, __Confirmacao.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCancelamentoNfse_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Confirmacao.name() : __Confirmacao,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcCancelamentoNfse = tcCancelamentoNfse
Namespace.addCategoryObject('typeBinding', 'tcCancelamentoNfse', tcCancelamentoNfse)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcSubstituicaoNfse with content type ELEMENT_ONLY
class tcSubstituicaoNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcSubstituicaoNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcSubstituicaoNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 473, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}SubstituicaoNfse uses Python identifier SubstituicaoNfse
    __SubstituicaoNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubstituicaoNfse'), 'SubstituicaoNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcSubstituicaoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdSubstituicaoNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 475, 12), )

    
    SubstituicaoNfse = property(__SubstituicaoNfse.value, __SubstituicaoNfse.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcSubstituicaoNfse_httpwww_w3_org200009xmldsigSignature', True, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __SubstituicaoNfse.name() : __SubstituicaoNfse,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcSubstituicaoNfse = tcSubstituicaoNfse
Namespace.addCategoryObject('typeBinding', 'tcSubstituicaoNfse', tcSubstituicaoNfse)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcCompNfse with content type ELEMENT_ONLY
class tcCompNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcCompNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcCompNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 479, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Nfse uses Python identifier Nfse
    __Nfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nfse'), 'Nfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCompNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 481, 12), )

    
    Nfse = property(__Nfse.value, __Nfse.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NfseCancelamento uses Python identifier NfseCancelamento
    __NfseCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NfseCancelamento'), 'NfseCancelamento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCompNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNfseCancelamento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 482, 12), )

    
    NfseCancelamento = property(__NfseCancelamento.value, __NfseCancelamento.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NfseSubstituicao uses Python identifier NfseSubstituicao
    __NfseSubstituicao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituicao'), 'NfseSubstituicao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcCompNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNfseSubstituicao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 483, 12), )

    
    NfseSubstituicao = property(__NfseSubstituicao.value, __NfseSubstituicao.set, None, None)

    _ElementMap.update({
        __Nfse.name() : __Nfse,
        __NfseCancelamento.name() : __NfseCancelamento,
        __NfseSubstituicao.name() : __NfseSubstituicao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcCompNfse = tcCompNfse
Namespace.addCategoryObject('typeBinding', 'tcCompNfse', tcCompNfse)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 488, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}MensagemRetorno uses Python identifier MensagemRetorno
    __MensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MensagemRetorno'), 'MensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdMensagemRetorno', True, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 490, 16), )

    
    MensagemRetorno = property(__MensagemRetorno.value, __MensagemRetorno.set, None, None)

    _ElementMap.update({
        __MensagemRetorno.name() : __MensagemRetorno
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcMensagemRetorno with content type ELEMENT_ONLY
class tcMensagemRetorno (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcMensagemRetorno with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcMensagemRetorno')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 494, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Codigo'), 'Codigo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcMensagemRetorno_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 496, 12), )

    
    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Mensagem uses Python identifier Mensagem
    __Mensagem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mensagem'), 'Mensagem', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcMensagemRetorno_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdMensagem', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 497, 12), )

    
    Mensagem = property(__Mensagem.value, __Mensagem.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Correcao uses Python identifier Correcao
    __Correcao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Correcao'), 'Correcao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcMensagemRetorno_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCorrecao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 498, 12), )

    
    Correcao = property(__Correcao.value, __Correcao.set, None, None)

    _ElementMap.update({
        __Codigo.name() : __Codigo,
        __Mensagem.name() : __Mensagem,
        __Correcao.name() : __Correcao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcMensagemRetorno = tcMensagemRetorno
Namespace.addCategoryObject('typeBinding', 'tcMensagemRetorno', tcMensagemRetorno)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcMensagemRetornoLote with content type ELEMENT_ONLY
class tcMensagemRetornoLote (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcMensagemRetornoLote with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcMensagemRetornoLote')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 501, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), 'IdentificacaoRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcMensagemRetornoLote_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 503, 12), )

    
    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Codigo'), 'Codigo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcMensagemRetornoLote_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 504, 12), )

    
    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Mensagem uses Python identifier Mensagem
    __Mensagem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Mensagem'), 'Mensagem', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcMensagemRetornoLote_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdMensagem', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 505, 12), )

    
    Mensagem = property(__Mensagem.value, __Mensagem.set, None, None)

    _ElementMap.update({
        __IdentificacaoRps.name() : __IdentificacaoRps,
        __Codigo.name() : __Codigo,
        __Mensagem.name() : __Mensagem
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tcMensagemRetornoLote = tcMensagemRetornoLote
Namespace.addCategoryObject('typeBinding', 'tcMensagemRetornoLote', tcMensagemRetornoLote)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 515, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Rps uses Python identifier Rps
    __Rps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rps'), 'Rps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON__httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRps', True, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 517, 24), )

    
    Rps = property(__Rps.value, __Rps.set, None, None)

    _ElementMap.update({
        __Rps.name() : __Rps
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 527, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), 'ListaMensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_2_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaMensagemRetorno', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4), )

    
    ListaMensagemRetorno = property(__ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote'), 'NumeroLote', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_2_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumeroLote', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 530, 20), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataRecebimento uses Python identifier DataRecebimento
    __DataRecebimento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataRecebimento'), 'DataRecebimento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_2_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataRecebimento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 531, 20), )

    
    DataRecebimento = property(__DataRecebimento.value, __DataRecebimento.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Protocolo uses Python identifier Protocolo
    __Protocolo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Protocolo'), 'Protocolo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_2_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdProtocolo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 532, 20), )

    
    Protocolo = property(__Protocolo.value, __Protocolo.set, None, None)

    _ElementMap.update({
        __ListaMensagemRetorno.name() : __ListaMensagemRetorno,
        __NumeroLote.name() : __NumeroLote,
        __DataRecebimento.name() : __DataRecebimento,
        __Protocolo.name() : __Protocolo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 540, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}LoteRps uses Python identifier LoteRps
    __LoteRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LoteRps'), 'LoteRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_3_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdLoteRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 542, 16), )

    
    LoteRps = property(__LoteRps.value, __LoteRps.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), 'Signature', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_3_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __LoteRps.name() : __LoteRps,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 549, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), 'ListaMensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_4_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaMensagemRetorno', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4), )

    
    ListaMensagemRetorno = property(__ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote'), 'NumeroLote', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_4_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumeroLote', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 552, 20), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Situacao uses Python identifier Situacao
    __Situacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Situacao'), 'Situacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_4_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdSituacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 553, 20), )

    
    Situacao = property(__Situacao.value, __Situacao.set, None, None)

    _ElementMap.update({
        __ListaMensagemRetorno.name() : __ListaMensagemRetorno,
        __NumeroLote.name() : __NumeroLote,
        __Situacao.name() : __Situacao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 561, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), 'Prestador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_5_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPrestador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 563, 16), )

    
    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Protocolo uses Python identifier Protocolo
    __Protocolo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Protocolo'), 'Protocolo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_5_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdProtocolo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 564, 16), )

    
    Protocolo = property(__Protocolo.value, __Protocolo.set, None, None)

    _ElementMap.update({
        __Prestador.name() : __Prestador,
        __Protocolo.name() : __Protocolo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 570, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), 'ListaMensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_6_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaMensagemRetorno', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4), )

    
    ListaMensagemRetorno = property(__ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), 'CompNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_6_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCompNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 572, 16), )

    
    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update({
        __ListaMensagemRetorno.name() : __ListaMensagemRetorno,
        __CompNfse.name() : __CompNfse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 579, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), 'IdentificacaoRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_7_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 581, 16), )

    
    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), 'Prestador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_7_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPrestador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 582, 16), )

    
    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    _ElementMap.update({
        __IdentificacaoRps.name() : __IdentificacaoRps,
        __Prestador.name() : __Prestador
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 588, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), 'ListaMensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_8_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaMensagemRetorno', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4), )

    
    ListaMensagemRetorno = property(__ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaNfse'), 'ListaNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_8_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 590, 16), )

    
    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update({
        __ListaMensagemRetorno.name() : __ListaMensagemRetorno,
        __ListaNfse.name() : __ListaNfse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 591, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), 'CompNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_9_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCompNfse', True, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 593, 28), )

    
    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update({
        __CompNfse.name() : __CompNfse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 603, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), 'Prestador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_10_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPrestador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 605, 16), )

    
    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NumeroNfse uses Python identifier NumeroNfse
    __NumeroNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumeroNfse'), 'NumeroNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_10_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumeroNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 606, 16), )

    
    NumeroNfse = property(__NumeroNfse.value, __NumeroNfse.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}PeriodoEmissao uses Python identifier PeriodoEmissao
    __PeriodoEmissao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PeriodoEmissao'), 'PeriodoEmissao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_10_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPeriodoEmissao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 607, 16), )

    
    PeriodoEmissao = property(__PeriodoEmissao.value, __PeriodoEmissao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Tomador uses Python identifier Tomador
    __Tomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tomador'), 'Tomador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_10_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdTomador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 615, 16), )

    
    Tomador = property(__Tomador.value, __Tomador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IntermediarioServico uses Python identifier IntermediarioServico
    __IntermediarioServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico'), 'IntermediarioServico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_10_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIntermediarioServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 616, 16), )

    
    IntermediarioServico = property(__IntermediarioServico.value, __IntermediarioServico.set, None, None)

    _ElementMap.update({
        __Prestador.name() : __Prestador,
        __NumeroNfse.name() : __NumeroNfse,
        __PeriodoEmissao.name() : __PeriodoEmissao,
        __Tomador.name() : __Tomador,
        __IntermediarioServico.name() : __IntermediarioServico
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 608, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataInicial uses Python identifier DataInicial
    __DataInicial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataInicial'), 'DataInicial', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_11_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataInicial', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 610, 28), )

    
    DataInicial = property(__DataInicial.value, __DataInicial.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataFinal uses Python identifier DataFinal
    __DataFinal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataFinal'), 'DataFinal', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_11_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataFinal', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 611, 28), )

    
    DataFinal = property(__DataFinal.value, __DataFinal.set, None, None)

    _ElementMap.update({
        __DataInicial.name() : __DataInicial,
        __DataFinal.name() : __DataFinal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 622, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), 'ListaMensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_12_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaMensagemRetorno', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4), )

    
    ListaMensagemRetorno = property(__ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaNfse uses Python identifier ListaNfse
    __ListaNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaNfse'), 'ListaNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_12_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 624, 16), )

    
    ListaNfse = property(__ListaNfse.value, __ListaNfse.set, None, None)

    _ElementMap.update({
        __ListaMensagemRetorno.name() : __ListaMensagemRetorno,
        __ListaNfse.name() : __ListaNfse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 625, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CompNfse uses Python identifier CompNfse
    __CompNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), 'CompNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_13_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCompNfse', True, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 627, 28), )

    
    CompNfse = property(__CompNfse.value, __CompNfse.set, None, None)

    _ElementMap.update({
        __CompNfse.name() : __CompNfse
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 637, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), 'Prestador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_14_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPrestador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 639, 16), )

    
    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Protocolo uses Python identifier Protocolo
    __Protocolo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Protocolo'), 'Protocolo', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_14_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdProtocolo', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 640, 16), )

    
    Protocolo = property(__Protocolo.value, __Protocolo.set, None, None)

    _ElementMap.update({
        __Prestador.name() : __Prestador,
        __Protocolo.name() : __Protocolo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 646, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaMensagemRetorno uses Python identifier ListaMensagemRetorno
    __ListaMensagemRetorno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), 'ListaMensagemRetorno', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_15_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaMensagemRetorno', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4), )

    
    ListaMensagemRetorno = property(__ListaMensagemRetorno.value, __ListaMensagemRetorno.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cancelamento uses Python identifier Cancelamento
    __Cancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cancelamento'), 'Cancelamento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_15_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCancelamento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 648, 16), )

    
    Cancelamento = property(__Cancelamento.value, __Cancelamento.set, None, None)

    _ElementMap.update({
        __ListaMensagemRetorno.name() : __ListaMensagemRetorno,
        __Cancelamento.name() : __Cancelamento
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 655, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Pedido uses Python identifier Pedido
    __Pedido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pedido'), 'Pedido', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_CTD_ANON_16_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPedido', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 657, 16), )

    
    Pedido = property(__Pedido.value, __Pedido.set, None, None)

    _ElementMap.update({
        __Pedido.name() : __Pedido
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfRps with content type ELEMENT_ONLY
class tcInfRps (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfRps with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcInfRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 376, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), 'IdentificacaoRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 378, 12), )

    
    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataEmissao'), 'DataEmissao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataEmissao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 379, 12), )

    
    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NaturezaOperacao uses Python identifier NaturezaOperacao
    __NaturezaOperacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NaturezaOperacao'), 'NaturezaOperacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNaturezaOperacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 380, 12), )

    
    NaturezaOperacao = property(__NaturezaOperacao.value, __NaturezaOperacao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}RegimeEspecialTributacao uses Python identifier RegimeEspecialTributacao
    __RegimeEspecialTributacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RegimeEspecialTributacao'), 'RegimeEspecialTributacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRegimeEspecialTributacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 381, 12), )

    
    RegimeEspecialTributacao = property(__RegimeEspecialTributacao.value, __RegimeEspecialTributacao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}OptanteSimplesNacional uses Python identifier OptanteSimplesNacional
    __OptanteSimplesNacional = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OptanteSimplesNacional'), 'OptanteSimplesNacional', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdOptanteSimplesNacional', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 382, 12), )

    
    OptanteSimplesNacional = property(__OptanteSimplesNacional.value, __OptanteSimplesNacional.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IncentivadorCultural uses Python identifier IncentivadorCultural
    __IncentivadorCultural = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncentivadorCultural'), 'IncentivadorCultural', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIncentivadorCultural', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 383, 12), )

    
    IncentivadorCultural = property(__IncentivadorCultural.value, __IncentivadorCultural.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdStatus', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 384, 12), )

    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}RpsSubstituido uses Python identifier RpsSubstituido
    __RpsSubstituido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RpsSubstituido'), 'RpsSubstituido', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRpsSubstituido', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 385, 12), )

    
    RpsSubstituido = property(__RpsSubstituido.value, __RpsSubstituido.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Servico uses Python identifier Servico
    __Servico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Servico'), 'Servico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 386, 12), )

    
    Servico = property(__Servico.value, __Servico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Prestador uses Python identifier Prestador
    __Prestador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), 'Prestador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPrestador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 387, 12), )

    
    Prestador = property(__Prestador.value, __Prestador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Tomador uses Python identifier Tomador
    __Tomador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tomador'), 'Tomador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdTomador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 388, 12), )

    
    Tomador = property(__Tomador.value, __Tomador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IntermediarioServico uses Python identifier IntermediarioServico
    __IntermediarioServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico'), 'IntermediarioServico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIntermediarioServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 389, 12), )

    
    IntermediarioServico = property(__IntermediarioServico.value, __IntermediarioServico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ContrucaoCivil uses Python identifier ContrucaoCivil
    __ContrucaoCivil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContrucaoCivil'), 'ContrucaoCivil', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdContrucaoCivil', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 390, 12), )

    
    ContrucaoCivil = property(__ContrucaoCivil.value, __ContrucaoCivil.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfRps_id', _module_typeBindings.tsIdTag)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 392, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 392, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __IdentificacaoRps.name() : __IdentificacaoRps,
        __DataEmissao.name() : __DataEmissao,
        __NaturezaOperacao.name() : __NaturezaOperacao,
        __RegimeEspecialTributacao.name() : __RegimeEspecialTributacao,
        __OptanteSimplesNacional.name() : __OptanteSimplesNacional,
        __IncentivadorCultural.name() : __IncentivadorCultural,
        __Status.name() : __Status,
        __RpsSubstituido.name() : __RpsSubstituido,
        __Servico.name() : __Servico,
        __Prestador.name() : __Prestador,
        __Tomador.name() : __Tomador,
        __IntermediarioServico.name() : __IntermediarioServico,
        __ContrucaoCivil.name() : __ContrucaoCivil
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.tcInfRps = tcInfRps
Namespace.addCategoryObject('typeBinding', 'tcInfRps', tcInfRps)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfNfse with content type ELEMENT_ONLY
class tcInfNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcInfNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 408, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Numero'), 'Numero', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumero', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 410, 12), )

    
    Numero = property(__Numero.value, __Numero.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoVerificacao uses Python identifier CodigoVerificacao
    __CodigoVerificacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoVerificacao'), 'CodigoVerificacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoVerificacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 411, 12), )

    
    CodigoVerificacao = property(__CodigoVerificacao.value, __CodigoVerificacao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataEmissao uses Python identifier DataEmissao
    __DataEmissao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataEmissao'), 'DataEmissao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataEmissao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 412, 12), )

    
    DataEmissao = property(__DataEmissao.value, __DataEmissao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoRps uses Python identifier IdentificacaoRps
    __IdentificacaoRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), 'IdentificacaoRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 413, 12), )

    
    IdentificacaoRps = property(__IdentificacaoRps.value, __IdentificacaoRps.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataEmissaoRps uses Python identifier DataEmissaoRps
    __DataEmissaoRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataEmissaoRps'), 'DataEmissaoRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataEmissaoRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 414, 12), )

    
    DataEmissaoRps = property(__DataEmissaoRps.value, __DataEmissaoRps.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NaturezaOperacao uses Python identifier NaturezaOperacao
    __NaturezaOperacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NaturezaOperacao'), 'NaturezaOperacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNaturezaOperacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 415, 12), )

    
    NaturezaOperacao = property(__NaturezaOperacao.value, __NaturezaOperacao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}RegimeEspecialTributacao uses Python identifier RegimeEspecialTributacao
    __RegimeEspecialTributacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RegimeEspecialTributacao'), 'RegimeEspecialTributacao', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdRegimeEspecialTributacao', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 416, 12), )

    
    RegimeEspecialTributacao = property(__RegimeEspecialTributacao.value, __RegimeEspecialTributacao.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}OptanteSimplesNacional uses Python identifier OptanteSimplesNacional
    __OptanteSimplesNacional = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OptanteSimplesNacional'), 'OptanteSimplesNacional', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdOptanteSimplesNacional', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 417, 12), )

    
    OptanteSimplesNacional = property(__OptanteSimplesNacional.value, __OptanteSimplesNacional.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IncentivadorCultural uses Python identifier IncentivadorCultural
    __IncentivadorCultural = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncentivadorCultural'), 'IncentivadorCultural', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIncentivadorCultural', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 418, 12), )

    
    IncentivadorCultural = property(__IncentivadorCultural.value, __IncentivadorCultural.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Competencia uses Python identifier Competencia
    __Competencia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Competencia'), 'Competencia', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCompetencia', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 419, 12), )

    
    Competencia = property(__Competencia.value, __Competencia.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NfseSubstituida uses Python identifier NfseSubstituida
    __NfseSubstituida = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituida'), 'NfseSubstituida', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNfseSubstituida', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 420, 12), )

    
    NfseSubstituida = property(__NfseSubstituida.value, __NfseSubstituida.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}OutrasInformacoes uses Python identifier OutrasInformacoes
    __OutrasInformacoes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutrasInformacoes'), 'OutrasInformacoes', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdOutrasInformacoes', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 421, 12), )

    
    OutrasInformacoes = property(__OutrasInformacoes.value, __OutrasInformacoes.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Servico uses Python identifier Servico
    __Servico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Servico'), 'Servico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 422, 12), )

    
    Servico = property(__Servico.value, __Servico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ValorCredito uses Python identifier ValorCredito
    __ValorCredito = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValorCredito'), 'ValorCredito', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdValorCredito', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 423, 12), )

    
    ValorCredito = property(__ValorCredito.value, __ValorCredito.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}PrestadorServico uses Python identifier PrestadorServico
    __PrestadorServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrestadorServico'), 'PrestadorServico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPrestadorServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 424, 12), )

    
    PrestadorServico = property(__PrestadorServico.value, __PrestadorServico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}TomadorServico uses Python identifier TomadorServico
    __TomadorServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TomadorServico'), 'TomadorServico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdTomadorServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 425, 12), )

    
    TomadorServico = property(__TomadorServico.value, __TomadorServico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IntermediarioServico uses Python identifier IntermediarioServico
    __IntermediarioServico = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico'), 'IntermediarioServico', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIntermediarioServico', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 426, 12), )

    
    IntermediarioServico = property(__IntermediarioServico.value, __IntermediarioServico.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}OrgaoGerador uses Python identifier OrgaoGerador
    __OrgaoGerador = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgaoGerador'), 'OrgaoGerador', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdOrgaoGerador', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 427, 12), )

    
    OrgaoGerador = property(__OrgaoGerador.value, __OrgaoGerador.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ContrucaoCivil uses Python identifier ContrucaoCivil
    __ContrucaoCivil = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContrucaoCivil'), 'ContrucaoCivil', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdContrucaoCivil', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 428, 12), )

    
    ContrucaoCivil = property(__ContrucaoCivil.value, __ContrucaoCivil.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfNfse_id', _module_typeBindings.tsIdTag)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 430, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 430, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __Numero.name() : __Numero,
        __CodigoVerificacao.name() : __CodigoVerificacao,
        __DataEmissao.name() : __DataEmissao,
        __IdentificacaoRps.name() : __IdentificacaoRps,
        __DataEmissaoRps.name() : __DataEmissaoRps,
        __NaturezaOperacao.name() : __NaturezaOperacao,
        __RegimeEspecialTributacao.name() : __RegimeEspecialTributacao,
        __OptanteSimplesNacional.name() : __OptanteSimplesNacional,
        __IncentivadorCultural.name() : __IncentivadorCultural,
        __Competencia.name() : __Competencia,
        __NfseSubstituida.name() : __NfseSubstituida,
        __OutrasInformacoes.name() : __OutrasInformacoes,
        __Servico.name() : __Servico,
        __ValorCredito.name() : __ValorCredito,
        __PrestadorServico.name() : __PrestadorServico,
        __TomadorServico.name() : __TomadorServico,
        __IntermediarioServico.name() : __IntermediarioServico,
        __OrgaoGerador.name() : __OrgaoGerador,
        __ContrucaoCivil.name() : __ContrucaoCivil
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.tcInfNfse = tcInfNfse
Namespace.addCategoryObject('typeBinding', 'tcInfNfse', tcInfNfse)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfPedidoCancelamento with content type ELEMENT_ONLY
class tcInfPedidoCancelamento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfPedidoCancelamento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcInfPedidoCancelamento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 439, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}IdentificacaoNfse uses Python identifier IdentificacaoNfse
    __IdentificacaoNfse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoNfse'), 'IdentificacaoNfse', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfPedidoCancelamento_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdIdentificacaoNfse', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 441, 12), )

    
    IdentificacaoNfse = property(__IdentificacaoNfse.value, __IdentificacaoNfse.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}CodigoCancelamento uses Python identifier CodigoCancelamento
    __CodigoCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodigoCancelamento'), 'CodigoCancelamento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfPedidoCancelamento_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCodigoCancelamento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 442, 12), )

    
    CodigoCancelamento = property(__CodigoCancelamento.value, __CodigoCancelamento.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfPedidoCancelamento_id', _module_typeBindings.tsIdTag)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 444, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 444, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __IdentificacaoNfse.name() : __IdentificacaoNfse,
        __CodigoCancelamento.name() : __CodigoCancelamento
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.tcInfPedidoCancelamento = tcInfPedidoCancelamento
Namespace.addCategoryObject('typeBinding', 'tcInfPedidoCancelamento', tcInfPedidoCancelamento)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcConfirmacaoCancelamento with content type ELEMENT_ONLY
class tcConfirmacaoCancelamento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcConfirmacaoCancelamento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcConfirmacaoCancelamento')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 452, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Pedido uses Python identifier Pedido
    __Pedido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pedido'), 'Pedido', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcConfirmacaoCancelamento_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdPedido', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 454, 12), )

    
    Pedido = property(__Pedido.value, __Pedido.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}DataHoraCancelamento uses Python identifier DataHoraCancelamento
    __DataHoraCancelamento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataHoraCancelamento'), 'DataHoraCancelamento', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcConfirmacaoCancelamento_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdDataHoraCancelamento', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 455, 12), )

    
    DataHoraCancelamento = property(__DataHoraCancelamento.value, __DataHoraCancelamento.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcConfirmacaoCancelamento_id', _module_typeBindings.tsIdTag)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 457, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 457, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __Pedido.name() : __Pedido,
        __DataHoraCancelamento.name() : __DataHoraCancelamento
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.tcConfirmacaoCancelamento = tcConfirmacaoCancelamento
Namespace.addCategoryObject('typeBinding', 'tcConfirmacaoCancelamento', tcConfirmacaoCancelamento)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfSubstituicaoNfse with content type ELEMENT_ONLY
class tcInfSubstituicaoNfse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcInfSubstituicaoNfse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcInfSubstituicaoNfse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 467, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NfseSubstituidora uses Python identifier NfseSubstituidora
    __NfseSubstituidora = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituidora'), 'NfseSubstituidora', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfSubstituicaoNfse_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNfseSubstituidora', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 469, 12), )

    
    NfseSubstituidora = property(__NfseSubstituidora.value, __NfseSubstituidora.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcInfSubstituicaoNfse_id', _module_typeBindings.tsIdTag)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 471, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 471, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __NfseSubstituidora.name() : __NfseSubstituidora
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.tcInfSubstituicaoNfse = tcInfSubstituicaoNfse
Namespace.addCategoryObject('typeBinding', 'tcInfSubstituicaoNfse', tcInfSubstituicaoNfse)


# Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcLoteRps with content type ELEMENT_ONLY
class tcLoteRps (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}tcLoteRps with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tcLoteRps')
    _XSDLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 508, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}NumeroLote uses Python identifier NumeroLote
    __NumeroLote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote'), 'NumeroLote', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcLoteRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdNumeroLote', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 510, 12), )

    
    NumeroLote = property(__NumeroLote.value, __NumeroLote.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}Cnpj uses Python identifier Cnpj
    __Cnpj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), 'Cnpj', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcLoteRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdCnpj', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 511, 12), )

    
    Cnpj = property(__Cnpj.value, __Cnpj.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}InscricaoMunicipal uses Python identifier InscricaoMunicipal
    __InscricaoMunicipal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), 'InscricaoMunicipal', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcLoteRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdInscricaoMunicipal', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 512, 12), )

    
    InscricaoMunicipal = property(__InscricaoMunicipal.value, __InscricaoMunicipal.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}QuantidadeRps uses Python identifier QuantidadeRps
    __QuantidadeRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QuantidadeRps'), 'QuantidadeRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcLoteRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdQuantidadeRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 513, 12), )

    
    QuantidadeRps = property(__QuantidadeRps.value, __QuantidadeRps.set, None, None)

    
    # Element {http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}ListaRps uses Python identifier ListaRps
    __ListaRps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListaRps'), 'ListaRps', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcLoteRps_httpisscuritiba_curitiba_pr_gov_brissnfse_xsdListaRps', False, pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 514, 12), )

    
    ListaRps = property(__ListaRps.value, __ListaRps.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpisscuritiba_curitiba_pr_gov_brissnfse_xsd_tcLoteRps_id', _module_typeBindings.tsIdTag)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 523, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 523, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __NumeroLote.name() : __NumeroLote,
        __Cnpj.name() : __Cnpj,
        __InscricaoMunicipal.name() : __InscricaoMunicipal,
        __QuantidadeRps.name() : __QuantidadeRps,
        __ListaRps.name() : __ListaRps
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.tcLoteRps = tcLoteRps
Namespace.addCategoryObject('typeBinding', 'tcLoteRps', tcLoteRps)


CompNfse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), tcCompNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 486, 4))
Namespace.addCategoryObject('elementBinding', CompNfse.name().localName(), CompNfse)

ListaMensagemRetorno = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4))
Namespace.addCategoryObject('elementBinding', ListaMensagemRetorno.name().localName(), ListaMensagemRetorno)

EnviarLoteRpsResposta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnviarLoteRpsResposta'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 526, 4))
Namespace.addCategoryObject('elementBinding', EnviarLoteRpsResposta.name().localName(), EnviarLoteRpsResposta)

EnviarLoteRpsEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnviarLoteRpsEnvio'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 539, 4))
Namespace.addCategoryObject('elementBinding', EnviarLoteRpsEnvio.name().localName(), EnviarLoteRpsEnvio)

ConsultarSituacaoLoteRpsResposta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarSituacaoLoteRpsResposta'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 548, 4))
Namespace.addCategoryObject('elementBinding', ConsultarSituacaoLoteRpsResposta.name().localName(), ConsultarSituacaoLoteRpsResposta)

ConsultarSituacaoLoteRpsEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarSituacaoLoteRpsEnvio'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 560, 4))
Namespace.addCategoryObject('elementBinding', ConsultarSituacaoLoteRpsEnvio.name().localName(), ConsultarSituacaoLoteRpsEnvio)

ConsultarNfseRpsResposta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarNfseRpsResposta'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 569, 4))
Namespace.addCategoryObject('elementBinding', ConsultarNfseRpsResposta.name().localName(), ConsultarNfseRpsResposta)

ConsultarNfseRpsEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarNfseRpsEnvio'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 578, 4))
Namespace.addCategoryObject('elementBinding', ConsultarNfseRpsEnvio.name().localName(), ConsultarNfseRpsEnvio)

ConsultarNfseResposta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarNfseResposta'), CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 587, 4))
Namespace.addCategoryObject('elementBinding', ConsultarNfseResposta.name().localName(), ConsultarNfseResposta)

ConsultarNfseEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarNfseEnvio'), CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 602, 4))
Namespace.addCategoryObject('elementBinding', ConsultarNfseEnvio.name().localName(), ConsultarNfseEnvio)

ConsultarLoteRpsResposta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarLoteRpsResposta'), CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 621, 4))
Namespace.addCategoryObject('elementBinding', ConsultarLoteRpsResposta.name().localName(), ConsultarLoteRpsResposta)

ConsultarLoteRpsEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsultarLoteRpsEnvio'), CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 636, 4))
Namespace.addCategoryObject('elementBinding', ConsultarLoteRpsEnvio.name().localName(), ConsultarLoteRpsEnvio)

CancelarNfseResposta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelarNfseResposta'), CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 645, 4))
Namespace.addCategoryObject('elementBinding', CancelarNfseResposta.name().localName(), CancelarNfseResposta)

CancelarNfseEnvio = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CancelarNfseEnvio'), CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 654, 4))
Namespace.addCategoryObject('elementBinding', CancelarNfseEnvio.name().localName(), CancelarNfseEnvio)



tcCpfCnpj._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cpf'), tsCpf, scope=tcCpfCnpj, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 270, 12)))

tcCpfCnpj._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), tsCnpj, scope=tcCpfCnpj, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 271, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcCpfCnpj._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cpf')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 270, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcCpfCnpj._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cnpj')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 271, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcCpfCnpj._Automaton = _BuildAutomaton()




tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Endereco'), tsEndereco, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 276, 12)))

tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numero'), tsNumeroEndereco, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 277, 12)))

tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Complemento'), tsComplementoEndereco, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 278, 12)))

tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Bairro'), tsBairro, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 279, 12)))

tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), tsCodigoMunicipioIbge, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 280, 12)))

tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Uf'), tsUf, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 281, 12)))

tcEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cep'), tsCep, scope=tcEndereco, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 282, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 276, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 277, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 278, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 279, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 280, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 281, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 282, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Endereco')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 276, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numero')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 277, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Complemento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 278, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Bairro')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 279, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 280, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Uf')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 281, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(tcEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cep')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 282, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tcEndereco._Automaton = _BuildAutomaton_()




tcContato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Telefone'), tsTelefone, scope=tcContato, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 287, 12)))

tcContato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Email'), tsEmail, scope=tcContato, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 288, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 287, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 288, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcContato._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Telefone')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 287, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tcContato._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Email')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 288, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tcContato._Automaton = _BuildAutomaton_2()




tcIdentificacaoOrgaoGerador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), tsCodigoMunicipioIbge, scope=tcIdentificacaoOrgaoGerador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 293, 12)))

tcIdentificacaoOrgaoGerador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Uf'), tsUf, scope=tcIdentificacaoOrgaoGerador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 294, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoOrgaoGerador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 293, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoOrgaoGerador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Uf')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 294, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcIdentificacaoOrgaoGerador._Automaton = _BuildAutomaton_3()




tcIdentificacaoRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numero'), tsNumeroRps, scope=tcIdentificacaoRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 299, 12)))

tcIdentificacaoRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Serie'), tsSerieRps, scope=tcIdentificacaoRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 300, 12)))

tcIdentificacaoRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tipo'), tsTipoRps, scope=tcIdentificacaoRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 301, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numero')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 299, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Serie')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 300, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tipo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 301, 12))
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
tcIdentificacaoRps._Automaton = _BuildAutomaton_4()




tcIdentificacaoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), tsCnpj, scope=tcIdentificacaoPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 306, 12)))

tcIdentificacaoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), tsInscricaoMunicipal, scope=tcIdentificacaoPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 307, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 307, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cnpj')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 306, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 307, 12))
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
tcIdentificacaoPrestador._Automaton = _BuildAutomaton_5()




tcIdentificacaoTomador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CpfCnpj'), tcCpfCnpj, scope=tcIdentificacaoTomador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 312, 12)))

tcIdentificacaoTomador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), tsInscricaoMunicipal, scope=tcIdentificacaoTomador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 313, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 312, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 313, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CpfCnpj')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 312, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 313, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tcIdentificacaoTomador._Automaton = _BuildAutomaton_6()




tcDadosTomador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoTomador'), tcIdentificacaoTomador, scope=tcDadosTomador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 318, 12)))

tcDadosTomador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial'), tsRazaoSocial, scope=tcDadosTomador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 319, 12)))

tcDadosTomador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Endereco'), tcEndereco, scope=tcDadosTomador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 320, 12)))

tcDadosTomador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contato'), tcContato, scope=tcDadosTomador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 321, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 318, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 319, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 320, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 321, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoTomador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 318, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 319, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Endereco')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 320, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(tcDadosTomador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contato')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 321, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tcDadosTomador._Automaton = _BuildAutomaton_7()




tcIdentificacaoIntermediarioServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial'), tsRazaoSocial, scope=tcIdentificacaoIntermediarioServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 326, 12)))

tcIdentificacaoIntermediarioServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CpfCnpj'), tcCpfCnpj, scope=tcIdentificacaoIntermediarioServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 327, 12)))

tcIdentificacaoIntermediarioServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), tsInscricaoMunicipal, scope=tcIdentificacaoIntermediarioServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 328, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 328, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoIntermediarioServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 326, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoIntermediarioServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CpfCnpj')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 327, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoIntermediarioServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 328, 12))
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
tcIdentificacaoIntermediarioServico._Automaton = _BuildAutomaton_8()




tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorServicos'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 333, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorDeducoes'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 334, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorPis'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 335, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorCofins'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 336, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorInss'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 337, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorIr'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 338, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorCsll'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 339, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IssRetido'), tsSimNao, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 340, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorIss'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 341, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorIssRetido'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 342, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutrasRetencoes'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 343, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BaseCalculo'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 344, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Aliquota'), tsAliquota, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 345, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorLiquidoNfse'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 346, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescontoIncondicionado'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 347, 12)))

tcValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescontoCondicionado'), tsValor, scope=tcValores, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 348, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 334, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 335, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 336, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 337, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 338, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 339, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 341, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 342, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 343, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 344, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 345, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 346, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 347, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 348, 12))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorServicos')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 333, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorDeducoes')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 334, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorPis')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 335, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorCofins')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 336, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorInss')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 337, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorIr')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 338, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorCsll')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 339, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IssRetido')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 340, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorIss')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 341, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorIssRetido')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 342, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutrasRetencoes')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 343, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BaseCalculo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 344, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Aliquota')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 345, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorLiquidoNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 346, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DescontoIncondicionado')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 347, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(tcValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DescontoCondicionado')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 348, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcValores._Automaton = _BuildAutomaton_9()




tcDadosServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Valores'), tcValores, scope=tcDadosServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 353, 12)))

tcDadosServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ItemListaServico'), tsItemListaServico, scope=tcDadosServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 354, 12)))

tcDadosServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoCnae'), tsCodigoCnae, scope=tcDadosServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 355, 12)))

tcDadosServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoTributacaoMunicipio'), tsCodigoTributacao, scope=tcDadosServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 356, 12)))

tcDadosServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Discriminacao'), tsDiscriminacao, scope=tcDadosServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 357, 12)))

tcDadosServico._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), tsCodigoMunicipioIbge, scope=tcDadosServico, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 358, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 355, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 356, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Valores')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 353, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ItemListaServico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 354, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoCnae')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 355, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoTributacaoMunicipio')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 356, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Discriminacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 357, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcDadosServico._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 358, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcDadosServico._Automaton = _BuildAutomaton_10()




tcDadosConstrucaoCivil._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoObra'), tsCodigoObra, scope=tcDadosConstrucaoCivil, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 363, 12)))

tcDadosConstrucaoCivil._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Art'), tsArt, scope=tcDadosConstrucaoCivil, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 364, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosConstrucaoCivil._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoObra')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 363, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcDadosConstrucaoCivil._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Art')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 364, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcDadosConstrucaoCivil._Automaton = _BuildAutomaton_11()




tcDadosPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoPrestador'), tcIdentificacaoPrestador, scope=tcDadosPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 369, 12)))

tcDadosPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial'), tsRazaoSocial, scope=tcDadosPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 370, 12)))

tcDadosPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NomeFantasia'), tsNomeFantasia, scope=tcDadosPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 371, 12)))

tcDadosPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Endereco'), tcEndereco, scope=tcDadosPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 372, 12)))

tcDadosPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contato'), tcContato, scope=tcDadosPrestador, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 373, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 371, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 373, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoPrestador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 369, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RazaoSocial')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 370, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NomeFantasia')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 371, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Endereco')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 372, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tcDadosPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contato')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 373, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcDadosPrestador._Automaton = _BuildAutomaton_12()




tcRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InfRps'), tcInfRps, scope=tcRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 396, 12)))

tcRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=tcRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 397, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InfRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 396, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcRps._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 397, 12))
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
tcRps._Automaton = _BuildAutomaton_13()




tcIdentificacaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numero'), tsNumeroNfse, scope=tcIdentificacaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 402, 12)))

tcIdentificacaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), tsCnpj, scope=tcIdentificacaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 403, 12)))

tcIdentificacaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), tsInscricaoMunicipal, scope=tcIdentificacaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 404, 12)))

tcIdentificacaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio'), tsCodigoMunicipioIbge, scope=tcIdentificacaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 405, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 404, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numero')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 402, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cnpj')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 403, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 404, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcIdentificacaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoMunicipio')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 405, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcIdentificacaoNfse._Automaton = _BuildAutomaton_14()




tcNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InfNfse'), tcInfNfse, scope=tcNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 434, 12)))

tcNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=tcNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 435, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InfNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 434, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 435, 12))
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
tcNfse._Automaton = _BuildAutomaton_15()




tcPedidoCancelamento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InfPedidoCancelamento'), tcInfPedidoCancelamento, scope=tcPedidoCancelamento, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 448, 12)))

tcPedidoCancelamento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=tcPedidoCancelamento, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 449, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcPedidoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InfPedidoCancelamento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 448, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcPedidoCancelamento._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 449, 12))
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
tcPedidoCancelamento._Automaton = _BuildAutomaton_16()




tcCancelamentoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Confirmacao'), tcConfirmacaoCancelamento, scope=tcCancelamentoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 462, 12)))

tcCancelamentoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=tcCancelamentoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcCancelamentoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Confirmacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 462, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcCancelamentoNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 463, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcCancelamentoNfse._Automaton = _BuildAutomaton_17()




tcSubstituicaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubstituicaoNfse'), tcInfSubstituicaoNfse, scope=tcSubstituicaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 475, 12)))

tcSubstituicaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=tcSubstituicaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 476, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcSubstituicaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubstituicaoNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 475, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcSubstituicaoNfse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 476, 12))
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
tcSubstituicaoNfse._Automaton = _BuildAutomaton_18()




tcCompNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nfse'), tcNfse, scope=tcCompNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 481, 12)))

tcCompNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NfseCancelamento'), tcCancelamentoNfse, scope=tcCompNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 482, 12)))

tcCompNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituicao'), tcSubstituicaoNfse, scope=tcCompNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 483, 12)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 482, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 483, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 481, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NfseCancelamento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 482, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tcCompNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituicao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 483, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcCompNfse._Automaton = _BuildAutomaton_19()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MensagemRetorno'), tcMensagemRetorno, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 490, 16)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 490, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_20()




tcMensagemRetorno._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Codigo'), tsCodigoMensagemAlerta, scope=tcMensagemRetorno, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 496, 12)))

tcMensagemRetorno._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mensagem'), tsDescricaoMensagemAlerta, scope=tcMensagemRetorno, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 497, 12)))

tcMensagemRetorno._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Correcao'), tsDescricaoMensagemAlerta, scope=tcMensagemRetorno, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 498, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 498, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Codigo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 496, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mensagem')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 497, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tcMensagemRetorno._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Correcao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 498, 12))
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
tcMensagemRetorno._Automaton = _BuildAutomaton_21()




tcMensagemRetornoLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), tcIdentificacaoRps, scope=tcMensagemRetornoLote, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 503, 12)))

tcMensagemRetornoLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Codigo'), tsCodigoMensagemAlerta, scope=tcMensagemRetornoLote, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 504, 12)))

tcMensagemRetornoLote._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Mensagem'), tsDescricaoMensagemAlerta, scope=tcMensagemRetornoLote, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 505, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcMensagemRetornoLote._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 503, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcMensagemRetornoLote._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Codigo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 504, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcMensagemRetornoLote._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Mensagem')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 505, 12))
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
tcMensagemRetornoLote._Automaton = _BuildAutomaton_22()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rps'), tcRps, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 517, 24)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 517, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_23()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote'), tsNumeroLote, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 530, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataRecebimento'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 531, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Protocolo'), tsNumeroProtocolo, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 532, 20)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 530, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataRecebimento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 531, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Protocolo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 532, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 534, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_24()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LoteRps'), tcLoteRps, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 542, 16)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature'), _ImportedBinding__dsig.SignatureType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/xmldsig-core-schema20020212.xsd', 41, 0)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 543, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LoteRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 542, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dsig, 'Signature')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 543, 16))
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
CTD_ANON_3._Automaton = _BuildAutomaton_25()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote'), tsNumeroLote, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 552, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Situacao'), tsSituacaoLoteRps, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 553, 20)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 552, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Situacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 553, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 555, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_26()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), tcIdentificacaoPrestador, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 563, 16)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Protocolo'), tsNumeroProtocolo, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 564, 16)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prestador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 563, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Protocolo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 564, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_27()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), tcCompNfse, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 572, 16)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 572, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 573, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_28()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), tcIdentificacaoRps, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 581, 16)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), tcIdentificacaoPrestador, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 582, 16)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 581, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prestador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 582, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_29()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaNfse'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 590, 16)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 590, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 597, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_30()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), tcCompNfse, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 593, 28)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 593, 28))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 593, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_31()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), tcIdentificacaoPrestador, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 605, 16)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumeroNfse'), tsNumeroNfse, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 606, 16)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PeriodoEmissao'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 607, 16)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tomador'), tcIdentificacaoTomador, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 615, 16)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico'), tcIdentificacaoIntermediarioServico, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 616, 16)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 606, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 607, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 615, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 616, 16))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prestador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 605, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumeroNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 606, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PeriodoEmissao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 607, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tomador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 615, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 616, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_32()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataInicial'), pyxb.binding.datatypes.date, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 610, 28)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataFinal'), pyxb.binding.datatypes.date, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 611, 28)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataInicial')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 610, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataFinal')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 611, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_33()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaNfse'), CTD_ANON_13, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 624, 16)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 624, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 631, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_34()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompNfse'), tcCompNfse, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 627, 28)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 627, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_35()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), tcIdentificacaoPrestador, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 639, 16)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Protocolo'), tsNumeroProtocolo, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 640, 16)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prestador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 639, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Protocolo')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 640, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_36()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno'), CTD_ANON, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 487, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cancelamento'), tcCancelamentoNfse, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 648, 16)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cancelamento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 648, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaMensagemRetorno')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 649, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_37()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pedido'), tcPedidoCancelamento, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 657, 16)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pedido')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 657, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_38()




tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), tcIdentificacaoRps, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 378, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEmissao'), pyxb.binding.datatypes.dateTime, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 379, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NaturezaOperacao'), tsNaturezaOperacao, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 380, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegimeEspecialTributacao'), tsRegimeEspecialTributacao, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 381, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OptanteSimplesNacional'), tsSimNao, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 382, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncentivadorCultural'), tsSimNao, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 383, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), tsStatusRps, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 384, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RpsSubstituido'), tcIdentificacaoRps, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 385, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Servico'), tcDadosServico, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 386, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Prestador'), tcIdentificacaoPrestador, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 387, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tomador'), tcDadosTomador, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 388, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico'), tcIdentificacaoIntermediarioServico, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 389, 12)))

tcInfRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContrucaoCivil'), tcDadosConstrucaoCivil, scope=tcInfRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 390, 12)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 381, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 385, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 388, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 389, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 390, 12))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 378, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataEmissao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 379, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NaturezaOperacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 380, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RegimeEspecialTributacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 381, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OptanteSimplesNacional')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 382, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncentivadorCultural')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 383, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 384, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RpsSubstituido')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 385, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Servico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 386, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Prestador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 387, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tomador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 388, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 389, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(tcInfRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContrucaoCivil')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 390, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcInfRps._Automaton = _BuildAutomaton_39()




tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Numero'), tsNumeroNfse, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 410, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoVerificacao'), tsCodigoVerificacao, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 411, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEmissao'), pyxb.binding.datatypes.dateTime, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 412, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps'), tcIdentificacaoRps, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 413, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEmissaoRps'), pyxb.binding.datatypes.date, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 414, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NaturezaOperacao'), tsNaturezaOperacao, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 415, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegimeEspecialTributacao'), tsRegimeEspecialTributacao, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 416, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OptanteSimplesNacional'), tsSimNao, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 417, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncentivadorCultural'), tsSimNao, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 418, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Competencia'), pyxb.binding.datatypes.dateTime, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 419, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituida'), tsNumeroNfse, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 420, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutrasInformacoes'), tsOutrasInformacoes, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 421, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Servico'), tcDadosServico, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 422, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValorCredito'), tsValor, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 423, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrestadorServico'), tcDadosPrestador, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 424, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TomadorServico'), tcDadosTomador, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 425, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico'), tcIdentificacaoIntermediarioServico, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 426, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgaoGerador'), tcIdentificacaoOrgaoGerador, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 427, 12)))

tcInfNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContrucaoCivil'), tcDadosConstrucaoCivil, scope=tcInfNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 428, 12)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 413, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 414, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 416, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 420, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 421, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 423, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 425, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 426, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 428, 12))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Numero')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 410, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoVerificacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 411, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataEmissao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 412, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 413, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataEmissaoRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 414, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NaturezaOperacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 415, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RegimeEspecialTributacao')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 416, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OptanteSimplesNacional')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 417, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncentivadorCultural')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 418, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Competencia')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 419, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituida')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 420, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutrasInformacoes')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 421, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Servico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 422, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValorCredito')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 423, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrestadorServico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 424, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TomadorServico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 425, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntermediarioServico')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 426, 12))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgaoGerador')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 427, 12))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(tcInfNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContrucaoCivil')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 428, 12))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcInfNfse._Automaton = _BuildAutomaton_40()




tcInfPedidoCancelamento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoNfse'), tcIdentificacaoNfse, scope=tcInfPedidoCancelamento, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 441, 12)))

tcInfPedidoCancelamento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodigoCancelamento'), tsCodigoCancelamentoNfse, scope=tcInfPedidoCancelamento, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 442, 12)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcInfPedidoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IdentificacaoNfse')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 441, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcInfPedidoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodigoCancelamento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 442, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcInfPedidoCancelamento._Automaton = _BuildAutomaton_41()




tcConfirmacaoCancelamento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pedido'), tcPedidoCancelamento, scope=tcConfirmacaoCancelamento, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 454, 12)))

tcConfirmacaoCancelamento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataHoraCancelamento'), pyxb.binding.datatypes.dateTime, scope=tcConfirmacaoCancelamento, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 455, 12)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pedido')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 454, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcConfirmacaoCancelamento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataHoraCancelamento')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 455, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcConfirmacaoCancelamento._Automaton = _BuildAutomaton_42()




tcInfSubstituicaoNfse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituidora'), tsNumeroNfse, scope=tcInfSubstituicaoNfse, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 469, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcInfSubstituicaoNfse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NfseSubstituidora')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 469, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tcInfSubstituicaoNfse._Automaton = _BuildAutomaton_43()




tcLoteRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote'), tsNumeroLote, scope=tcLoteRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 510, 12)))

tcLoteRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cnpj'), tsCnpj, scope=tcLoteRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 511, 12)))

tcLoteRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal'), tsInscricaoMunicipal, scope=tcLoteRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 512, 12)))

tcLoteRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QuantidadeRps'), tsQuantidadeRps, scope=tcLoteRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 513, 12)))

tcLoteRps._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListaRps'), CTD_ANON_, scope=tcLoteRps, location=pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 514, 12)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumeroLote')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 510, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cnpj')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 511, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InscricaoMunicipal')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 512, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QuantidadeRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 513, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tcLoteRps._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListaRps')), pyxb.utils.utility.Location('/Users/Marcelo/Dev/Projetos/PyNFSe/PyNFSe/XSD/Curitiba/Template/nfse.xsd', 514, 12))
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
tcLoteRps._Automaton = _BuildAutomaton_44()

