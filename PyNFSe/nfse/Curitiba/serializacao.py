#from importlib import import_module
from PyNFSe.nfse.Curitiba import schema as nfse_schema

class Serializacao(object):

    #def __init__(self):
        #global nfse_schema
        #nfse_schema = import_module('PyNFSe.nfse.Curitiba.schema')

    def consulta_nfse(self, prestador, numero_nfse):
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.Cnpj = prestador.cnpj
        id_prestador.InscricaoMunicipal = prestador.inscricao_municipal

        consulta = nfse_schema.ConsultarNfseEnvio()
        consulta.Prestador = id_prestador

        consulta.NumeroNfse = numero_nfse

        xml = consulta.toxml(element_name='ConsultarNfseEnvio')
        xml = self.limpeza_xml(xml)

        return xml






    def limpeza_xml(self, xml):

        return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>',
                                                                   '<?xml version="1.0" encoding="UTF-8"?>')