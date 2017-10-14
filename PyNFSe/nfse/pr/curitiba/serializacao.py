from pyxb import BIND

from PyNFSe.nfse.pr.curitiba import _schema as nfse_schema
from PyNFSe.utils.entidades import Prestador, Tomador, Servico, RPS, LoteRPS, PedidoCancelamentoNFSe


def consulta_nfse_por_numero(prestador, numero_nfse):

    consulta = nfse_schema.ConsultarNfseEnvio()
    consulta.Prestador = _serial_prestador(prestador)

    consulta.NumeroNfse = numero_nfse

    xml = consulta.toxml(element_name='ConsultarNfseEnvio')
    xml = _limpeza_xml(xml)

    return xml


def consulta_nfse_por_data(prestador, data_inicial, data_final):

    consulta = nfse_schema.ConsultarNfseEnvio()
    consulta.Prestador = _serial_prestador(prestador)

    consulta.PeriodoEmissao = BIND()

    consulta.PeriodoEmissao.DataInicial = data_inicial
    consulta.PeriodoEmissao.DataFinal = data_final

    xml = consulta.toxml()
    xml = _limpeza_xml(xml)

    return xml


def consulta_nfse_por_rps(rps):

    id_rps = nfse_schema.tcIdentificacaoRps()
    id_rps.Numero = rps.numero
    id_rps.Serie = rps.serie
    id_rps.Tipo = rps.tipo

    id_prestador = _serial_prestador(rps.prestador)

    consulta = nfse_schema.ConsultarNfseRpsEnvio()
    consulta.IdentificacaoRps = id_rps
    consulta.Prestador = id_prestador

    xml = consulta.toxml()
    xml = _limpeza_xml(xml)

    return xml


def consulta_situacao_lote_rps(prestador, protocolo):

    consulta = nfse_schema.ConsultarSituacaoLoteRpsEnvio()
    consulta.Prestador = _serial_prestador(prestador)
    consulta.Protocolo = protocolo

    xml = consulta.toxml()
    xml = _limpeza_xml(xml)

    return xml


def consulta_lote_rps(prestador, protocolo):

    consulta = nfse_schema.ConsultarLoteRpsEnvio()
    consulta.Prestador = _serial_prestador(prestador)
    consulta.Protocolo = protocolo

    xml = consulta.toxml()
    xml = _limpeza_xml(xml)

    return xml


def envio_lote_rps(dict_lote_rps):
    lote_rps = LoteRPS(**dict_lote_rps)

    serial_lote_rps = nfse_schema.tcLoteRps()
    serial_lote_rps.NumeroLote = lote_rps.numero_lote
    serial_lote_rps.id = lote_rps.identificador
    serial_lote_rps.Cnpj = lote_rps.cnpj
    serial_lote_rps.InscricaoMunicipal = lote_rps.inscricao_municipal
    serial_lote_rps.QuantidadeRps = len(lote_rps.lista_rps)
    serial_lote_rps.ListaRps = BIND()
    for rps in lote_rps.lista_rps:
        serial_lote_rps.ListaRps.append(_serial_rps(rps))

    serial_enviar_lote = nfse_schema.EnviarLoteRpsEnvio()
    serial_enviar_lote.LoteRps = serial_lote_rps

    xml = serial_enviar_lote.toxml()
    xml = _limpeza_xml(xml)

    return xml


def cancela_nfse(dict_pedido_cancelamento_nfse):
    pedido_cancelamento_nfse = PedidoCancelamentoNFSe(**dict_pedido_cancelamento_nfse)

    id_nfse = nfse_schema.tcIdentificacaoNfse()
    id_nfse.Numero = pedido_cancelamento_nfse.numero_nota
    id_nfse.Cnpj = pedido_cancelamento_nfse.prestador.cnpj
    id_nfse.InscricaoMunicipal = pedido_cancelamento_nfse.prestador.inscricao_municipal
    id_nfse.CodigoMunicipio = pedido_cancelamento_nfse.codigo_municipio

    info_pedido = nfse_schema.tcInfPedidoCancelamento()
    info_pedido.IdentificacaoNfse = id_nfse
    info_pedido.id = pedido_cancelamento_nfse.identificador
    info_pedido.CodigoCancelamento = pedido_cancelamento_nfse.codigo_cancelamento

    pedido = nfse_schema.tcPedidoCancelamento()
    pedido.InfPedidoCancelamento = info_pedido

    cancelar = nfse_schema.CancelarNfseEnvio()
    cancelar.Pedido = pedido

    xml = cancelar.toxml()
    xml = _limpeza_xml(xml)

    return xml


def _serial_prestador(prestador):

    id_prestador = nfse_schema.tcIdentificacaoPrestador()
    id_prestador_schema = {
        'Cnpj': prestador.cnpj,
        'InscricaoMunicipal': prestador.inscricao_municipal
    }
    for key, value in id_prestador_schema.items():
        setattr(id_prestador, key, value)

    return id_prestador


def _serial_tomador(tomador):
    endereco_tomador = nfse_schema.tcEndereco()
    endereco_tomador_schema = {
        'Endereco': tomador.endereco,
        'Complemento': tomador.endereco_complemento,
        'Numero': tomador.endereco_numero,
        'Bairro': tomador.bairro,
        'CodigoMunicipio': tomador.codigo_municipio,
        'Uf': tomador.uf,
        'Cep': tomador.cep,
    }
    for key, value in endereco_tomador_schema.items():
        setattr(endereco_tomador, key, value)

    id_tomador = nfse_schema.tcIdentificacaoTomador()
    id_tomador_schema = {
        'CpfCnpj': tomador.numero_documento,
        'InscricaoMunicipal': tomador.inscricao_municipal,
    }
    for key, value in id_tomador_schema.items():
        setattr(id_tomador, key, value)

    serial_tomador = nfse_schema.tcDadosTomador()
    serial_tomador_schema = {
        'IdentificacaoTomador': id_tomador,
        'RazaoSocial': tomador.razao_social,
        'Endereco': endereco_tomador,
    }
    for key, value in serial_tomador_schema.items():
        setattr(serial_tomador, key, value)

    if tomador.telefone or tomador.email:
        serial_tomador.Contato = nfse_schema.tcContato()
        contato_schema = {
            'Telefone': tomador.telefone,
            'Email': tomador.email
        }
        for key, value in contato_schema.items():
            setattr(serial_tomador.Contato, key, value)

    return serial_tomador


def _serial_servico(servico):
    valores_servico = nfse_schema.tcValores()
    valores_servico_schema = {
        'ValorServicos': servico.valor_servico,
        'BaseCalculo': servico.base_calculo,
        'IssRetido': servico.iss_retido,
        'ValorLiquidoNfse': servico.valor_liquido,
        'ValorDeducoes': servico.valor_deducoes if servico.valor_deducoes else None,
        'ValorPis': servico.valor_pis if servico.valor_pis else None,
        'ValorCofins': servico.valor_cofins if servico.valor_cofins else None,
        'ValorInss': servico.valor_inss if servico.valor_inss else None,
        'ValorIr': servico.valor_ir if servico.valor_ir else None,
        'ValorCsll': servico.valor_csll if servico.valor_csll else None,
        'ValorIss': servico.valor_iss if servico.valor_iss else None,
        'ValorIssRetido': servico.valor_iss_retido if servico.valor_iss_retido else None,
        'OutrasRetencoes': servico.outras_retencoes if servico.outras_retencoes else None,
        'Aliquota': servico.aliquota if servico.aliquota else None,
        'DescontoIncondicionado': servico.desconto_incondicionado if servico.desconto_incondicionado else None,
        'DescontoCondicionado': servico.desconto_condicionado if servico.desconto_condicionado else None,
    }
    for key, value in valores_servico_schema.items():
        setattr(valores_servico, key, value)

    serial_servico = nfse_schema.tcDadosServico()
    serial_servico_schema = {
        'Valores': valores_servico,
        'ItemListaServico': servico.item_lista,
        'Discriminacao': servico.discriminacao,
        'CodigoMunicipio': servico.codigo_municipio,
        'CodigoCnae': servico.codigo_cnae,
        'CodigoTributacaoMunicipio': servico.codigo_tributacao_municipio,
    }
    for key, value in serial_servico_schema.items():
        setattr(serial_servico, key, value)

    return serial_servico


def _serial_rps(rps):
    id_rps = nfse_schema.tcIdentificacaoRps()
    id_rps_schema = {
        'Numero': rps.numero,
        'Serie': rps.serie,
        'Tipo': rps.tipo,
    }
    for key, value in id_rps_schema.items():
        setattr(id_rps, key, value)

    inf_rps = nfse_schema.tcInfRps()
    inf_rps_schema = {
        'IdentificacaoRps': id_rps,
        'DataEmissao': rps.data_emissao.strftime('%Y-%m-%dT%H:%M:%S'),
        'NaturezaOperacao': rps.natureza_operacao,
        'RegimeEspecialTributacao': rps.regime_especial,
        'OptanteSimplesNacional': rps.simples,
        'IncentivadorCultural': rps.incentivo,
        'Status': 1,
        'Servico': _serial_servico(rps.servico),
        'Prestador': _serial_prestador(rps.prestador),
        'Tomador': _serial_tomador(rps.tomador),
        'id': rps.identificador,
    }
    for key, value in inf_rps_schema.items():
        setattr(inf_rps, key, value)

    serial_rps = nfse_schema.tcRps()
    serial_rps.InfRps = inf_rps
    
    return serial_rps


def _limpeza_xml(xml):

    return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>',
                                                               '<?xml version="1.0" encoding="UTF-8"?>')
