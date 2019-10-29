from decimal import Decimal

import pytest

from PyNFSe.base.pydantic_models import Prestador, Servico, Tomador, _validate_cnpj, _validate_cpf


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


def test_servico():
    servico = Servico(
        valor_servico=Decimal("1000.00"),
        iss_retido=1,
        item_lista="0107",
        discriminacao="Teste Integração",
        codigo_municipio="4106902",
        aliquota=Decimal("0.02"),
        valor_pis=Decimal("10.00"),
        valor_cofins=Decimal("9.00"),
        valor_inss=Decimal("8.00"),
        valor_ir=Decimal("7.00"),
        valor_csll=Decimal("6.00"),
        outras_retencoes=Decimal("5.00"),
        desconto_incondicionado=Decimal("3.00"),
        desconto_condicionado=Decimal("2.00"),
    )

    total_discount = sum(
        [
            servico.desconto_condicionado,
            servico.desconto_incondicionado,
            servico.outras_retencoes,
            servico.valor_cofins,
            servico.valor_csll,
            servico.valor_inss,
            servico.valor_ir,
            servico.valor_iss_retido,
            servico.valor_pis,
        ]
    )
    expected_valor_iss = Decimal(servico.base_calculo * servico.aliquota).quantize(Decimal("0.01"))
    expected_base_calculo = servico.valor_servico - servico.valor_deducoes - servico.desconto_incondicionado
    expected_valor_liquido = Decimal(servico.valor_servico - total_discount)

    assert servico.base_calculo == expected_base_calculo
    assert servico.valor_iss == expected_valor_iss
    assert servico.valor_liquido == expected_valor_liquido


@pytest.mark.parametrize("iss_retido, valor_iss_retido", ((1, "2.00"), (2, "0")))
def test_servico_iss_retido(iss_retido, valor_iss_retido):
    servico = Servico(
        valor_servico=Decimal("100.00"),
        iss_retido=iss_retido,
        item_lista="0107",
        discriminacao="Teste Integração",
        codigo_municipio="4106902",
        aliquota=Decimal("0.02"),
    )

    assert servico.valor_iss_retido == Decimal(valor_iss_retido)


def test_servico_incorrect_iss_retido_value():
    with pytest.raises(ValueError) as exc:
        Servico(
            valor_servico=Decimal("100.00"),
            iss_retido=3,
            item_lista="0107",
            discriminacao="Teste Integração",
            codigo_municipio="4106902",
            aliquota=Decimal("0.02"),
        )

    assert "ISS Retido deve ser 1 para SIM ou 2 para NÃO." in exc.value.errors()[0]["msg"]


@pytest.mark.parametrize("wrong_cpf", ("123456789012", "1234567890", "1234567890a"))
def test_validate__wrong_cpf(wrong_cpf):
    with pytest.raises(ValueError) as exc:
        _validate_cpf(wrong_cpf)

    assert "CPF deve conter 11 caracteres, sendo todos números." in exc.value.args


@pytest.mark.parametrize("wrong_cnpj", ("1234567890123", "123456789012345", "1234567890123a"))
def test_validate_wrong_cnpj(wrong_cnpj):
    with pytest.raises(ValueError) as exc:
        _validate_cnpj(wrong_cnpj)

    assert "CNPJ deve conter 14 caracteres, sendo todos números." in exc.value.args
