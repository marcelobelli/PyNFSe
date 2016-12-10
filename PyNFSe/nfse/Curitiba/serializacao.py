from PyNFSe.nfse.Curitiba import schema as nfse_schema


def consulta_nfse(prestador, numero_nfse):

    consulta = nfse_schema.ConsultarNfseEnvio()
    consulta.Prestador = _serial_prestador(prestador)

    consulta.NumeroNfse = numero_nfse

    xml = consulta.toxml(element_name='ConsultarNfseEnvio')
    xml = _limpeza_xml(xml)

    return xml


def _serial_prestador(prestador):

    id_prestador = nfse_schema.tcIdentificacaoPrestador()
    id_prestador.Cnpj = prestador.cnpj
    id_prestador.InscricaoMunicipal = prestador.inscricao_municipal

    return id_prestador


def _serial_tomador(tomador):

    endereco_tomador = nfse_schema.tcEndereco()
    endereco_tomador.Endereco = tomador.endereco
    endereco_tomador.Complemento = tomador.endereco_complemento if tomador.endereco_complemento else None
    endereco_tomador.Numero = tomador.endereco_numero
    endereco_tomador.Bairro = tomador.bairro
    endereco_tomador.CodigoMunicipio = tomador.codigo_municipio if tomador.codigo_municipio else None
    endereco_tomador.Uf = tomador.uf
    endereco_tomador.Cep = tomador.cep

    id_tomador = nfse_schema.tcIdentificacaoTomador()
    id_tomador.CpfCnpj = tomador.numero_documento
    id_tomador.InscricaoMunicipal = tomador.inscricao_municipal if tomador.inscricao_municipal else None

    serial_tomador = nfse_schema.tcDadosTomador()
    serial_tomador.IdentificacaoTomador = id_tomador
    serial_tomador.RazaoSocial = tomador.razao_social
    serial_tomador.Endereco = endereco_tomador

    if tomador.telefone or tomador.email:
        serial_tomador.Contato = nfse_schema.tcContato()
        serial_tomador.Contato.Telefone = tomador.telefone if tomador.telefone else None
        serial_tomador.Contato.Email = tomador.email if tomador.email else None

    return serial_tomador


def _limpeza_xml(xml):

    return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>',
                                                               '<?xml version="1.0" encoding="UTF-8"?>')
