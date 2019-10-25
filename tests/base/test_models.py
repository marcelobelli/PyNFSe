from datetime import datetime
from decimal import Decimal

import pytest
from simple_model import to_dict
from simple_model.exceptions import ValidationError

from PyNFSe.base import models


def test_prestador():
    prestador = models.Prestador(cnpj="12345678901234", inscricao_municipal="1234567890")

    assert prestador.validate(raise_exception=False) is True


@pytest.mark.parametrize("cnpj_incorreto", ("1234567890123", "123456789012345", "1234567890123a"))
def test_prestador_cnpj_incorreto(cnpj_incorreto):
    with pytest.raises(ValidationError) as exc:
        models.Prestador(cnpj=cnpj_incorreto, inscricao_municipal="1234567890")

    assert "CNPJ deve conter 14 caracteres, sendo todos números." in exc.value.args


@pytest.mark.parametrize(
    "tipo_documento,numero_documento", (("CNPJ", "12345678901234"), ("CPF", "12345678901"))
)
def test_tomador(tipo_documento, numero_documento):
    tomador = models.Tomador(
        razao_social="Nome do Tomador",
        tipo_documento=tipo_documento,
        numero_documento=numero_documento,
        endereco="Rua Getúlio Vargas",
        endereco_numero="1000",
        bairro="Bairro Centro",
        codigo_municipio="4106902",
        uf="PR",
        cep="80000000",
    )

    assert tomador.validate(raise_exception=False) is True


def test_tomador_tipo_documento_incorreto():
    with pytest.raises(ValidationError) as exc:
        models.Tomador(
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

    assert "O tipo de documento do tomador deve ser CPF ou CNPJ." in exc.value.args


@pytest.mark.parametrize("cpf_incorreto", ("123456789012", "1234567890", "1234567890a"))
def test_tomador_numero_cpf_incorreto(cpf_incorreto):
    with pytest.raises(ValidationError) as exc:
        models.Tomador(
            razao_social="Nome do Tomador",
            tipo_documento="CPF",
            numero_documento=cpf_incorreto,
            endereco="Rua Getúlio Vargas",
            endereco_numero="1000",
            bairro="Bairro Centro",
            codigo_municipio="4106902",
            uf="PR",
            cep="80000000",
        )

    assert "CPF deve conter 11 caracteres, sendo todos números." in exc.value.args


@pytest.mark.parametrize("cnpj_incorreto", ("1234567890123", "123456789012345", "1234567890123a"))
def test_tomador_numero_cnpj_incorreto(cnpj_incorreto):
    with pytest.raises(ValidationError) as exc:
        models.Tomador(
            razao_social="Nome do Tomador",
            tipo_documento="CNPJ",
            numero_documento=cnpj_incorreto,
            endereco="Rua Getúlio Vargas",
            endereco_numero="1000",
            bairro="Bairro Centro",
            codigo_municipio="4106902",
            uf="PR",
            cep="80000000",
        )

    assert "CNPJ deve conter 14 caracteres, sendo todos números." in exc.value.args


def test_servico():
    servico = models.Servico(
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
        valor_iss_retido=Decimal("4.00"),
        desconto_incondicionado=Decimal("3.00"),
        desconto_condicionado=Decimal("2.00"),
    )

    assert servico.validate(raise_exception=False) is True
    assert servico.base_calculo == servico._calcular_base_calculo()
    assert servico.valor_iss == servico._calcular_iss()
    assert servico.valor_liquido == servico._calcular_valor_liquido()


def test_servico_iss_retido_incorreto():
    with pytest.raises(ValidationError) as exc:
        models.Servico(
            valor_servico=Decimal("100.00"),
            iss_retido=3,
            item_lista="0107",
            discriminacao="Teste Integração",
            codigo_municipio="4106902",
            aliquota=Decimal("0.02"),
        )

    assert "ISS Retido deve ser 1 para SIM ou 2 para NÃO." in exc.value.args


@pytest.mark.parametrize(
    "valor_servico,valor_deducoes,desconto_incondicionado",
    (("100.00", "10.00", "10.00"), ("50.00", "9.00", "5.00")),
)
def test_servico_calcular_base_calculo(valor_servico, valor_deducoes, desconto_incondicionado):
    servico = models.Servico(
        valor_servico=Decimal(valor_servico),
        iss_retido=2,
        item_lista="0107",
        discriminacao="Teste Integração",
        codigo_municipio="4106902",
        aliquota=Decimal("0.02"),
        valor_deducoes=Decimal(valor_deducoes),
        desconto_incondicionado=Decimal(desconto_incondicionado),
    )

    esperado = Decimal(valor_servico) - Decimal(valor_deducoes) - Decimal(desconto_incondicionado)

    assert servico._calcular_base_calculo() == esperado


@pytest.mark.parametrize(
    "valor_servico,aliquota_iss", (("100.00", "0.02"), ("50.00", "0.05"), ("76.00", "0.07"))
)
def test_servico_calcular_iss(valor_servico, aliquota_iss):
    servico = models.Servico(
        valor_servico=Decimal(valor_servico),
        iss_retido=2,
        item_lista="0107",
        discriminacao="Teste Integração",
        codigo_municipio="4106902",
        aliquota=Decimal(aliquota_iss),
    )

    esperado = Decimal(valor_servico) * Decimal(aliquota_iss)

    assert servico._calcular_iss() == esperado


@pytest.mark.parametrize("iss_retido,valor_iss_retido", ((1, "2.00"), (2, "0")))
def test_servico_iss_retido(iss_retido, valor_iss_retido):
    servico = models.Servico(
        valor_servico=Decimal("100.00"),
        iss_retido=iss_retido,
        item_lista="0107",
        discriminacao="Teste Integração",
        codigo_municipio="4106902",
        aliquota=Decimal("0.02"),
    )

    assert servico.valor_iss_retido == Decimal(valor_iss_retido)


def test_servico_valor_liquido():
    servico = models.Servico(
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
        valor_iss_retido=Decimal("4.00"),
        desconto_incondicionado=Decimal("3.00"),
        desconto_condicionado=Decimal("2.00"),
    )

    descontos = sum(
        [
            servico.valor_pis,
            servico.valor_cofins,
            servico.valor_inss,
            servico.valor_ir,
            servico.valor_csll,
            servico.outras_retencoes,
            servico.valor_iss_retido,
            servico.desconto_incondicionado,
            servico.desconto_condicionado,
        ]
    )

    esperado = servico.valor_servico - descontos

    assert servico._calcular_valor_liquido() == esperado


def test_rps(prestador, tomador, servico):
    rps = models.RPS(
        identificador="N1",
        data_emissao=datetime.today(),
        servico=servico,
        prestador=prestador,
        tomador=tomador,
        simples=1,
        incentivo=2,
        numero=1,
        serie="A1",
        tipo="1",
        natureza_operacao=1,
    )

    assert rps.validate(raise_exception=False) is True


@pytest.mark.parametrize("natureza_operacao_invalida", (0, 7))
def test_rps_natureza_operacao_invalido(natureza_operacao_invalida, prestador, tomador, servico):
    with pytest.raises(ValidationError) as exc:
        models.RPS(
            identificador="N1",
            data_emissao=datetime.today(),
            servico=servico,
            prestador=prestador,
            tomador=tomador,
            simples=1,
            incentivo=2,
            numero=1,
            serie="A1",
            tipo="1",
            natureza_operacao=natureza_operacao_invalida,
        )

    assert "Natureza da Operação deve ser um número entre 1 e 6." in exc.value.args


@pytest.mark.parametrize("regime_especial_invalido", (-1, 5, "A"))
def test_rps_regime_especial_invalido(regime_especial_invalido, prestador, tomador, servico):
    with pytest.raises(ValidationError) as exc:
        models.RPS(
            identificador="N1",
            data_emissao=datetime.today(),
            servico=servico,
            prestador=prestador,
            tomador=tomador,
            simples=1,
            incentivo=2,
            numero=1,
            serie="A1",
            tipo="1",
            natureza_operacao=1,
            regime_especial=regime_especial_invalido,
        )

    assert "Regime Especial deve ser um número entre 0 e 4 ou None." in exc.value.args


def test_rps_criar_a_partir_de_dados(dados_rps):
    rps = models.RPS.criar_a_partir_de_dados(dados_rps)

    assert rps.validate(raise_exception=False) is True
    assert to_dict(rps) == dados_rps


def test_lote_rps(rps):
    lote_rps = models.LoteRPS(
        identificador="L1",
        numero_lote=1,
        cnpj=rps.prestador.cnpj,
        inscricao_municipal=rps.prestador.inscricao_municipal,
        lista_rps=[rps],
    )

    assert lote_rps.validate(raise_exception=False) is True


@pytest.mark.parametrize("cnpj_incorreto", ("1234567890123", "123456789012345", "1234567890123a"))
def test_lote_rps_cnpj_incorreto(cnpj_incorreto, rps):
    with pytest.raises(ValidationError) as exc:
        models.LoteRPS(
            identificador="L1",
            numero_lote=1,
            cnpj=cnpj_incorreto,
            inscricao_municipal=rps.prestador.inscricao_municipal,
            lista_rps=[rps],
        )

    assert "CNPJ deve conter 14 caracteres, sendo todos números." in exc.value.args


def test_lote_rps_criar_a_partir_de_dados(dados_lote_rps):
    lote_rps = models.LoteRPS.criar_a_partir_de_dados(dados_lote_rps)

    assert lote_rps.validate(raise_exception=False) is True
    assert to_dict(lote_rps) == dados_lote_rps


def test_lote_rps_criar_a_partir_de_dados_com_multiplos_rps(dados_lote_rps, dados_rps):
    dados_lote_rps["lista_rps"] = [dados_rps for _ in range(3)]
    lote_rps = models.LoteRPS.criar_a_partir_de_dados(dados_lote_rps)

    assert lote_rps.validate(raise_exception=False) is True
    assert to_dict(lote_rps) == dados_lote_rps
    assert len(lote_rps.lista_rps) == 3
