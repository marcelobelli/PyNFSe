from .base import  Entidade


class RPS(Entidade):
    identificador = str()
    data_emissao = None
    servico = None
    prestador = None
    tomador = None
    simples = int()
    incentivo = int()
    numero = int()
    serie = str()
    tipo = str()
    natureza_operacao = int()
    regime_especial = int()