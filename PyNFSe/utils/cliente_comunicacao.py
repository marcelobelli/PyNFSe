from zeep import Client

from .transports import TransportWithCert


class ClienteComunicacao(Client):

    def __init__(self, url_ambiente , homologacao, certificado):
        verify = False if homologacao else True
        transport = TransportWithCert(verify=verify, cert=certificado)
        super(ClienteComunicacao, self).__init__(url_ambiente, transport=transport)