from .base import Entidade


class LoteRPS(Entidade):
    identificador = str()
    numero_lote = int()
    lote_cnpj = str()
    lote_inscricao_municipal = str()
    quantidade_rps = int()
    lista_rps = None