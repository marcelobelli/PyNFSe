import json

import click

from PyNFSe.cli import constants
from PyNFSe.utils.entidades import Ambiente


def ambiente(ambiente):
    click.echo('### Configuração ambiente {}'.format(ambiente))
    amb = Ambiente()

    amb.numero_rps = click.prompt('Número inicial do rps', type=int, default=1)
    amb.numero_lote = click.prompt('Número inicial do lote rps', type=int, default=1)
    amb.certificado = click.prompt('Caminho para o certificado', type=str)
    amb.senha = click.prompt('Senha certificado', type=str)

    return amb


def retornar_ambiente(producao):
    if producao:
        ambiente = constants.JSON_AMBIENTE_PRODUCAO
    else:
        ambiente = constants.JSON_AMBIENTE_HOMOLOGACAO
    with open(ambiente) as file:
        return Ambiente(**json.load(file))
