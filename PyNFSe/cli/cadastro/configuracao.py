import json

import click

from PyNFSe.cli import constants
from PyNFSe.utils.entidades import Configuracao


def configuracao():
    conf = Configuracao()

    conf.simples = int(click.prompt('Simples Nacional (1 - Sim / 2 - Não)', type=click.Choice(['1', '2'])))
    conf.incentivo = int(
        click.prompt('Incentivador Cultural (1 - Sim / 2 - Não)', type=click.Choice(['1', '2'])))

    conf.iss_retido = int(click.prompt('ISS Retido padrão (1 - Sim / 2 - Não)', type=click.Choice(['1', '2'])))
    conf.regime_especial = int(click.prompt('Regime Especial (0 para ver as opções)',
                                            type=click.Choice(['0', '1', '2', '3', '4'])))
    while conf.regime_especial == 0:
        click.echo(
            '1 - ME Municipal\n'
            '2 - Estimativa\n'
            '3 - Sociedade de profissionais\n'
            '4 - Cooperativa\n'
        )
        conf.regime_especial = int(click.prompt('Regime Especial (0 para ver as opções)',
                                                type=click.Choice(['0', '1', '2', '3', '4'])))

    conf.natureza_operacao = int(click.prompt('Natureza da Operação (0 para ver as opções)',
                                              type=click.Choice(['0', '1', '2', '3', '4', '5', '6'])))
    while conf.natureza_operacao == 0:
        click.echo(
            '1 - Tributação no município\n'
            '2 - Tributação fora do município\n'
            '3 - Isenção\n'
            '4 - Imune\n'
            '5 –Exigibilidade suspensa por decisão judicial\n'
            '6 - Exigibilidade suspensa por procedimento administrativo\n'
        )
        conf.natureza_operacao = int(click.prompt('Natureza da Operação (0 para ver as opções)',
                                                  type=click.Choice(['0', '1', '2', '3', '4', '5', '6'])))

    conf.codigo_municipio = click.prompt('Código do município padrão', type=str)
    conf.item_lista = click.prompt('Código de item da lista de serviço padrão', type=str)
    conf.codigo_tributacao_municipio = click.prompt('Código de Tributação padrão', type=str,
                                                    default=conf.item_lista)
    conf.codigo_cnae = click.prompt('Código CNAE padrão', type=int)
    conf.aliquota = click.prompt('Aliquota padrão')

    return conf


def retornar_configuracao():
    with open(constants.JSON_CONFIGURACAO) as file:
        return Configuracao(**json.load(file))
