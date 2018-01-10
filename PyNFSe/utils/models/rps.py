import typing

from datetime import datetime

from simple_model import Model

from . import Prestador, Servico, Tomador


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
