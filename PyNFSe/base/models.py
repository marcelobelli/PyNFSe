from datetime import datetime
from decimal import Decimal
from typing import Any, List

from simple_model import Model
from simple_model.exceptions import ValidationError


class Prestador(Model):

    cnpj: str
    inscricao_municipal: str

    def __post_init__(self, **kwargs):
        self.validate()

    def validate_cnpj(self, cnpj: str):
        if len(cnpj) != 14 or not cnpj.isdigit():
            raise ValidationError('CNPJ deve conter 14 caracteres, sendo todos números.')

        return cnpj


class Tomador(Model):
    inscricao_municipal: Any = None
    numero_documento: str
    razao_social: str
    tipo_documento: str

    bairro: str
    cep: str
    codigo_municipio: str
    endereco: str
    endereco_complemento: Any = None
    endereco_numero: str
    uf: str

    email: Any = None
    telefone: Any = None

    def __post_init__(self, **kwargs):
        self.validate()

    def validate_tipo_documento(self, tipo_documento: str):
        if tipo_documento.upper() not in ['CPF', 'CNPJ']:
            raise ValidationError('O tipo de documento do tomador deve ser CPF ou CNPJ.')

        return tipo_documento.upper()

    def validate_numero_documento(self, numero_documento: str):
        validators = {
            'CPF': self._validate_cpf,
            'CNPJ': self._validate_cnpj,
        }
        validator = validators.get(self.tipo_documento.upper())

        if not validator:
            return numero_documento

        return validator(numero_documento)

    def _validate_cpf(self, numero_documento: str):
        if len(numero_documento) != 11 or not numero_documento.isdigit():
            raise ValidationError('CPF deve conter 11 caracteres, sendo todos números.')

        return numero_documento

    def _validate_cnpj(self, numero_documento: str):
        if len(numero_documento) != 14 or not numero_documento.isdigit():
            raise ValidationError('CNPJ deve conter 14 caracteres, sendo todos números.')

        return numero_documento


class Servico(Model):
    aliquota: Decimal
    codigo_cnae: Any = None
    codigo_municipio: str
    codigo_tributacao_municipio: Any = None
    discriminacao: str
    iss_retido: int
    item_lista: str
    valor_servico: Decimal

    desconto_condicionado: Decimal = 0
    desconto_incondicionado: Decimal = 0
    outras_retencoes: Decimal = 0
    valor_cofins: Decimal = 0
    valor_csll: Decimal = 0
    valor_deducoes: Decimal = 0
    valor_inss: Decimal = 0
    valor_ir: Decimal = 0
    valor_pis: Decimal = 0

    def __post_init__(self, **kwargs):
        self.gerar_valores_faltantes()
        self.validate()

    def validate_iss_retido(self, iss_retido):
        if iss_retido not in [1, 2]:
            raise ValidationError('ISS Retido deve ser 1 para SIM ou 2 para NÃO.')

        return iss_retido

    def gerar_valores_faltantes(self):
        self.base_calculo = self._calcular_base_calculo()
        self.valor_iss = self._calcular_iss()
        self.valor_iss_retido = Decimal() if self.iss_retido == 2 else self.valor_iss
        self.valor_liquido = self._calcular_valor_liquido()

    def _calcular_base_calculo(self):
        return self.valor_servico - self.valor_deducoes - self.desconto_incondicionado

    def _calcular_valor_liquido(self):
        descontos = sum([
            self.desconto_condicionado,
            self.desconto_incondicionado,
            self.outras_retencoes,
            self.valor_cofins,
            self.valor_csll,
            self.valor_inss,
            self.valor_ir,
            self.valor_iss_retido,
            self.valor_pis,
        ])

        return Decimal(self.valor_servico - descontos)

    def _calcular_iss(self):
        return Decimal(self.base_calculo * self.aliquota).quantize(Decimal('0.01'))


class RPS(Model):
    data_emissao: datetime
    identificador: str
    incentivo: int
    natureza_operacao: int
    numero: int
    prestador: Prestador
    regime_especial: Any = None
    serie: str
    servico: Servico
    simples: int
    tipo: str
    tomador: Tomador

    def __post_init__(self, **kwargs):
        self.validate()

    def validate_natureza_operacao(self, natureza_operacao: int):
        if natureza_operacao not in range(1, 7):
            raise ValidationError('Natureza da Operação deve ser um número entre 1 e 6.')

        return natureza_operacao

    def validate_regime_especial(self, regime_especial: Any):
        if regime_especial is None:
            return regime_especial

        if type(regime_especial) != int or type(regime_especial) == int and regime_especial not in range(0, 5):
            raise ValidationError('Regime Especial deve ser um número entre 0 e 4 ou None.')

        return regime_especial

    @classmethod
    def criar_a_partir_de_dados(cls, dados_rps: dict) -> 'RPS':
        return cls(
            data_emissao=dados_rps['data_emissao'],
            identificador=dados_rps['identificador'],
            incentivo=dados_rps['incentivo'],
            natureza_operacao=dados_rps['natureza_operacao'],
            numero=dados_rps['numero'],
            prestador=Prestador(**dados_rps['prestador']),
            regime_especial=dados_rps.get('regime_especial'),
            serie=dados_rps['serie'],
            servico=Servico(**dados_rps['servico']),
            simples=dados_rps['simples'],
            tipo=dados_rps['tipo'],
            tomador=Tomador(**dados_rps['tomador']),
        )


class LoteRPS(Model):
    cnpj: str
    identificador: str
    inscricao_municipal: str
    lista_rps: List[RPS]
    numero_lote: int

    def __post_init__(self, **kwargs):
        self.validate()

    def validate_cnpj(self, cnpj: str):
        if len(cnpj) != 14 or not cnpj.isdigit():
            raise ValidationError('CNPJ deve conter 14 caracteres, sendo todos números.')

        return cnpj

    @classmethod
    def criar_a_partir_de_dados(cls, dados_lote_rps: dict) -> 'LoteRPS':
        return cls(
            cnpj=dados_lote_rps['cnpj'],
            identificador=dados_lote_rps['identificador'],
            inscricao_municipal=dados_lote_rps['inscricao_municipal'],
            lista_rps=[RPS.criar_a_partir_de_dados(dados_rps) for dados_rps in dados_lote_rps['lista_rps']],
            numero_lote=dados_lote_rps['numero_lote'],
        )


class PedidoCancelamentoNFSe(Model):
    identificador: str
    prestador: Prestador
    numero_nota: int
    codigo_municipio: str
    codigo_cancelamento: str
