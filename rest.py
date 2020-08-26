'''
REST Server.
To Start:
gunicorn -b 0.0.0.0:8000 "rest:create_app()" &

To Call: 
```
time curl -X POST  localhost:8000/api -H 'Content-Type: application/json' -d '{"tomador": {"razao_social": "Nome Cliente","tipo_documento": "CNPJ","numero_documento": "12345678000123","endereco": "Rua Cliente","endereco_numero": "1234","bairro": "Bairro Cliente","codigo_municipio": "4106902","uf": "PR","cep": "80000000","telefone": "4132221122","email": "financeiro@cliente.com.br"},"servico": {"valor_servico": 1000.00,"iss_retido": 2,"item_lista": "1401","discriminacao": "Descrição do Serviço Prestado","codigo_municipio": "4106902","codigo_cnae": 9511800,"codigo_tributacao_municipio": "1401","aliquota": "0.02"},"rps": {"identificador": "N1","year": 2016,"month": 12,"day": 12,"hour": 17,"minutes": 22,"seconds": 39,"miliseconds": 960610,"numero": 1,"serie": "A1","tipo": "1","natureza_operacao": 1}}' -i
```

To validate if service is alive:
curl localhost:8000/health
'''
import gc
import time
import json
import falcon
import xmltodict
from decimal import Decimal
from datetime import datetime
from pynfse.base.models import RPS, LoteRPS, PedidoCancelamentoNFSe, Prestador, Servico, Tomador
import pynfse.nfse.pr.curitiba.serializacao as s


class Health():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = 'Alive!'


class RestResource():
    def __init__(self):
        # TODO: load this information from config file
        self.prestador = Prestador(
            **{"cnpj": "12345678000123",
               "inscricao_municipal": "0987654321"})

    def on_post(self, req, resp, **kwargs):
        print("ON POST")
        start_time = time.time()
        ret = {}
        try:
            data = req.media
            tomador = Tomador(**data['tomador'])
            servico = Servico(
                **{
                    "valor_servico": Decimal(data['servico']['valor_servico']),
                    "iss_retido": data['servico']['iss_retido'],
                    "item_lista": data['servico']['item_lista'],
                    "discriminacao": data['servico']['discriminacao'],
                    "codigo_municipio": data['servico']['codigo_municipio'],
                    "codigo_cnae": data['servico']['codigo_cnae'],
                    "codigo_tributacao_municipio": data['servico']['codigo_tributacao_municipio'],
                    "aliquota": Decimal(data['servico']['aliquota']),
                }
            )
            rps = RPS(
                **{
                    "identificador": data['rps']['identificador'],
                    "data_emissao": datetime(data['rps']['year'],
                                             data['rps']['month'],
                                             data['rps']['day'],
                                             data['rps']['hour'],
                                             data['rps']['minutes'],
                                             data['rps']['seconds'],
                                             data['rps']['miliseconds']),
                    "servico": servico,
                    "prestador": self.prestador,
                    "tomador": tomador,
                    "simples": data['rps']['simples'],
                    "incentivo": data['rps']['incentivo'],
                    "numero": data['rps']['numero'],
                    "serie": data['rps']['serie'],
                    "tipo": data['rps']['tipo'],
                    "natureza_operacao": data['rps']['natureza_operacao'],
                }
            )
            lote_rps = LoteRPS(
                **{
                    "identificador": "L1",
                    "numero_lote": 1,
                    "cnpj": self.prestador.cnpj,
                    "inscricao_municipal": self.prestador.inscricao_municipal,
                    "quantidade_rps": 1,
                    "lista_rps": [rps],
                }
            )
            xml_lote_rps = s.envio_lote_rps(lote_rps)
            ret['success'] = 1
            message_status = falcon.HTTP_200
        except Exception as e:
            print(f'{str(e)}')
            message_status = falcon.HTTP_404
            ret['success'] = 0
            xml_lote_rps = str(e)
        finally:
            o = xmltodict.parse(xml_lote_rps)
            json_lote_rps = json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'
            ret['data'] = json_lote_rps
            resp.status = message_status
            resp.media = ret
            print(f"ret: {ret}")
            print(
                f"execution time: {round(time.time() - start_time, 4)} seconds")
            gc.collect()


def create_app():
    app = falcon.API()
    api = RestResource()
    health = Health()
    app.add_route('/api', api)
    app.add_route('/health', health)
    return app
