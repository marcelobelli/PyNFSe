from datetime import datetime

from PyNFSe.utils.entidades import LoteRPS, RPS


def lote_rps(prestador, tomador, servico, ambiente, configuracao):
    rps = RPS()
    lote = LoteRPS()

    rps.identificador = 'N{}'.format(ambiente.numero_rps)
    rps.data_emissao = datetime.today()
    rps.servico = servico.__dict__
    rps.prestador = prestador.__dict__
    rps.tomador = tomador.__dict__
    rps.simples = configuracao.simples
    rps.incentivo = configuracao.incentivo
    rps.numero = ambiente.numero_rps
    rps.serie = 'A1'
    rps.tipo = '1'
    rps.natureza_operacao = configuracao.natureza_operacao
    rps.regime_especial = configuracao.regime_especial

    lote.identificador = 'L{}'.format(ambiente.numero_lote)
    lote.numero_lote = ambiente.numero_lote
    lote.cnpj = prestador.cnpj
    lote.inscricao_municipal = prestador.inscricao_municipal
    lote.lista_rps = [rps.__dict__]

    return lote
