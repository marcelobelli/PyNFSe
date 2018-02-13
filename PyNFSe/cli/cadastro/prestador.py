import json

import click

from PyNFSe.cli import constants
from PyNFSe.utils.models import Prestador


def prestador():
    click.echo('### Cadastro do Prestador ###')
    prestador = Prestador()
    prestador.cnpj = click.prompt('Informe o CNPJ', type=str)
    prestador.inscricao_municipal = click.prompt('Informe a Inscrição Municipal', type=str)

    return prestador


def retornar_prestador():
    with open(constants.JSON_PRESTADOR) as file:
        return Prestador(**json.load(file))
