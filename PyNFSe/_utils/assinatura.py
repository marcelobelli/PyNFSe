from lxml import etree
from OpenSSL import crypto
from signxml import XMLSigner, methods


class Assinatura:

    def __init__(self, certificado_pfx, senha, namespace):

        self.certificado_pfx = certificado_pfx
        self.senha = senha.encode()
        self.NAMESPACE = namespace

        self._assinador = XMLSigner(
            method=methods.detached,
            signature_algorithm="rsa-sha1",
            digest_algorithm='sha1',
            c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
        )

    def assinar_lote_rps(self, xml_lote_rps):

        root = etree.fromstring(xml_lote_rps.encode())
        lista_rps = root.findall('./{0}LoteRps/{0}ListaRps/*'.format(self.NAMESPACE))

        for rps in lista_rps:
            infrps = rps.find('{0}InfRps'.format(self.NAMESPACE))
            reference_uri = infrps.attrib.get('id')
            assinatura = self._assinatura_xml(rps, reference_uri)

            rps.append(assinatura)

        lote_rps = root.find('{0}LoteRps'.format(self.NAMESPACE))
        reference_uri = lote_rps.attrib.get('id')
        assinatura = self._assinatura_xml(root, reference_uri)

        root.append(assinatura)

        xml_lote_rps_assinado = etree.tostring(root, encoding='utf-8').decode()

        xml_lote_rps_assinado = xml_lote_rps_assinado.replace('ds:', '').replace(':ds', '')

        return xml_lote_rps_assinado

    def assinar_cancelamento_nfse(self, xml_cancelamento_nfse):

        root = etree.fromstring(xml_cancelamento_nfse.encode())
        pedido = root.find('{0}Pedido'.format(self.NAMESPACE))
        inf_pedido = pedido.find('{0}InfPedidoCancelamento'.format(self.NAMESPACE))
        reference_uri = inf_pedido.attrib.get('id')

        assinatura = self._assinatura_xml(pedido, reference_uri)

        pedido.append(assinatura)

        xml_pedido_cancelamento_assinado = etree.tostring(root, encoding='utf-8').decode()

        xml_pedido_cancelamento_assinado = xml_pedido_cancelamento_assinado.replace('ds:', '').replace(':ds', '')

        return xml_pedido_cancelamento_assinado

    def _assinatura_xml(self, data, reference_uri):

        pkcs12 = crypto.load_pkcs12(open(self.certificado_pfx, 'rb').read(), self.senha)
        cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())
        key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

        assinatura = self._assinador.sign(
            data=data,
            key=key,
            cert=cert,
            reference_uri='#{}'.format(reference_uri)
        )

        return assinatura
