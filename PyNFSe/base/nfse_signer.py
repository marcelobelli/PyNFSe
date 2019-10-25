from lxml import etree
from signxml import XMLSigner, methods


class NFSeSigner:
    def __init__(self, certificate: bytes, key: bytes, namespace: str):
        self.cert = certificate
        self.key = key
        self.namespace = namespace

    def sign_rps_batch(self, rps_batch_xml: str) -> str:
        root = etree.fromstring(rps_batch_xml.encode())
        rps_list = root.findall("./{0}LoteRps/{0}ListaRps/*".format(self.namespace))

        for rps in rps_list:
            infrps = rps.find("{0}InfRps".format(self.namespace))
            reference_uri = infrps.attrib.get("id")
            signature = self.sign(rps, reference_uri)

            rps.append(signature)

        rps_batch = root.find("{0}LoteRps".format(self.namespace))
        reference_uri = rps_batch.attrib.get("id")
        signature = self.sign(root, reference_uri)
        root.append(signature)

        rps_batch_xml_signed = etree.tostring(root, encoding="utf-8").decode()
        rps_batch_xml_signed = rps_batch_xml_signed.replace("ds:", "").replace(":ds", "")

        return rps_batch_xml_signed

    def sign_cancellation_request(self, xml_cancellation_request: str) -> str:
        xml_root = etree.fromstring(xml_cancellation_request.encode())
        cancellation_request = xml_root.find("{0}Pedido".format(self.namespace))
        cancellation_request_info = cancellation_request.find(
            "{0}InfPedidoCancelamento".format(self.namespace)
        )
        reference_uri = cancellation_request_info.attrib.get("id")

        signature = self.sign(cancellation_request, reference_uri)
        cancellation_request.append(signature)

        cancellation_request_signed = etree.tostring(xml_root, encoding="utf-8").decode()
        cancellation_request_signed = cancellation_request_signed.replace("ds:", "").replace(":ds", "")

        return cancellation_request_signed

    def sign(self, data, reference_uri):
        signer = XMLSigner(
            method=methods.detached,
            signature_algorithm="rsa-sha1",
            digest_algorithm="sha1",
            c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        )

        return signer.sign(data=data, key=self.key, cert=self.cert, reference_uri="#{}".format(reference_uri))
