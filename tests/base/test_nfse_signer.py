import pytest
from PyNFSe.base.certificado import certificado
from PyNFSe.base.nfse_signer import NFSeSigner


@pytest.fixture
def signer(certificate_file_path, certificate_password):
    namespace = '{http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}'
    cert, _, key, _ = certificado(certificate_file_path, certificate_password)
    return NFSeSigner(cert, key, namespace)


def test_sign_rps_batch(xml_rps, xml_rps_signed, signer):
    assert signer.sign_rps_batch(xml_rps) == xml_rps_signed


def test_sign_canceled_nfse(xml_canceled_nfse, xml_canceled_nfse_signed, signer):
    assert signer.sign_cancellation_request(xml_canceled_nfse) == xml_canceled_nfse_signed
