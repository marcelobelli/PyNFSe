class Prestador(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    cnpj = str()
    inscricao_municipal = str()