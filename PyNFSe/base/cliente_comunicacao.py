from requests import Session
from zeep import Client
from zeep.transports import Transport


class ClienteComunicacao(Client):

    def __init__(self, url_ambiente, certificado, producao):
        verify = producao
        session = Session()
        session.cert = certificado
        session.verify = verify

        super(ClienteComunicacao, self).__init__(url_ambiente, transport=Transport(session=session))
