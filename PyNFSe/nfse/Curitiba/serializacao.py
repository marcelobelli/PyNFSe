from PyNFSe.nfse.Curitiba import schema as nfse_schema


def consulta_nfse(prestador, numero_nfse):

    consulta = nfse_schema.ConsultarNfseEnvio()
    consulta.Prestador = id_prestador(prestador)

    consulta.NumeroNfse = numero_nfse

    xml = consulta.toxml(element_name='ConsultarNfseEnvio')
    xml = limpeza_xml(xml)

    return xml


def id_prestador(prestador):

    id_prestador = nfse_schema.tcIdentificacaoPrestador()
    id_prestador.Cnpj = prestador.cnpj
    id_prestador.InscricaoMunicipal = prestador.inscricao_municipal

    return id_prestador


def limpeza_xml(xml):

    return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>',
                                                               '<?xml version="1.0" encoding="UTF-8"?>')
