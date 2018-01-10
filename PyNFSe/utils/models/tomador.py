import typing

from simple_model import Model


class Tomador(Model):
    razao_social: str
    tipo_documento: str = 'CNPJ'
    numero_documento: str
    inscricao_municipal: typing.Any = None

    endereco: str
    endereco_numero: str
    endereco_complemento: typing.Any = None
    bairro: str
    codigo_municipio: typing.Any = None
    uf: str
    cep: str

    telefone: typing.Any = None
    email: typing.Any = None
