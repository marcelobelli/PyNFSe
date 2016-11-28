from zeep import Client

class Comunicacao():
    _url_homologacao = 'https://pilotoisscuritiba.curitiba.pr.gov.br/nfse_ws/NfseWs.asmx?WSDL'
    _url_producao = 'https://isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx?WSDL'
    _url_ambiente = None
    _cliente = None

    def __init__(self, homologacao=False):
        self._url_ambiente = self._url_homologacao if homologacao else self._url_producao
        self._cliente = Client(self._url_ambiente)

    def validar_xml(self, xml):
        return self._cliente.service.ValidarXml(xml)