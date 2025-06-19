from decimal import Decimal
from enum import StrEnum

from pydantic import BaseModel


class TipoConta(StrEnum):
    CORRENTE = "corrente"
    POUPANCA = "poupanca"
    BONUS = "bonus"


class CadastrarContaDTO(BaseModel):
    numero: str
    saldo_inicial: Decimal
    tipo: TipoConta


class TransferirDTO(BaseModel):
    origem: str
    destino: str
    valor: Decimal


class CreditarDebitarDTO(BaseModel):
    numero: str
    valor: Decimal


class RenderJurosDTO(BaseModel):
    numero: str
    taxa_percentual: Decimal
