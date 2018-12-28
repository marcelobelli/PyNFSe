from tempfile import NamedTemporaryFile
from typing import Tuple

from OpenSSL import crypto


def get_certificate(cfx_certificate_filepath: str, password: str) -> Tuple:
    with open(cfx_certificate_filepath, 'rb') as cert_pfx:
        pkcs12 = crypto.load_pkcs12(cert_pfx.read(), password.encode())

    cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

    cert_ca = b''

    if pkcs12.get_ca_certificates():
        for ca in pkcs12.get_ca_certificates():
            cert_ca = crypto.dump_certificate(crypto.FILETYPE_PEM, ca) + cert_ca

    cert_ca = cert + cert_ca

    cert_file = _create_temp_file(cert_ca)
    key_file = _create_temp_file(key)

    return cert_ca, cert_file, key, key_file


def _create_temp_file(content: bytes):
    temp_file = NamedTemporaryFile()
    temp_file.write(content)
    temp_file.seek(0)

    return temp_file
