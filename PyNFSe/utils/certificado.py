from tempfile import NamedTemporaryFile

from OpenSSL import crypto


def certificado(certificado_pfx, senha):
    with open(certificado_pfx, 'rb') as cert_pfx:
        pkcs12 = crypto.load_pkcs12(cert_pfx.read(), senha.encode())

    cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

    cert_ca = b''

    if pkcs12.get_ca_certificates():
        for ca in pkcs12.get_ca_certificates():
            cert_ca = crypto.dump_certificate(crypto.FILETYPE_PEM, ca) + cert_ca

    cert_ca = cert + cert_ca

    cert_file = _cria_arquivo_temp(cert_ca)
    key_file = _cria_arquivo_temp(key)

    certificado = [
        cert_ca,
        cert_file,
        key,
        key_file
    ]

    return certificado

def _cria_arquivo_temp(str_arquivo):
    arquivo = NamedTemporaryFile()
    arquivo.write(str_arquivo)
    arquivo.seek(0)

    return arquivo
