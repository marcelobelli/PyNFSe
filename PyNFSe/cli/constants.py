import json
import os


def _retorna_parametro(parametro):
    try:
        with open(JSON_CONFIGURACAO, mode='r') as file:
            return json.load(file)[parametro]
    except FileNotFoundError:
        return None



HOME_FOLDER = os.path.expanduser('~')
DIR_PYNFSE = os.path.join(HOME_FOLDER, '.pynfse')
JSON_PRESTADOR = os.path.join(DIR_PYNFSE, 'prestador.json')
JSON_CONFIGURACAO = os.path.join(DIR_PYNFSE, 'configuracao.json')
JSON_AMBIENTE_PRODUCAO = os.path.join(DIR_PYNFSE, 'ambiente_producao.json')
JSON_AMBIENTE_HOMOLOGACAO = os.path.join(DIR_PYNFSE, 'ambiente_homologacao.json')
JSON_TOMADORES = os.path.join(DIR_PYNFSE, 'clientes.json')
ISS_RETIDO = _retorna_parametro('iss_retido')
CODIGO_MUNICIPIO = _retorna_parametro('codigo_municipio')
ITEM_LISTA = _retorna_parametro('item_lista')
CODIGO_CNAE = _retorna_parametro('codigo_cnae')
ALIQUOTA = _retorna_parametro('aliquota')
