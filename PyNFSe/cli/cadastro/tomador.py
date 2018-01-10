import json

import click

from PyNFSe.cli import constants
from PyNFSe.utils.models import Tomador


def tomador():
    tomador = Tomador()
    tomador.tipo_documento = click.prompt('Tipo Documento', type=click.Choice(['cpf', 'cnpj']), default='cnpj').upper()
    tomador.numero_documento = click.prompt('Número Documento')
    tomador.razao_social = click.prompt('Razão Social')

    if tomador.tipo_documento == 'CNPJ':
        tomador.inscricao_municipal = click.prompt('Inscrição Municipal (0 para em branco)')
        if tomador.inscricao_municipal == '0':
            tomador.inscricao_municipal = None

    tomador.endereco = click.prompt('Endereço (Apenas a rua)')
    tomador.endereco_numero = click.prompt('Número endereço')

    tomador.endereco_complemento = click.prompt('Complemento endereço (0 para em branco)')
    if tomador.endereco_complemento == '0':
        tomador.endereco_complemento = None

    tomador.bairro = click.prompt('Bairro')
    tomador.codigo_municipio = click.prompt('Código Município', default=constants.CODIGO_MUNICIPIO)
    tomador.uf = click.prompt('UF')
    tomador.cep = click.prompt('CEP')

    tomador.telefone = click.prompt('Telefone (0 para em branco)')
    if tomador.telefone == '0':
        tomador.telefone = None

    tomador.email = click.prompt('Email (0 para em branco)')
    if tomador.email == '0':
        tomador.email = None

    return tomador


def retornar_tomador():
    numero_doc = click.prompt('Numero documento')
    with open(constants.JSON_TOMADORES, mode='r') as file:
        clientes = json.load(file)
    try:
        return Tomador(**clientes[numero_doc])
    except KeyError:
        click.echo('{} não cadastrado'.format(numero_doc))
