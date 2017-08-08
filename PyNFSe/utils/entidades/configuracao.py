from .base import Entidade


class Configuracao(Entidade):
    simples = int()
    incentivo = int()
    regime_especial = int()
    numero_rps = int()
    numero_lote = int()
    natureza_operacao = int()
    codigo_municipio = str()
    certificado = str()
    senha = str()
