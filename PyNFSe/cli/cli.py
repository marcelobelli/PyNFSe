import click

from PyNFSe.cli.cli_commands import salvar_cliente, listar_clientes, setup
from PyNFSe.utils.entidades.tomador import Tomador


@click.group()
def cli():
    pass


@cli.command()
def configurar_cli():
    setup()
    # click.echo('{}'.format('sim' if yes else 'não'))
    # pass

@cli.command()
@click.option('-td', '--tipo_doc', prompt='Tipo Documento', type=click.Choice(['cpf', 'cnpj']), default='cnpj')
@click.option('-nd', '--numero_doc', prompt='Número Documento')
@click.option('-rz', '--razao_social', prompt='Razão Social')
@click.option('-im', '--inscricao_municipal')
@click.option('-er', '--endereco', prompt='Endereço (Apenas a rua)')
@click.option('-en', '--endereco_numero', prompt='Número endereço')
@click.option('-ec', '--endereco_complemento')
@click.option('-eb', '--bairro', prompt='Bairro')
@click.option('-cm', '--codigo_municipio', prompt='Código Município')
@click.option('-uf', '--uf', prompt='UF')
@click.option('-cep', '--cep', prompt='CEP')
@click.option('-te', '--telefone')
@click.option('-em', '--email')
def cadastrar_tomador(tipo_doc, numero_doc, razao_social, inscricao_municipal,
                      endereco, endereco_numero, endereco_complemento,
                      bairro, codigo_municipio, uf, cep, telefone, email):

    tomador = Tomador()
    tomador.tipo_documento = tipo_doc
    tomador.numero_documento = numero_doc
    tomador.razao_social = razao_social
    tomador.inscricao_municipal = inscricao_municipal
    tomador.endereco = endereco
    tomador.endereco_numero = endereco_numero
    tomador.endereco_complemento = endereco_complemento
    tomador.bairro = bairro
    tomador.codigo_municipio = codigo_municipio
    tomador.uf = uf
    tomador.cep = cep
    tomador.telefone = telefone
    tomador.email = email

    salvar_cliente(tomador.json(), tomador.numero_documento)


@cli.command()
def listar_cliente():
    print('Lista')
    listar_clientes()

