import pytest

from PyNFSe.base.pydantic_models import Prestador, Tomador, _validate_cnpj, _validate_cpf


def test_prestador_incorrect_cnpj():
    with pytest.raises(ValueError):
        Prestador(cnpj="1234567890123", inscricao_municipal="987654321")


def test_tomador_incorrect_tipo_documento():
    with pytest.raises(ValueError):
        Tomador(
            razao_social="Nome do Tomador",
            tipo_documento="ABC",
            numero_documento="12345678901",
            endereco="Rua Getúlio Vargas",
            endereco_numero="1000",
            bairro="Bairro Centro",
            codigo_municipio="4106902",
            uf="PR",
            cep="80000000",
        )


def test_tomador_invalid_cpf_number():
    with pytest.raises(ValueError):
        Tomador(
            razao_social="Nome do Tomador",
            tipo_documento="CPF",
            numero_documento="1234567890",
            endereco="Rua Getúlio Vargas",
            endereco_numero="1000",
            bairro="Bairro Centro",
            codigo_municipio="4106902",
            uf="PR",
            cep="80000000",
        )


def test_tomador_invalid_cnpj_number():
    with pytest.raises(ValueError):
        Tomador(
            razao_social="Nome do Tomador",
            tipo_documento="CNPJ",
            numero_documento="1234567890123",
            endereco="Rua Getúlio Vargas",
            endereco_numero="1000",
            bairro="Bairro Centro",
            codigo_municipio="4106902",
            uf="PR",
            cep="80000000",
        )


@pytest.mark.parametrize("wrong_cpf", ("123456789012", "1234567890", "1234567890a"))
def test_validate__wrongcpf(wrong_cpf):
    with pytest.raises(ValueError) as exc:
        _validate_cpf(wrong_cpf)

    assert "CPF deve conter 11 caracteres, sendo todos números." in exc.value.args


@pytest.mark.parametrize("wrong_cnpj", ("1234567890123", "123456789012345", "1234567890123a"))
def test_validate_wrong_cnpj(wrong_cnpj):
    with pytest.raises(ValueError) as exc:
        _validate_cnpj(wrong_cnpj)

    assert "CNPJ deve conter 14 caracteres, sendo todos números." in exc.value.args
