from zeep import Client

from PyNFSe.utils.transports import TransportWithCert


class Comunicacao(object):

    def __init__(self, url_homolocacao, url_producao, homologacao=False, certificado=None):
        self.url_homologacao = url_homolocacao
        self.url_producao = url_producao
        self.homologacao = homologacao
        self.certificado = certificado
        self.set_cliente()

    def set_cliente(self):
        url_ambiente = self.url_homologacao if self.homologacao else self.url_producao
        verify = False if self.homologacao else True

        self._cliente = Client(url_ambiente, transport=TransportWithCert(verify=verify, cert=self.certificado))

    def validar_xml(self, xml):
        return self._cliente.service.ValidarXml(xml)

    def consultar_nfse(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarNfse', xml)

    def consultar_situacao_lote_rps(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarSituacaoLoteRps', xml)

    def consultar_lote_rps(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarLoteRps', xml)

    def consultar_nfse_por_rps(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarNfsePorRps', xml)

    def enviar_lote_rps(self, xml):
        return self._cliente.service.RecepcionarXml('RecepcionarLoteRps', xml)

    def cancelar_nfse(self, xml):
        return self._cliente.service.RecepcionarXml('CancelarNfse', xml)
