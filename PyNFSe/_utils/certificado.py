from OpenSSL import crypto
from tempfile import NamedTemporaryFile


def certificado(certificado_pfx, senha):
    with open(certificado_pfx, 'rb') as cert_pfx:
        pkcs12 = crypto.load_pkcs12(cert_pfx.read(), senha.encode())

    cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
    key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

    cert_file = _cria_arquivo_temp(cert)
    key_file = _cria_arquivo_temp(key)

    # certificado = {
    #     'str_certificado': cert,
    #     'arquivo_certificado': cert_file,
    #     'str_chave': key,
    #     'arquivo_chave': key_file
    # }
    certificado = [
        cert,
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