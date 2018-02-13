import json
import os

import click

from PyNFSe.cli import cadastro, constants, helpers


@click.group()
def cli():
    pass


@cli.command()
def configurar_cli():
    helpers.criar_diretorio(constants.DIR_PYNFSE)

    if helpers.criar_arquivo_json(constants.JSON_PRESTADOR):
        prestador = cadastro.prestador()
        helpers.salvar_arquivo_json(constants.JSON_PRESTADOR, prestador)

    if helpers.criar_arquivo_json(constants.JSON_CONFIGURACAO):
        configuracao = cadastro.configuracao()
        helpers.salvar_arquivo_json(constants.JSON_CONFIGURACAO, configuracao)

    if helpers.criar_arquivo_json(constants.JSON_AMBIENTE_PRODUCAO):
        ambiente = cadastro.ambiente('Produção')
        helpers.salvar_arquivo_json(constants.JSON_AMBIENTE_PRODUCAO, ambiente)

    ambiente_teste = click.prompt('Deseja cadastar ambiente homologação (s/n)', type=click.Choice(['s', 'n']),
                                  default='s')
    if ambiente_teste == 's':
        if helpers.criar_arquivo_json(constants.JSON_AMBIENTE_HOMOLOGACAO):
            ambiente = cadastro.ambiente('Homologação')
            helpers.salvar_arquivo_json(constants.JSON_AMBIENTE_HOMOLOGACAO, ambiente)

    helpers.criar_arquivo_json(constants.JSON_TOMADORES)


@cli.command()
def cadastrar_tomador():
    if not os.path.exists(constants.DIR_PYNFSE):
        print('pynfse não configurado. Execute "python pynfse.py configurar_cli" e siga os passos.')
        return

    tomador = cadastro.tomador()

    with open(constants.JSON_TOMADORES, mode='r') as file:
        json_file = json.load(file)

    with open(constants.JSON_TOMADORES, mode='w') as file:
        json_file[tomador.numero_documento] = tomador.__dict__
        json.dump(json_file, file, ensure_ascii=False)


@cli.command()
@click.option('--producao', is_flag=True)
def emitir_nfse(producao):

    ambiente = cadastro.retornar_ambiente(producao)
    configuracao = cadastro.retornar_configuracao()
    prestador = cadastro.retornar_prestador()
    tomador = cadastro.retornar_tomador()
    while not tomador:
        tomador = cadastro.retornar_tomador()

    servico = cadastro.servico()

    lote = cadastro.lote_rps(prestador, tomador, servico, ambiente, configuracao)

    retorno = helpers.enviar_lote(lote, ambiente, producao)

    ambiente.numero_lote += 1
    ambiente.numero_rps += 1

    if producao:
        helpers.salvar_arquivo_json(constants.JSON_AMBIENTE_PRODUCAO, ambiente)
    else:
        helpers.salvar_arquivo_json(constants.JSON_AMBIENTE_HOMOLOGACAO, ambiente)

    print(retorno)


@cli.command()
def listar_cliente():
    with open(constants.JSON_TOMADORES, mode='r') as file:
        tomadores = json.load(file)

    for num_doc in tomadores:
        tomador = tomadores[num_doc]
        print('{0} - {1}'.format(tomador['razao_social'], tomador['numero_documento']))
