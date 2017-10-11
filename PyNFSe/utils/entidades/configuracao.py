from decimal import Decimal

from .base import Entidade


class Configuracao(Entidade):
    simples = int()
    incentivo = int()
    regime_especial = int()
    natureza_operacao = int()
    codigo_municipio = str()
    iss_retido = int()
    item_lista = str()
    codigo_cnae = int()
    codigo_tributacao_municipio = str()
    aliquota = Decimal()


class Ambiente(Entidade):
    numero_rps = int()
    numero_lote = int()
    certificado = str()
    senha = str()
