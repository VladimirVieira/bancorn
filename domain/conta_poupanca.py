from decimal import Decimal

from domain.conta import Conta
from domain.excecoes import SaldoInicialInvalidoError, ValorOperacaoInvalidoError


class ContaPoupanca(Conta):
    TAXA_PERCENTUAL_MAXIMA_JUROS = 100
    SALDO_MINIMO = Decimal("0.00")

    def __init__(self, numero: str, saldo_inicial: Decimal) -> None:
        if saldo_inicial < 0:
            raise SaldoInicialInvalidoError
        super().__init__(numero, saldo_inicial)
        self._saldo = saldo_inicial

    def render_juros(self, taxa_percentual: Decimal) -> None:
        if taxa_percentual <= 0 or taxa_percentual > self.TAXA_PERCENTUAL_MAXIMA_JUROS:
            raise ValorOperacaoInvalidoError(
                "A taxa percentual deve ser um valor entre 0 e 100.",
            )
        self._saldo += self._saldo * taxa_percentual / Decimal(100)

    def __str__(self) -> str:
        return (
            f"Conta Poupança {self.numero} - Saldo: {self.formatar_saldo(self._saldo)}"
        )
