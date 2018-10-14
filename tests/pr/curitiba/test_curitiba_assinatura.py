import unittest

import PyNFSe.nfse.pr.curitiba.serializacao as s
from PyNFSe.base.assinatura import Assinatura
from PyNFSe.base.certificado import certificado as c
from tests.pr.curitiba.basetestesserializacao import BaseTestesSerializacao, xml_expected


class AssinaturaTestCase(BaseTestesSerializacao):

    def setUp(self):
        super(AssinaturaTestCase, self).setUp()
        namespace = '{http://isscuritiba.curitiba.pr.gov.br/iss/nfse.xsd}'
        cert, cert_file, key, key_file = c('tests/pr/curitiba/certificado/certificado.pfx', '123456')
        self.assinador = Assinatura(cert, key, namespace)

    def test_assinatura_lote_rps(self):

        xml_lote_rps = s.envio_lote_rps(self.lote_rps)
        xml_lote_rps = self.assinador.assinar_lote_rps(xml_lote_rps)

        xml_lote_rps_expected = xml_expected('EnviarLoteRpsEnvio-Assinado.xml')

        self.assertEqual(xml_lote_rps, xml_lote_rps_expected)

    def test_assinatura_cancelamento_nfse(self):
        xml_cancelar_nfse = s.cancela_nfse(self.pedido_cancelamento_nfse)
        xml_cancelar_nfse = self.assinador.assinar_cancelamento_nfse(xml_cancelar_nfse)

        xml_cancelar_nfse_expected = xml_expected('CancelarNfseEnvio-Assinado.xml')

        self.assertEqual(xml_cancelar_nfse, xml_cancelar_nfse_expected)


if __name__ == '__main__':
    unittest.main()
