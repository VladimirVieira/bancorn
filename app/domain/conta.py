from decimal import Decimal

from .excecoes import SaldoInsuficiente, ValorOperacaoInvalido


class Conta:
    def __init__(self, numero: str) -> None:
        self.numero = numero
        self._saldo = Decimal("0.00")

    def depositar(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido()
        self._saldo += valor

    def transferir(self, valor: Decimal, conta: "Conta") -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido()
        self.debitar(valor)
        conta.creditar(valor)

    def creditar(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido()
        self._saldo += valor

    def debitar(self, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorOperacaoInvalido()
        if valor > self._saldo:
            raise SaldoInsuficiente()
        self._saldo -= valor

    @staticmethod
    def formatar_saldo(saldo: Decimal) -> str:
        return f"R$ {saldo:.2f}"

    def __str__(self) -> str:
        return f"Conta Simples {self.numero} - Saldo: {self.formatar_saldo(self._saldo)}"

    def __hash__(self) -> int:
        return hash(self.numero)
