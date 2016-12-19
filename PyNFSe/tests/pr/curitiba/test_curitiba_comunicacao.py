import unittest

from datetime import datetime
from decimal import Decimal

from PyNFSe.nfse.pr.curitiba import serializacao as s
from PyNFSe.utils.certificado import certificado as c
from PyNFSe.nfse.pr.curitiba.comunicacao import Comunicacao
from PyNFSe.tests.pr.curitiba.basetestesserializacao import xml_expected


class ComunicacaoTestCase(unittest.TestCase):
    maxDiff = None

    def setUp(self):

        self.prestador = {
            'cnpj': '09400293000179',
            'inscricao_municipal': '140106128722'
        }

        self.tomador = {
            'razao_social': 'Anéis RCS',
            'numero_documento': '81062952000131',
            'endereco': 'Rua João Bettega',
            'endereco_numero': '2052',
            'bairro': 'Portão',
            'codigo_municipio': '4106902',
            'uf': 'PR',
            'cep': '81070001',
            'telefone': '4132458338',
            'email': 'financeiro@aneisrcs.com.br'
        }

        self.servico1 = {
            'valor_servico': Decimal('1000.00'),
            'iss_retido': 2,
            'item_lista': '1401',
            'discriminacao': 'Descrição do Serviço Prestado',
            'codigo_municipio': '4106902',
            'codigo_cnae': 9511800,
            'codigo_tributacao_municipio': '1401',
            'aliquota': Decimal('0.02')
        }

        self.rps = {
            'identificador': 'N1',
            'data_emissao': datetime(2016, 12, 12, 17, 22, 39, 960610),
            'servico': self.servico1,
            'prestador': self.prestador,
            'tomador': self.tomador,
            'simples': 1,
            'incentivo': 2,
            'numero': 12,
            'serie': 'A1',
            'tipo': '1',
            'natureza_operacao': 1,
            'regime_especial': 1
        }

        url_homologacao = 'https://pilotoisscuritiba.curitiba.pr.gov.br/nfse_ws/NfseWs.asmx?WSDL'
        self.cert, self.cert_file, self.key, self.key_file = c('PyNFSe/tests/pr/curitiba/certificado/certificado.pfx', '123456')
        self.servicos_wsdl = Comunicacao(url_homologacao, True, (self.cert_file.name, self.key_file.name))
        self.protocolo = '636175970893192424'

    def test_consultar_nfse_por_numero(self):
        numero_nfse = 190
        xml = s.consulta_nfse_por_numero(self.prestador, numero_nfse)
        xml_retorno = self.servicos_wsdl.recepcionar_xml('ConsultarNfse', xml)

        xml_retorno_expected = xml_expected('comunicacao/ConsultarNfseResposta-por_numero.xml')

        self.assertEqual(xml_retorno, xml_retorno_expected)

    def test_consultar_nfse_por_data(self):
        data_inicial = datetime(2016, 12, 12)
        data_final = datetime(2016, 12, 12)
        xml = s.consulta_nfse_por_data(self.prestador, data_inicial, data_final)
        xml_retorno = self.servicos_wsdl.recepcionar_xml('ConsultarNfse', xml)

        xml_retorno_expected = xml_expected('comunicacao/ConsultarNfseResposta-por_data.xml')

        self.assertEqual(xml_retorno, xml_retorno_expected)

    def test_consultar_nfse_por_rps(self):
        xml = s.consulta_nfse_por_rps(self.rps)
        xml_retorno = self.servicos_wsdl.recepcionar_xml('ConsultarNfsePorRps', xml)

        xml_retorno_expected = xml_expected('comunicacao/ConsultarNfseRpsResposta-por_rps.xml')

        self.assertEqual(xml_retorno, xml_retorno_expected)

    def test_consultar_situacao_lote_rps(self):
        xml = s.consulta_situacao_lote_rps(self.prestador, self.protocolo)
        xml_retorno = self.servicos_wsdl.recepcionar_xml('ConsultarSituacaoLoteRps', xml)

        xml_retorno_expected = xml_expected('comunicacao/ConsultarSituacaoLoteRpsResposta.xml')

        self.assertEqual(xml_retorno, xml_retorno_expected)

    def test_consultar_lote_rps(self):
        xml = s.consulta_lote_rps(self.prestador, self.protocolo)
        xml_retorno = self.servicos_wsdl.recepcionar_xml('ConsultarLoteRps', xml)

        xml_retorno_expected = xml_expected('comunicacao/ConsultarLoteRpsResposta.xml')

        self.assertEqual(xml_retorno, xml_retorno_expected)


if __name__ == '__main__':
    unittest.main()
