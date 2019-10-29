from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, validator


class Prestador(BaseModel):
    cnpj: str
    inscricao_municipal: str

    @validator("cnpj")
    def cnpj_must_have_14_digits(cls, value):
        return _validate_cnpj(value)


class Tomador(BaseModel):
    tipo_documento: str
    numero_documento: str
    razao_social: str
    bairro: str
    cep: str
    codigo_municipio: str
    endereco: str
    endereco_numero: str
    uf: str

    inscricao_municipal: Optional[str] = None
    endereco_complemento: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

    @validator("tipo_documento")
    def tipo_documento_must_be_CPF_or_CNPJ(cls, value):
        if value.upper() not in ["CPF", "CNPJ"]:
            raise ValueError("O tipo de documento do tomador deve ser CPF ou CNPJ.")

        return value.upper()

    @validator("numero_documento")
    def validate_digits_from_numero_documento(cls, value, values):
        validators = {"CPF": _validate_cpf, "CNPJ": _validate_cnpj}

        if "tipo_documento" not in values:
            return value

        document_validator = validators.get(values["tipo_documento"].upper(), None)
        return document_validator(value)


class Servico(BaseModel):
    aliquota: Decimal
    codigo_municipio: str
    discriminacao: str
    iss_retido: int
    item_lista: str
    valor_servico: Decimal

    desconto_condicionado: Decimal = 0
    desconto_incondicionado: Decimal = 0
    outras_retencoes: Decimal = 0
    valor_cofins: Decimal = 0
    valor_csll: Decimal = 0
    valor_deducoes: Decimal = 0
    valor_inss: Decimal = 0
    valor_ir: Decimal = 0
    valor_pis: Decimal = 0

    codigo_cnae: Optional[int] = None
    codigo_tributacao_municipio: Optional[str] = None

    @validator("iss_retido")
    def iss_retido_must_be_1_or_2(cls, value):
        if value not in [1, 2]:
            raise ValueError("ISS Retido deve ser 1 para SIM ou 2 para NÃO.")

        return value

    @property
    def base_calculo(self):
        return self.valor_servico - self.valor_deducoes - self.desconto_incondicionado

    @property
    def valor_iss(self):
        return Decimal(self.base_calculo * self.aliquota).quantize(Decimal("0.01"))

    @property
    def valor_iss_retido(self):
        return self.valor_iss if self.iss_retido == 1 else 0

    @property
    def valor_liquido(self):
        total_discount = sum(
            [
                self.desconto_condicionado,
                self.desconto_incondicionado,
                self.outras_retencoes,
                self.valor_cofins,
                self.valor_csll,
                self.valor_inss,
                self.valor_ir,
                self.valor_iss_retido,
                self.valor_pis,
            ]
        )

        return Decimal(self.valor_servico - total_discount)


def _validate_cpf(document_number: str) -> str:
    if len(document_number) != 11 or not document_number.isdigit():
        raise ValueError("CPF deve conter 11 caracteres, sendo todos números.")

    return document_number


def _validate_cnpj(document_number: str) -> str:
    if len(document_number) != 14 or not document_number.isdigit():
        raise ValueError("CNPJ deve conter 14 caracteres, sendo todos números.")

    return document_number


class RPS(BaseModel):
    data_emissao: datetime
    identificador: str
    incentivo: int
    natureza_operacao: int
    numero: int
    prestador: Prestador
    regime_especial: int = 1
    serie: str
    servico: Servico
    simples: int
    tipo: str
    tomador: Tomador

    @validator("natureza_operacao")
    def natureza_operacao_must_be_between_1_and_6(cls, value):
        if value not in range(1, 7):
            raise ValueError("Natureza da Operação deve ser um número entre 1 e 6.")

        return value

    @validator("regime_especial")
    def regime_especial_must_be_between_1_and_4(cls, value):
        if value not in range(1, 5):
            raise ValueError("Regime Especial deve ser um número entre 1 e 4.")

        return value
