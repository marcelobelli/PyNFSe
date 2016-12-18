import requests

from zeep.utils import NotSet
from zeep.transports import Transport


class TransportWithCert(Transport):
    def __init__(self, cache=NotSet, timeout=300, operation_timeout=None, verify=True,
                 http_auth=None, cert=None):
        self.cert = cert
        super(TransportWithCert, self).__init__(cache=cache, timeout=timeout,
                                                operation_timeout=operation_timeout,
                                                verify=verify)

    def create_session(self):
        session = requests.Session()
        session.cert = self.cert
        session.verify = self.http_verify
        session.auth = self.http_auth
        session.headers = self.http_headers
        return session
