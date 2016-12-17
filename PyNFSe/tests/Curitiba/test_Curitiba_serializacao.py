import unittest

from decimal import Decimal

from PyNFSe.entidades.lote_rps import LoteRPS
from PyNFSe.entidades.servico import Servico
from PyNFSe.entidades.tomador import Tomador
from PyNFSe.entidades.prestador import Prestador
from PyNFSe.entidades.rps import RPS
from PyNFSe.nfse.Curitiba import schema as nfse_schema
from PyNFSe.nfse.Curitiba.serializacao import _serial_tomador, _serial_prestador, _serial_servico, _serial_rps, consulta_nfse
import PyNFSe.nfse.Curitiba.serializacao as s
from datetime import datetime
from pyxb import BIND

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

        self.servico = Servico(
            valor_servico=Decimal('1000.00'),
            iss_retido=2,  # 1 - Sim, 2 - Não
            item_lista='1401',
            discriminacao='Descrição do Serviço Prestado',
            codigo_municipio='4106902',
            codigo_cnae=9511800,
            codigo_tributacao_municipio='1401',
            aliquota=Decimal('0.02')
        )

        self.rps = RPS(identificador='N1',
                       data_emissao=datetime(2016, 12, 12, 17, 22, 39, 960610),
                       servico=self.servico,
                       prestador=self.prestador,
                       tomador=self.tomador,
                       simples=1,
                       incentivo=2,
                       numero=1,
                       serie='A1',
                       tipo='1',
                       natureza_operacao=1,
                       regime_especial=6)

        self.lote_rps = LoteRPS(identificador='L1',
                                numero_lote=1,
                                cnpj=self.rps.prestador.cnpj,
                                inscricao_municipal=self.rps.prestador.inscricao_municipal,
                                quantidade_rps=1,
                                lista_rps=[self.rps, ])

        # Necessário para "serializar" os objetos antes do lote completo.
        self.tc_inf_rps = nfse_schema.tcInfRps()
        self.tc_lote_rps = nfse_schema.tcLoteRps()
        self.tc_lote_rps.ListaRps = BIND()

    def test_xml_prestador(self):
        xml_prestador = _serial_prestador(self.prestador)
        self.tc_inf_rps.Prestador = xml_prestador
        xml_prestador = xml_prestador.toxml()

        xml_prestador_expected = xml_expected('prestador.xml')

        self.assertEqual(xml_prestador, xml_prestador_expected)

    def test_xml_tomador(self):
        xml_tomador = _serial_tomador(self.tomador)
        self.tc_inf_rps.Tomador = xml_tomador
        xml_tomador = xml_tomador.toxml()

        xml_tomador_expected = xml_expected('tomador.xml')

        self.assertEqual(xml_tomador, xml_tomador_expected)

    def test_xml_servico(self):
        xml_servico = _serial_servico(self.servico)
        self.tc_inf_rps.Servico = xml_servico
        xml_servico = xml_servico.toxml()

        xml_servico_expected = xml_expected('servico.xml')

        self.assertEqual(xml_servico, xml_servico_expected)

    def test_xml_rps(self):
        xml_rps = s._serial_rps(self.rps)
        self.tc_lote_rps.ListaRps.append(xml_rps)
        xml_rps = xml_rps.toxml()


        xml_rps_expected = xml_expected('rps.xml')

        self.assertEqual(xml_rps, xml_rps_expected)

    def test_consultar_nfse_por_nota(self):
        numero_nota = 179
        xml_consultar_nfse = consulta_nfse(self.prestador, numero_nota)

        xml_consultar_nfse_expected = xml_expected('ConsultarNfseEnvio-por_nota.xml')

        self.assertEqual(xml_consultar_nfse, xml_consultar_nfse_expected)

    def test_envio_lote_rps(self):
        xml_lote_rps = s.envio_lote_rps(self.lote_rps)

        xml_lote_rps_expected = xml_expected('EnviarLoteRpsEnvio.xml')

        self.assertEqual(xml_lote_rps, xml_lote_rps_expected)


def xml_expected(arquivo_xml):
    with open('PyNFSe/tests/Curitiba/xml_expected/{}'.format(arquivo_xml), 'r') as xml:
        xml_expected = xml.read()

    return xml_expected

if __name__ == '__main__':
    unittest.main()
