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


def consulta_nfse_por_rps(dict_rps):
    rps = RPS(**dict_rps)
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
    id_nfse.Cnpj = pedido_cancelamento_nfse.prestador['cnpj']
    id_nfse.InscricaoMunicipal = pedido_cancelamento_nfse.prestador['inscricao_municipal']
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


def _serial_prestador(dict_prestador):
    prestador = Prestador(**dict_prestador)

    id_prestador = nfse_schema.tcIdentificacaoPrestador()
    id_prestador.Cnpj = prestador.cnpj
    id_prestador.InscricaoMunicipal = prestador.inscricao_municipal

    return id_prestador


def _serial_tomador(dict_tomador):
    tomador = Tomador(**dict_tomador)

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


def _serial_servico(dict_servico):
    servico = Servico(**dict_servico)

    valores_servico = nfse_schema.tcValores()
    valores_servico.ValorServicos = servico.valor_servico
    valores_servico.BaseCalculo = servico.base_calculo
    valores_servico.IssRetido = servico.iss_retido
    valores_servico.ValorLiquidoNfse = servico.valor_liquido
    valores_servico.ValorDeducoes = servico.valor_deducoes if servico.valor_deducoes else None
    valores_servico.ValorPis = servico.valor_pis if servico.valor_pis else None
    valores_servico.ValorCofins = servico.valor_cofins if servico.valor_cofins else None
    valores_servico.ValorInss = servico.valor_inss if servico.valor_inss else None
    valores_servico.ValorIr = servico.valor_ir if servico.valor_ir else None
    valores_servico.ValorCsll = servico.valor_csll if servico.valor_csll else None
    valores_servico.ValorIss = servico.valor_iss if servico.valor_iss else None
    valores_servico.ValorIssRetido = servico.valor_iss_retido if servico.valor_iss_retido else None
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


def _serial_rps(dict_rps):
    rps = RPS(**dict_rps)

    id_rps = nfse_schema.tcIdentificacaoRps()
    id_rps.Numero = rps.numero
    id_rps.Serie = rps.serie
    id_rps.Tipo = rps.tipo

    inf_rps = nfse_schema.tcInfRps()
    inf_rps.IdentificacaoRps = id_rps
    inf_rps.DataEmissao = rps.data_emissao.strftime('%Y-%m-%dT%H:%M:%S')
    inf_rps.NaturezaOperacao = rps.natureza_operacao
    inf_rps.RegimeEspecialTributacao = rps.regime_especial if rps.regime_especial else None
    inf_rps.OptanteSimplesNacional = rps.simples
    inf_rps.IncentivadorCultural = rps.incentivo
    inf_rps.Status = 1
    inf_rps.Servico = _serial_servico(rps.servico)
    inf_rps.Prestador = _serial_prestador(rps.prestador)
    inf_rps.Tomador = _serial_tomador(rps.tomador)
    inf_rps.id = rps.identificador

    serial_rps = nfse_schema.tcRps()
    serial_rps.InfRps = inf_rps
    
    return serial_rps


def _limpeza_xml(xml):

    return xml.replace('ns1:', '').replace(':ns1', '').replace('<?xml version="1.0" ?>',
                                                               '<?xml version="1.0" encoding="UTF-8"?>')
