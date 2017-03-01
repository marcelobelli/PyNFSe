from PyNFSe.utils.cliente_comunicacao import ClienteComunicacao


class Comunicacao(object):

    def __init__(self, url_ambiente, certificado, producao):
        self._cliente = ClienteComunicacao(url_ambiente, certificado, producao)

    def validar_xml(self, xml):
        return self._cliente.service.ValidarXml(xml)

    def recepcionar_xml(self, metodo, xml):
        return self._cliente.service.RecepcionarXml(metodo, xml)
