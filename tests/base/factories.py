from datetime import datetime
from decimal import Decimal

from factory import Factory
from pynfse.base import models


class PrestadorFactory(Factory):
    cnpj = "12345678901234"
    inscricao_municipal = "1234567890"

    class Meta:
        model = models.Prestador


class TomadorFactory(Factory):
    razao_social = "Nome do Tomador"
    tipo_documento = "CNPJ"
    numero_documento = "12345678901234"
    endereco = "Rua Getúlio Vargas"
    endereco_numero = "1000"
    bairro = "Bairro Centro"
    codigo_municipio = "4106902"
    uf = "PR"
    cep = "80000000"

    class Meta:
        model = models.Tomador


class ServicoFactory(Factory):
    valor_servico = Decimal("1000.00")
    iss_retido = 1
    item_lista = "0107"
    discriminacao = "Teste Integração"
    codigo_municipio = "4106902"
    aliquota = Decimal("0.02")

    class Meta:
        model = models.Servico


class RPSFactory(Factory):
    identificador = "N1"
    data_emissao = datetime.today()
    servico = ServicoFactory()
    prestador = PrestadorFactory()
    tomador = TomadorFactory()
    simples = 1
    incentivo = 2
    numero = 1
    serie = "A1"
    tipo = "1"
    natureza_operacao = 1

    class Meta:
        model = models.RPS


class LoteRPSFactory(Factory):
    identificador = "L1"
    numero_lote = 1
    cnpj = "12345678901234"
    inscricao_municipal = "1234567890"
    lista_rps = [RPSFactory()]

    class Meta:
        model = models.LoteRPS
