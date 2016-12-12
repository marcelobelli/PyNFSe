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


def _serial_servico(servico):
    
    valores_servico = nfse_schema.tcValores()
    valores_servico.ValorServicos = servico.valor_servico
    valores_servico.IssRetido = servico.iss_retido
    valores_servico.ValorDeducoes = servico.valor_servico if servico.valor_servico else None
    valores_servico.ValorPis = servico.valor_pis if servico.valor_pis else None
    valores_servico.ValorCofins = servico.valor_cofins if servico.valor_cofins else None
    valores_servico.ValorInss = servico.valor_inss if servico.valor_inss else None
    valores_servico.ValorIr = servico.valor_ir if servico.valor_ir else None
    valores_servico.ValorCsll = servico.valor_csll if servico.valor_csll else None
    valores_servico.ValorIss = servico.valor_iss if servico.valor_iss else None
    valores_servico.ValorIssRetido = servico.valor_iss_retido if servico.valor_iss_retido else None
    valores_servico.ValorLiquidoNfse = servico.valor_liquido if servico.valor_liquido else None
    valores_servico.OutrasRetencoes = servico.outras_retencoes if servico.outras_retencoes else None
    valores_servico.Aliquota = servico.aliquota if servico.aliquota else None
    valores_servico.DescontoIncondicionado = servico.desconto_incondicionado if servico.desconto_incondicionado else None
    valores_servico.DescontoCondicionado = servico.desconto_condicionado if servico.desconto_condicionado else None

    serial_servico = nfse_schema.tcDadosServico()
    serial_servico.Valores = valores_servico
    serial_servico.ItemListaServico = servico.item_lista
    serial_servico.Discriminacao = servico.discriminacao
    serial_servico.CodigoMunicipio = servico.codigo_municipio
    serial_servico.CodigoCnae = servico.codigo_cnae if servico.codigo_cnae else None
    serial_servico.CodigoTributacaoMunicipio = servico.codigo_tributacao_municipio if servico.codigo_tributacao_municipio else None

    return serial_servico


def _limpeza_xml(xml):

    return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>',
                                                               '<?xml version="1.0" encoding="UTF-8"?>')
