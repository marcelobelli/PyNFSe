from .base import Entidade
from decimal import Decimal


class Servico(Entidade):

    valor_servico = Decimal()
    iss_retido = int() # 1 - Sim, 2 - Não
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
    outras_retencoes = Decimal()
    aliquota = Decimal()
    desconto_incondicionado = Decimal()
    desconto_condicionado = Decimal()

    def __init__(self, **kwargs):

        super(Servico, self).__init__(**kwargs)

        self.base_calculo = self._calcular_base_calculo()
        self.valor_iss = self._calcular_iss()
        self.valor_iss_retido = self._calcular_iss() if self.iss_retido else None
        self.valor_liquido = self._calcular_valor_liquido()

    def _calcular_base_calculo(self):

        base_calculo = self.valor_servico - self.valor_deducoes - self.desconto_incondicionado

        return base_calculo

    def _calcular_valor_liquido(self):

        valor_liquido = self.valor_servico - self.valor_pis - self.valor_cofins - self.valor_inss -\
                        self.valor_ir - self.valor_csll - self.outras_retencoes - self.valor_iss_retido -\
                        self.desconto_incondicionado - self.desconto_condicionado

        return Decimal(valor_liquido)

    def _calcular_iss(self):

        valor_iss = self.base_calculo * self.aliquota

        return valor_iss