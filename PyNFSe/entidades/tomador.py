from .base import Entidade


class Tomador(Entidade):

    razao_social = str()

    tipo_documento = 'CNPJ'
    numero_documento = str()
    inscricao_municipal = str()

    endereco = str()
    endereco_numero = str()
    endereco_complemento = str()
    bairro = str()
    codigo_municipio = str()
    uf = str()
    cep = str()

    telefone = str()
    email = str()