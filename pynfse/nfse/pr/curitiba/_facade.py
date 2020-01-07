from datetime import date

from pynfse.base.certificate import get_certificate
from pynfse.base.models import RPS, LoteRPS, PedidoCancelamentoNFSe, Prestador
from pynfse.base.nfse_signer import NFSeSigner
from pynfse.nfse.pr.curitiba import serializacao as s
from pynfse.nfse.pr.curitiba.comunicacao import Comunicacao


class Facade:
    def __init__(self, certificado_pfx, senha, producao=False):
        namespace = "{http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}"
        url_homologacao = "https://pilotoisscuritiba.curitiba.pr.gov.br/nfse_ws/NfseWs.asmx?WSDL"
        url_producao = "https://isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx?WSDL"

        self.cert, self.cert_file, self.key, self.key_file = get_certificate(certificado_pfx, senha)
        url_ambiente = url_producao if producao else url_homologacao
        cert_file_and_key_file = (self.cert_file.name, self.key_file.name)

        self._assinador = NFSeSigner(self.cert, self.key, namespace)
        self._servicos_wsdl = Comunicacao(url_ambiente, cert_file_and_key_file, producao)

    def consultar_nfse_por_numero(self, prestador_data: dict, nfse_number: str) -> str:
        prestador = Prestador(**prestador_data)
        request_xml = s.consulta_nfse_por_numero(prestador, nfse_number)
        response_xml = self._servicos_wsdl.consultar_nfse(request_xml)

        return response_xml

    def consultar_nfse_por_data(self, prestador_data: dict, data_inicial: date, data_final: date) -> str:
        prestador = Prestador(**prestador_data)
        xml = s.consulta_nfse_por_data(prestador, data_inicial, data_final)
        xml_retorno = self._servicos_wsdl.consultar_nfse(xml)

        return xml_retorno

    def consultar_nfse_por_rps(self, rps_data: dict) -> str:
        rps = RPS(**rps_data)
        xml = s.consulta_nfse_por_rps(rps)
        xml_retorno = self._servicos_wsdl.consultar_nfse_por_rps(xml)

        return xml_retorno

    def consultar_situacao_lote_rps(self, prestador_data: dict, protocolo: str) -> str:
        prestador = Prestador(**prestador_data)
        xml = s.consulta_situacao_lote_rps(prestador, protocolo)
        xml_retorno = self._servicos_wsdl.consultar_situacao_lote_rps(xml)

        return xml_retorno

    def consultar_lote_rps(self, prestador_data: dict, protocolo: str) -> str:
        prestador = Prestador(**prestador_data)
        xml = s.consulta_lote_rps(prestador, protocolo)
        xml_retorno = self._servicos_wsdl.consultar_lote_rps(xml)

        return xml_retorno

    def recepcionar_lote_rps(self, lote_rps_data: dict) -> str:
        lote_rps = LoteRPS(**lote_rps_data)
        xml = s.envio_lote_rps(lote_rps)
        xml = self._assinador.sign_rps_batch(xml)
        xml_retorno = self._servicos_wsdl.recepcionar_lote_rps(xml)

        return xml_retorno

    def cancelar_nfse(self, pedido_cancelamento_nfse_data: dict) -> str:
        pedido_cancelamento_nfse = PedidoCancelamentoNFSe(**pedido_cancelamento_nfse_data)
        xml = s.cancela_nfse(pedido_cancelamento_nfse)
        xml = self._assinador.sign_cancellation_request(xml)
        xml_retorno = self._servicos_wsdl.cancelar_nfse(xml)

        return xml_retorno

    def validar_xml(self, xml: str) -> str:
        retorno = self._servicos_wsdl.validar_xml(xml)

        return retorno
