import typing
from datetime import datetime
from decimal import Decimal

from simple_model import Model


class Prestador(Model):

    cnpj: str
    inscricao_municipal: str


class Tomador(Model):
    razao_social: str
    tipo_documento: str = 'CNPJ'
    numero_documento: str
    inscricao_municipal: typing.Any = None

    endereco: str
    endereco_numero: str
    endereco_complemento: typing.Any = None
    bairro: str
    codigo_municipio: typing.Any = None
    uf: str
    cep: str

    telefone: typing.Any = None
    email: typing.Any = None


class Servico(Model):

    valor_servico: Decimal = 0
    iss_retido: int  # 1 - Sim, 2 - Não
    item_lista: str
    discriminacao: str
    codigo_municipio: str
    codigo_cnae: typing.Any = None
    codigo_tributacao_municipio: typing.Any = None

    valor_deducoes: Decimal = 0
    valor_pis: Decimal = 0
    valor_cofins: Decimal = 0
    valor_inss: Decimal = 0
    valor_ir: Decimal = 0
    valor_csll: Decimal = 0
    outras_retencoes: Decimal = 0
    aliquota: Decimal = 0
    desconto_incondicionado: Decimal = 0
    desconto_condicionado: Decimal = 0

    def __post_init__(self, **kwargs):
        self.gerar_valores_faltantes()

    def gerar_valores_faltantes(self):
        self.base_calculo = self._calcular_base_calculo()
        self.valor_iss = self._calcular_iss()
        self.valor_iss_retido = Decimal() if self.iss_retido == 2 else self.valor_iss
        self.valor_liquido = self._calcular_valor_liquido()

    def _calcular_base_calculo(self):
        return self.valor_servico - self.valor_deducoes - self.desconto_incondicionado

    def _calcular_valor_liquido(self):
        descontos = [self.valor_pis, self.valor_cofins, self.valor_inss, self.valor_ir, self.valor_csll,
                     self.outras_retencoes, self.valor_iss_retido, self.desconto_incondicionado,
                     self.desconto_condicionado]
        desconto_total = sum(descontos)

        return Decimal(self.valor_servico - desconto_total)

    def _calcular_iss(self):
        return Decimal(self.base_calculo * self.aliquota).quantize(Decimal('0.01'))


class RPS(Model):
    identificador: str
    data_emissao: datetime
    servico: Servico
    prestador: Prestador
    tomador: Tomador
    simples: int
    incentivo: int
    numero: int
    serie: str
    tipo: str
    natureza_operacao: int
    regime_especial: typing.Any = None


class LoteRPS(Model):
    identificador: str
    numero_lote: int
    cnpj: str
    inscricao_municipal: str
    lista_rps: typing.List[RPS]


class PedidoCancelamentoNFSe(Model):

    identificador: str
    prestador: Prestador
    numero_nota: int
    codigo_municipio: str
    codigo_cancelamento: str


class Configuracao(Model):
    simples: int
    incentivo: int
    regime_especial: int
    natureza_operacao: int
    codigo_municipio: str
    iss_retido: int
    item_lista: str
    codigo_cnae: int
    codigo_tributacao_municipio: str
    aliquota: Decimal


class Ambiente(Model):
    numero_rps: int
    numero_lote: int
    certificado: str
    senha: str
