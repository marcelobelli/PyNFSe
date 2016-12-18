from PyNFSe._utils.certificado import certificado as c
from PyNFSe._utils.assinatura import Assinatura
from PyNFSe.nfse.pr.curitiba import serializacao as s
from PyNFSe.nfse.pr.curitiba.comunicacao import Comunicacao
from PyNFSe._entidades import Prestador, Tomador, Servico, RPS, LoteRPS, PedidoCancelamentoNFSe


class Servicos:

    def __init__(self, certificado_pfx, senha, homologacao=False):
        namespace = '{http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}'
        url_homologacao = 'https://pilotoisscuritiba.curitiba.pr.gov.br/nfse_ws/NfseWs.asmx?WSDL'
        url_producao = 'https://isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx?WSDL'

        cert, cert_file, key, key_file = c(certificado_pfx, senha)
        url_ambiente = url_homologacao if homologacao else url_producao

        self._assinador = Assinatura(cert, key, namespace)
        self._servicos_wsdl = Comunicacao(url_ambiente, homologacao, (cert_file.name, key_file.name))

    def consultar_nfse_por_numero(self, dict_prestador, numero_nfse):
        prestador = Prestador(**dict_prestador)
        xml = s.consulta_nfse_por_numero(prestador, numero_nfse)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('ConsultarNfse', xml)

        return xml_retorno

    def consultar_nfse_por_data(self, dict_prestador, data_inicial, data_final):
        prestador = Prestador(**dict_prestador)
        xml = s.consulta_nfse_por_data(prestador, data_inicial, data_final)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('ConsultarNfse', xml)

        return xml_retorno

    def consultar_nfse_por_rps(self, dict_rps):
        rps = RPS(**dict_rps)
        xml = s.consulta_nfse_por_rps(rps)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('ConsultarNfsePorRps', xml)

        return xml_retorno

    def consultar_situacao_lote_rps(self, dict_prestador, protocolo):
        prestador = Prestador(**dict_prestador)
        xml = s.consulta_lote_rps(prestador, protocolo)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('ConsultarSituacaoLoteRps', xml)

        return xml_retorno

    def consultar_lote_rps(self, dict_prestador, protocolo):
        prestador = Prestador(**dict_prestador)
        xml = s.consulta_lote_rps(prestador, protocolo)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('ConsultarLoteRps', xml)

        return xml_retorno

    def recepcionar_lote_rps(self, dict_lote_rps):
        lote_rps = LoteRPS(**dict_lote_rps)
        xml = s.envio_lote_rps(lote_rps)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('RecepcionarLoteRps', xml)

        return xml_retorno

    def cancelar_nfse(self, dict_pedido_cancelamento_nfse):
        pedido_cancelamento_nfse = PedidoCancelamentoNFSe(**dict_pedido_cancelamento_nfse)
        xml = s.cancela_nfse(pedido_cancelamento_nfse)
        xml_retorno = self._servicos_wsdl.recepcionar_xml('CancelarNfse', xml)

        return xml_retorno