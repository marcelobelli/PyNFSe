import click

from datetime import datetime
from decimal import Decimal

from PyNFSe.cli import constants, helpers
from PyNFSe.utils.entidades import Prestador, Configuracao, Servico, Tomador, RPS, LoteRPS, Ambiente


def prestador():
    click.echo('### Cadastro do Prestador ###')
    prestador = Prestador()
    prestador.cnpj = click.prompt('Informe o CNPJ', type=str)
    prestador.inscricao_municipal = click.prompt('Informe a Inscrição Municipal', type=str)

    return prestador


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


def ambiente(ambiente):
    click.echo('### Configuração ambiente {}'.format(ambiente))
    amb = Ambiente()

    amb.numero_rps = click.prompt('Número inicial do rps', type=int, default=1)
    amb.numero_lote = click.prompt('Número inicial do lote rps', type=int, default=1)
    amb.certificado = click.prompt('Caminho para o certificado', type=str)
    amb.senha = click.prompt('Senha certificado', type=str)

    return amb


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


def lote_rps(prestador, tomador, servico, ambiente):
    conf = helpers.retornar_configuracao()
    amb = ambiente
    rps = RPS()
    lote = LoteRPS()

    rps.identificador = 'N{}'.format(amb.numero_rps)
    rps.data_emissao = datetime.today()
    rps.servico = servico.__dict__
    rps.prestador = prestador.__dict__
    rps.tomador = tomador.__dict__
    rps.simples = conf.simples
    rps.incentivo = conf.incentivo
    rps.numero = amb.numero_rps
    rps.serie = 'A1'
    rps.tipo = '1'
    rps.natureza_operacao = conf.natureza_operacao
    rps.regime_especial = conf.regime_especial

    lote.identificador = 'L{}'.format(amb.numero_lote)
    lote.numero_lote = amb.numero_lote
    lote.cnpj = prestador.cnpj
    lote.inscricao_municipal = prestador.inscricao_municipal
    lote.lista_rps = [(rps.__dict__)]

    return lote
