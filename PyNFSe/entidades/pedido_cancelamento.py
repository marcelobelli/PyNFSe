from .base import Entidade


class PedidoCancelamentoNFSe(Entidade):

    identificador = str()
    prestador = None
    numero_nota = int()
    codigo_municipio = str()
    codigo_cancelamento = str()
