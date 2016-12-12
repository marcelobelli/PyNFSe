from .base import Entidade


class LoteRPS(Entidade):
    identificador = str()
    numero_lote = int()
    cnpj = str()
    inscricao_municipal = str()
    lista_rps = []