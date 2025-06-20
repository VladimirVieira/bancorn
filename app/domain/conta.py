from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum

from app.domain.excecoes import (
    SaldoInicialInvalido,
    SaldoInsuficiente,
    ValorOperacaoInvalido,
)


class TipoOperacao(StrEnum):
    DEPOSITO = "deposito"
    SAQUE = "saque"
    TRANSFERENCIA = "transferencia"
    CONSULTA_SALDO = "consulta_saldo"
    RENDIMENTO = "rendimento"


@dataclass
class Operacao:
    tipo: TipoOperacao
    valor: Decimal
    origem: str
    destino: str | None


class Conta:
    SALDO_MINIMO = -Decimal("1000.00")

    def __init__(self, numero: str, saldo_inicial: Decimal) -> None:
        if saldo_inicial < 0:
            raise SaldoInicialInvalido()
        self.numero = numero
        self._saldo = saldo_inicial

    def depositar(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido("O valor deve ser maior que zero.")
        self._saldo += valor

    def transferir(self, valor: Decimal, conta: "Conta") -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido("O valor deve ser maior que zero.")
        self.debitar(valor)
        conta.receber_transferencia(valor)

    def receber_transferencia(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido("O valor deve ser maior que zero.")
        self._saldo += valor

    def debitar(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido("O valor deve ser maior que zero.")
        if self._saldo - valor < self.SALDO_MINIMO:
            raise SaldoInsuficiente()
        self._saldo -= valor

    def creditar(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido("O valor deve ser maior que zero.")
        self._saldo += valor


    @staticmethod
    def formatar_saldo(saldo: Decimal) -> str:
        return f"R$ {saldo:.2f}"

    def __str__(self) -> str:
        return (
            f"Conta Simples {self.numero} - Saldo: {self.formatar_saldo(self._saldo)}"
        )

    def __hash__(self) -> int:
        return hash(self.numero)
