from decimal import Decimal

import click

from PyNFSe.cli import constants
from PyNFSe.utils.entidades import Servico


def servico():
    servico = Servico()
    servico.valor_servico = Decimal(click.prompt('Valor serviço'))
    servico.iss_retido = int(click.prompt('ISS Retido (1 - Sim / 2 - Não)', type=click.Choice(['1', '2']), default=constants.ISS_RETIDO))
    servico.item_lista = click.prompt('Código de item da lista de serviço', default=constants.ITEM_LISTA)
    servico.discriminacao = click.prompt('Discriminação do serviço prestado')
    servico.codigo_municipio = click.prompt('Código do município', default=constants.CODIGO_MUNICIPIO)
    servico.codigo_cnae = click.prompt('Código CNAE', type=int, default=constants.CODIGO_CNAE)
    servico.codigo_tributacao_municipio = click.prompt('Código de Tributação', default=servico.item_lista)
    servico.aliquota = Decimal(click.prompt('Aliquota', default=constants.ALIQUOTA))

    return servico
