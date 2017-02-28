from requests import Session
from zeep import Client
from zeep.transports import Transport
from .transports import TransportWithCert


class ClienteComunicacao(Client):

    def __init__(self, url_ambiente , homologacao, certificado):
        verify = False if homologacao else True
        session = Session()
        session.cert = certificado
        session.verify = verify
        
        super(ClienteComunicacao, self).__init__(url_ambiente, transport=Transport(session=session))
        
        # transport = TransportWithCert(verify=verify, cert=certificado)
        # super(ClienteComunicacao, self).__init__(url_ambiente, transport=transport)