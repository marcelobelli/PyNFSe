import unittest

from decimal import Decimal
from datetime import datetime
from pyxb import BIND

from PyNFSe.nfse.pr.curitiba import _schema as nfse_schema
from PyNFSe.utils.entidades import Prestador, Tomador, Servico, RPS


class BaseTestesSerializacao(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.prestador = Prestador(**{
            'cnpj':'12345678000123',
            'inscricao_municipal':'0987654321'
        })

        self.tomador = Tomador(**{
            'razao_social':'Nome Cliente',
            'numero_documento':'12345678000123',
            'endereco':'Rua Cliente',
            'endereco_numero':'1234',
            'bairro':'Bairro Cliente',
            'codigo_municipio':'4106902',
            'uf':'PR',
            'cep':'80000000',
            'telefone':'4132221122',
            'email':'financeiro@cliente.com.br'
        })

        self.servico = Servico(**{
            'valor_servico':Decimal('1000.00'),
            'iss_retido':2,  # 1 - Sim, 2 - Não
            'item_lista':'1401',
            'discriminacao':'Descrição do Serviço Prestado',
            'codigo_municipio':'4106902',
            'codigo_cnae':9511800,
            'codigo_tributacao_municipio':'1401',
            'aliquota':Decimal('0.02')
        })

        self.rps = RPS(**{
            'identificador':'N1',
            'data_emissao':datetime(2016, 12, 12, 17, 22, 39, 960610),
            'servico':self.servico,
            'prestador':self.prestador,
            'tomador':self.tomador,
            'simples':1,
            'incentivo':2,
            'numero':1,
            'serie':'A1',
            'tipo':'1',
            'natureza_operacao':1,
            'regime_especial':6
        })

        self.lote_rps = {
            'identificador':'L1',
            'numero_lote':1,
            'cnpj':self.prestador.cnpj,
            'inscricao_municipal':self.prestador.inscricao_municipal,
            'quantidade_rps':1,
            'lista_rps':[self.rps, ]
        }

        self.pedido_cancelamento_nfse = {
            'identificador':'C1',
            'prestador':self.prestador,
            'numero_nota':192,
            'codigo_municipio':'4106902',
            'codigo_cancelamento':'1'
        }

        # Necessário para "serializar" os objetos antes do lote completo.
        self.tc_inf_rps = nfse_schema.tcInfRps()
        self.tc_lote_rps = nfse_schema.tcLoteRps()
        self.tc_lote_rps.ListaRps = BIND()


def xml_expected(arquivo_xml):
    with open('tests/pr/curitiba/xml_expected/{}'.format(arquivo_xml), 'r') as xml:
        xml_expected = xml.read()

    return xml_expected
