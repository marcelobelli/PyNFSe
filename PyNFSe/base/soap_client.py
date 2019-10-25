from requests import Session
from zeep import Client
from zeep.transports import Transport


class NFSeSoapClient(Client):

    def __init__(self, url_env: str, certificate: tuple, is_production: bool = False):
        session = Session()
        session.cert = certificate
        session.verify = is_production

        super().__init__(url_env, transport=Transport(session=session))
