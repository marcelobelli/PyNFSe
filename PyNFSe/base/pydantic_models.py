from typing import Optional

from pydantic import validator
from pydantic.dataclasses import dataclass


@dataclass
class Prestador:
    cnpj: str
    inscricao_municipal: str

    @validator("cnpj")
    def cnpj_must_have_14_digits(cls, value):
        return _validate_cnpj(value)


@dataclass
class Tomador:
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


def _validate_cpf(document_number: str) -> str:
    if len(document_number) != 11 or not document_number.isdigit():
        raise ValueError("CPF deve conter 11 caracteres, sendo todos números.")

    return document_number


def _validate_cnpj(document_number: str) -> str:
    if len(document_number) != 14 or not document_number.isdigit():
        raise ValueError("CNPJ deve conter 14 caracteres, sendo todos números.")

    return document_number
