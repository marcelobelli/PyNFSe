from simple_model import Model


class LoteRPS(Model):
    identificador: str
    numero_lote: int
    cnpj: str
    inscricao_municipal: str
    lista_rps: list
