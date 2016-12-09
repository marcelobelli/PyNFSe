from .base import Entidade
from decimal import Decimal


class Servico(Entidade):

    valor_servico = Decimal()
    iss_retido = int()
    item_lista = str()
    discriminacao = str()
    codigo_municipio = str()
    codigo_cnae = int()
    codigo_tributacao_municipio = str()

    valor_deducoes = Decimal()
    valor_pis = Decimal()
    valor_cofins = Decimal()
    valor_inss = Decimal()
    valor_ir = Decimal()
    valor_csll = Decimal()
    valor_iss = Decimal()
    valor_iss_retido = Decimal()
    valor_liquido = Decimal()
    outras_retencoes = Decimal()
    base_calculo = Decimal()
    aliquota = Decimal()
    desconto_incondicionado = Decimal()
    desconto_condicionado = Decimal()