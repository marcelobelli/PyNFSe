from PyNFSe.base.soap_client import NFSeSoapClient


class Comunicacao:

    def __init__(self, url_ambiente, certificado, producao):
        self._cliente = NFSeSoapClient(url_ambiente, certificado, producao)

    def validar_xml(self, xml):
        return self._cliente.service.ValidarXml(xml)

    def consultar_nfse(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarNfse', xml)

    def consultar_nfse_por_rps(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarNfsePorRps', xml)

    def consultar_situacao_lote_rps(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarSituacaoLoteRps', xml)

    def consultar_lote_rps(self, xml):
        return self._cliente.service.RecepcionarXml('ConsultarLoteRps', xml)

    def recepcionar_lote_rps(self, xml):
        return self._cliente.service.RecepcionarXml('RecepcionarLoteRps', xml)

    def cancelar_nfse(self, xml):
        return self._cliente.service.RecepcionarXml('CancelarNfse', xml)

    def recepcionar_xml(self, metodo, xml):
        return self._cliente.service.RecepcionarXml(metodo, xml)
