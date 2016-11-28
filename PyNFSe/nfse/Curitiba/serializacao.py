from importlib import import_module


class Serializacao():

    def __init__(self):
        global nfse_schema
        nfse_schema = import_module('PyNFSe.nfse.Curitiba.schema')

    def consultar_nfse(self, emissor, numero_nfse):
        id_emissor = nfse_schema.tcIdentificacaoPrestador()
        id_emissor.Cnpj = emissor.cnpj
        id_emissor.InscricaoMunicipal = emissor.inscricao_municipal

        consulta = nfse_schema.ConsultarNfseEnvio()
        consulta.Prestador = id_emissor

        consulta.NumeroNfse = numero_nfse

        xml = consulta.toxml(element_name='ConsultarNfseEnvio').replace('ns1:', '').replace(':ns1', '')\
            .replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="UTF-8"?>')

        return xml