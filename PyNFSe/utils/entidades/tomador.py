from .base import Entidade


class Tomador(Entidade):

    razao_social = str()

    tipo_documento = 'CNPJ'
    numero_documento = str()
    inscricao_municipal = None

    endereco = str()
    endereco_numero = str()
    endereco_complemento = None
    bairro = str()
    codigo_municipio = None
    uf = str()
    cep = str()

    telefone = None
    email = None
