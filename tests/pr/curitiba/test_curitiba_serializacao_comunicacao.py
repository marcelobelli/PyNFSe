import datetime
import unittest

import PyNFSe.nfse.pr.curitiba.serializacao as s
from tests.pr.curitiba.basetestesserializacao import BaseTestesSerializacao, xml_expected


class SerializacaoComunicacaoTestCase(BaseTestesSerializacao):
    def test_consultar_nfse_por_nota(self):
        numero_nota = 179
        xml_consultar_nfse = s.consulta_nfse_por_numero(self.prestador, numero_nota)

        xml_consultar_nfse_expected = xml_expected("ConsultarNfseEnvio-por_nota.xml")

        self.assertEqual(xml_consultar_nfse, xml_consultar_nfse_expected)

    def test_consultar_nfse_por_data(self):
        data_inicial = datetime.datetime(2016, 12, 12)
        data_final = datetime.datetime(2016, 12, 17)
        xml_consultar_nfse = s.consulta_nfse_por_data(self.prestador, data_inicial, data_final)

        xml_consultar_nfse_expected = xml_expected("ConsultarNfseEnvio-por_data.xml")

        self.assertEqual(xml_consultar_nfse, xml_consultar_nfse_expected)

    def test_envio_lote_rps(self):
        xml_lote_rps = s.envio_lote_rps(self.lote_rps)

        xml_lote_rps_expected = xml_expected("EnviarLoteRpsEnvio.xml")

        self.assertEqual(xml_lote_rps, xml_lote_rps_expected)

    def test_consultar_situacao_lote_rps(self):
        xml_consultar_situacao_lote = s.consulta_situacao_lote_rps(self.prestador, "636174090357960929")

        xml_consultar_situacao_lote_expected = xml_expected("ConsultarSituacaoLoteRpsEnvio.xml")

        self.assertEqual(xml_consultar_situacao_lote, xml_consultar_situacao_lote_expected)

    def test_consultar_nfse_por_rps(self):

        xml_consultar_nfse = s.consulta_nfse_por_rps(self.rps)

        xml_consultar_nfse_expected = xml_expected("ConsultarNfseRpsEnvio.xml")

        self.assertEqual(xml_consultar_nfse, xml_consultar_nfse_expected)

    def test_consultar_lote_rps(self):
        xml_consultar_lote = s.consulta_lote_rps(self.prestador, "636174090357960929")

        xml_consultar_lote_expected = xml_expected("ConsultarLoteRpsEnvio.xml")

        self.assertEqual(xml_consultar_lote, xml_consultar_lote_expected)

    def test_cancelar_nfse(self):
        xml_cancelar_nfse = s.cancela_nfse(self.pedido_cancelamento_nfse)

        xml_cancelar_nfse_expected = xml_expected("CancelarNfseEnvio.xml")

        self.assertEqual(xml_cancelar_nfse, xml_cancelar_nfse_expected)


if __name__ == "__main__":
    unittest.main()
