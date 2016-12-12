import unittest

from decimal import Decimal

from PyNFSe.entidades.servico import Servico
from PyNFSe.entidades.tomador import Tomador
from PyNFSe.entidades.prestador import Prestador
from PyNFSe.nfse.Curitiba import schema as nfse_schema
from PyNFSe.nfse.Curitiba.serializacao import _serial_tomador, _serial_prestador, _serial_servico, consulta_nfse

class SerializacaoTestCase(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.prestador = Prestador(cnpj='12345678000123',
                                   inscricao_municipal='0987654321')

        self.tomador = Tomador(razao_social='Nome Cliente',
                               numero_documento='12345678000123',
                               endereco='Rua Cliente',
                               endereco_numero='1234',
                               bairro='Bairro Cliente',
                               codigo_municipio='4106902',
                               uf='PR',
                               cep='80000000',
                               telefone='4132221122',
                               email='financeiro@cliente.com.br')

        self.servico = Servico(valor_servico=Decimal('100.00'),
                               iss_retido=2,
                               item_lista='1401',
                               discriminacao='Descrição do Serviço Prestado',
                               codigo_municipio='4106902',
                               codigo_cnae=9511800,
                               codigo_tributacao_municipio='1401',
                               # Opcional
                               valor_deducoes=Decimal('10.00'),
                               valor_pis=Decimal('10.00'),
                               valor_cofins=Decimal('10.00'),
                               valor_inss=Decimal('10.00'),
                               valor_ir=Decimal('10.00'),
                               valor_csll=Decimal('10.00'),
                               valor_iss=Decimal('10.00'),
                               valor_iss_retido=Decimal('10.00'),
                               valor_liquido=Decimal('10.00'),
                               outras_retencoes=Decimal('10.00'),
                               base_calculo=Decimal('10.00'),
                               aliquota=Decimal('0.02'),
                               desconto_incondicionado=Decimal('10.00'),
                               desconto_condicionado=Decimal('10.00'))

        # Necessário para "serializar" os objetos antes do lote completo.
        self.inf_rps = nfse_schema.tcInfRps()

    def test_xml_prestador(self):
        xml_prestador = _serial_prestador(self.prestador)
        self.inf_rps.Prestador = xml_prestador
        xml_prestador = xml_prestador.toxml()

        xml_prestador_expected = xml_expected('prestador.xml')

        self.assertEqual(xml_prestador, xml_prestador_expected)

    def test_xml_tomador(self):
        xml_tomador = _serial_tomador(self.tomador)
        self.inf_rps.Tomador = xml_tomador
        xml_tomador = xml_tomador.toxml()

        xml_tomador_expected = xml_expected('tomador.xml')

        self.assertEqual(xml_tomador, xml_tomador_expected)

    def test_xml_servico(self):
        xml_servico = _serial_servico(self.servico)
        self.inf_rps.Servico = xml_servico
        xml_servico = xml_servico.toxml()

        xml_servico_expected = xml_expected('servico.xml')

        self.assertEqual(xml_servico, xml_servico_expected)

    def test_consultar_nfse_por_nota(self):
        numero_nota = 179
        xml_consultar_nfse = consulta_nfse(self.prestador, numero_nota)

        xml_consultar_nfse_expected = xml_expected('ConsultarNfseEnvio-por_nota.xml')

        self.assertEqual(xml_consultar_nfse, xml_consultar_nfse_expected)


def xml_expected(arquivo_xml):
    with open('PyNFSe/tests/Curitiba/xml_expected/{}'.format(arquivo_xml), 'r') as xml:
        xml_expected = xml.read()

    return xml_expected

if __name__ == '__main__':
    unittest.main()
