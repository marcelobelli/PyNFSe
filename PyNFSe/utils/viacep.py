import json
import requests


class ViaCEP(object):

    def __init__(self, cep):
        self.cep = cep

    def consulta_cep(self):
        url_viacep = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        requisicao = requests.get(url_viacep)
        retorno = json.loads(requisicao.text)

        return retorno
