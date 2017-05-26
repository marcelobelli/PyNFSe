import click
import json

from prompt_toolkit import prompt

from PyNFSe.cli.cli_validator import EmptyValidator, CPFouCNPJChoiceValidator, CPFouCNPJValueValidator, NumberValidator
from PyNFSe.cli.file_manipulation import append_json

@click.group()
def cli():
    pass

@cli.command()
def cadastrar_cliente():

    cliente = {}

    razao_social = prompt('Nome: ', validator=EmptyValidator())
    cliente['razao_social'] = razao_social

    tipo_documento = prompt('CPF ou CNPJ: ', validator=CPFouCNPJChoiceValidator())
    tipo_documento = tipo_documento.upper()
    cliente['tipo_documento'] = tipo_documento

    numero_documento = prompt('Número do {}: '.format(tipo_documento), validator=CPFouCNPJValueValidator(tipo_documento))
    cliente['numero_documento'] = numero_documento

    if tipo_documento == 'CNPJ':
        inscricao_municipal = prompt('Inscrição Municipal: ', validator=EmptyValidator())
        cliente['inscricao_municipal'] = inscricao_municipal

    endereco = prompt('Endereço (Apenas a rua): ', validator=EmptyValidator())
    cliente['endereco'] = endereco

    endereco_numero = prompt('Número endereço: ', validator=EmptyValidator())
    cliente['endereco_numero'] = endereco_numero

    endereco_complemento = prompt('Complemento endereço: ', validator=EmptyValidator())
    cliente['endereco_complemento'] = endereco_complemento

    bairro = prompt('Bairro: ', validator=EmptyValidator())
    cliente['bairro'] = bairro

    codigo_municipio = prompt('Código Município: ' , validator=EmptyValidator())
    cliente['codigo_municipio'] = codigo_municipio

    uf = prompt('UF: ', validator=EmptyValidator())
    cliente['uf'] = uf

    cep = prompt('CEP: ', validator=NumberValidator())
    cliente['cep'] = cep

    telefone = prompt('Telefone: ', validator=NumberValidator())
    cliente['telefone'] = telefone

    email = prompt('Email: ', validator=EmptyValidator())
    cliente['email'] = email

    json2 = json.dumps(cliente, ensure_ascii=False)

    append_json('teste.json', json2)

    click.echo('OK')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(cadastrar_cliente)
cli.add_command(dropdb)