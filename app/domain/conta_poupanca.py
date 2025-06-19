from decimal import Decimal

from app.domain.conta import Conta
from app.domain.excecoes import SaldoInicialInvalido, ValorOperacaoInvalido


class ContaPoupanca(Conta):
    SALDO_MINIMO = Decimal("0.00")

    def __init__(self, numero: str, saldo_inicial: Decimal):
        if saldo_inicial < 0:
            raise SaldoInicialInvalido()
        super().__init__(numero, saldo_inicial)
        self._saldo = saldo_inicial

    def render_juros(self, taxa_percentual: Decimal) -> None:
        if taxa_percentual <= 0 or taxa_percentual > 100:
            raise ValorOperacaoInvalido(
                "A taxa percentual deve ser um valor entre 0 e 100."
            )
        self._saldo += self._saldo * taxa_percentual / Decimal("100")

    def __str__(self) -> str:
        return (
            f"Conta Poupança {self.numero} - Saldo: {self.formatar_saldo(self._saldo)}"
        )
