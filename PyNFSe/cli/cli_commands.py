import json
import os
import click

from PyNFSe.cli.file_manipulation import criar_diretorio, criar_arquivo_json
from PyNFSe.utils.entidades.configuracao import Configuracao
from PyNFSe.utils.entidades.prestador import Prestador

HOME_FOLDER = os.path.expanduser('~')
DIR_PYNFSE = os.path.join(HOME_FOLDER, '.pynfse')
JSON_PRESTADOR = os.path.join(DIR_PYNFSE, 'prestador.json')
JSON_CONFIG_PRODUCAO = os.path.join(DIR_PYNFSE, 'config-producao.json')
JSON_CONFIG_TESTE = os.path.join(DIR_PYNFSE, 'config-teste.json')
JSON_CLIENTES = os.path.join(DIR_PYNFSE, 'clientes.json')


def setup():
    criar_diretorio(DIR_PYNFSE)

    if criar_arquivo_json(JSON_PRESTADOR):
        with open(JSON_PRESTADOR, mode='w') as file:
            prestador = cadastrar_prestador()
            # click.echo(prestador.__dict__)
            json.dump(prestador.__dict__, file, ensure_ascii=False)

    if criar_arquivo_json(JSON_CONFIG_PRODUCAO):
        with open(JSON_CONFIG_PRODUCAO, mode='w') as file:
            configuracao = cadastrar_configuracao('Produção')
            json.dump(configuracao.__dict__, file, ensure_ascii=False)

    ambiente_teste = click.prompt('Deseja cadastar ambiente homologação (s/n)', type=click.Choice(['s', 'n']), default='s')
    if ambiente_teste == 's':
        if criar_arquivo_json(JSON_CONFIG_TESTE):
            with open(JSON_CONFIG_TESTE, mode='w') as file:
                configuracao = cadastrar_configuracao('Homologação')
                json.dump(configuracao.__dict__, file, ensure_ascii=False)



    criar_arquivo_json(JSON_CLIENTES)


def cadastrar_prestador():
    prestador = Prestador()

    click.echo('### Cadastro do Prestador ###')
    prestador.cnpj = click.prompt('Informe o CNPJ', type=str)
    prestador.inscricao_municipal = click.prompt('Informe a Inscrição Municipal', type=str)

    return prestador


def cadastrar_configuracao(ambiente):
    configuracao = Configuracao()

    click.echo('### Configuração ambiente {}'.format(ambiente))

    configuracao.simples = int(click.prompt('Simples Nacional (1 - Sim / 2 - Não)', type=click.Choice(['1', '2'])))
    configuracao.incentivo = int(click.prompt('Incentivador Cultural (1 - Sim / 2 - Não)', type=click.Choice(['1', '2'])))

    configuracao.regime_especial = int(click.prompt('Regime Especial (0 para ver as opções)',
                                            type=click.Choice(['0', '1', '2', '3', '4'])))
    while configuracao.regime_especial == 0:
        click.echo(
            '1 - ME Municipal\n'
            '2 - Estimativa\n'
            '3 - Sociedade de profissionais\n'
            '4 - Cooperativa\n'
        )
        configuracao.regime_especial = int(click.prompt('Regime Especial (0 para ver as opções)',
                                                type=click.Choice(['0', '1', '2', '3', '4'])))

    configuracao.numero_rps = click.prompt('Número inicial do rps', type=int, default=1)
    configuracao.numero_lote = click.prompt('Número inicial do lote rps', type=int, default=1)

    configuracao.natureza_operacao = int(click.prompt('Natureza da Operação (0 para ver as opções)',
                                              type=click.Choice(['0', '1', '2', '3', '4', '5', '6'])))
    while configuracao.natureza_operacao == 0:
        click.echo(
            '1 - Tributação no município\n'
            '2 - Tributação fora do município\n'
            '3 - Isenção\n'
            '4 - Imune\n'
            '5 –Exigibilidade suspensa por decisão judicial\n'
            '6 - Exigibilidade suspensa por procedimento administrativo\n'
        )
        configuracao.natureza_operacao = int(click.prompt('Natureza da Operação (0 para ver as opções)',
                                                  type=click.Choice(['0', '1', '2', '3', '4', '5', '6'])))

    configuracao.codigo_municipio = click.prompt('Código do município padrão', type=str)
    configuracao.certificado = click.prompt('Caminho para o certificado', type=str)
    configuracao.senha = click.prompt('Senha certificado', type=str)

    return configuracao


def salvar_cliente(json_cliente, numero_documento):

    if not os.path.exists(DIR_PYNFSE):
        print('pynfse não configurado. Execute "python pynfse.py configurar_cli" e siga os passos.')
        return

    with open(JSON_CLIENTES, mode='r') as file:
        json_file = json.load(file)

    with open(JSON_CLIENTES, mode='w') as file:
        json_file[numero_documento] = json_cliente
        json.dump(json_file, file, ensure_ascii=False)


def listar_clientes():
    with open('teste.json', mode='r') as file:
        json_file = json.load(file)

    for client in json_file:
        json_client = json.loads(json_file[client])
        razao_social = json_client['razao_social']
        numero_documento = json_client['numero_documento']
        texto = f'{razao_social} - {numero_documento}'
        print('{0} - {1}'.format(json_client['razao_social'], json_client['numero_documento']))