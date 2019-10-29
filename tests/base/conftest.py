import os.path

import pytest
from simple_model import to_dict

from .factories import (
    PrestadorFactory,
    PrestadorPydanticFactory,
    RPSFactory,
    RPSPydanticFactory,
    ServicoFactory,
    ServicoPydanticFactory,
    TomadorFactory,
    TomadorPydanticFactory,
)

file_path = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def prestador():
    return PrestadorFactory()


@pytest.fixture
def prestador_pydantic():
    return PrestadorPydanticFactory()


@pytest.fixture
def tomador():
    return TomadorFactory()


@pytest.fixture
def tomador_pydantic():
    return TomadorPydanticFactory()


@pytest.fixture
def servico():
    return ServicoFactory()


@pytest.fixture
def servico_pydantic():
    return ServicoPydanticFactory()


@pytest.fixture
def rps():
    return RPSFactory()


@pytest.fixture
def rps_pydantic():
    return RPSPydanticFactory()


@pytest.fixture
def dados_rps(rps):
    return to_dict(rps)


@pytest.fixture
def dados_lote_rps(dados_rps):
    return {
        "cnpj": "12345678901234",
        "identificador": "L1",
        "inscricao_municipal": "1234567890",
        "lista_rps": [dados_rps],
        "numero_lote": 1,
    }


@pytest.fixture
def xml_rps():
    xml_path = os.path.join(file_path, "fixtures/EnviarLoteRpsEnvio.xml")
    with open(xml_path, "r") as xml:
        return xml.read()


@pytest.fixture
def xml_rps_signed():
    xml_path = os.path.join(file_path, "fixtures/EnviarLoteRpsEnvio-Signed.xml")
    with open(xml_path, "r") as xml:
        return xml.read()


@pytest.fixture
def xml_canceled_nfse():
    xml_path = os.path.join(file_path, "fixtures/CancelarNfseEnvio.xml")
    with open(xml_path, "r") as xml:
        return xml.read()


@pytest.fixture
def xml_canceled_nfse_signed():
    xml_path = os.path.join(file_path, "fixtures/CancelarNfseEnvio-Signed.xml")
    with open(xml_path, "r") as xml:
        return xml.read()


@pytest.fixture
def certificate_file_path():
    return os.path.join(file_path, "fixtures/certificate.pfx")


@pytest.fixture
def certificate_password():
    return "123456"
