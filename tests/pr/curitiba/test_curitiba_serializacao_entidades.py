import unittest

import PyNFSe.nfse.pr.curitiba.serializacao as s
from tests.pr.curitiba.basetestesserializacao import (BaseTestesSerializacao,
                                                      xml_expected)


class SerializacaoEntidadesTestCase(BaseTestesSerializacao):

    def test_xml_prestador(self):
        xml_prestador = s._serial_prestador(self.prestador)
        self.tc_inf_rps.Prestador = xml_prestador
        xml_prestador = xml_prestador.toxml()

        xml_prestador_expected = xml_expected('prestador.xml')

        self.assertEqual(xml_prestador, xml_prestador_expected)

    def test_xml_tomador(self):
        xml_tomador = s._serial_tomador(self.tomador)
        self.tc_inf_rps.Tomador = xml_tomador
        xml_tomador = xml_tomador.toxml()

        xml_tomador_expected = xml_expected('tomador.xml')

        self.assertEqual(xml_tomador, xml_tomador_expected)

    def test_xml_servico(self):
        xml_servico = s._serial_servico(self.servico)
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

if __name__ == '__main__':
    unittest.main()
