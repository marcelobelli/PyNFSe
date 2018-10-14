import pytest
from simple_model import to_dict

from .factories import PrestadorFactory, RPSFactory, ServicoFactory, TomadorFactory


@pytest.fixture
def prestador():
    return PrestadorFactory()


@pytest.fixture
def tomador():
    return TomadorFactory()


@pytest.fixture
def servico():
    return ServicoFactory()


@pytest.fixture
def rps():
    return RPSFactory()


@pytest.fixture
def dados_rps(rps):
    return to_dict(rps)


@pytest.fixture
def dados_lote_rps(dados_rps):
    return {
        'cnpj': '12345678901234',
        'identificador': 'L1',
        'inscricao_municipal': '1234567890',
        'lista_rps': [dados_rps],
        'numero_lote': 1,
    }
