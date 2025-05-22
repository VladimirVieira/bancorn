from decimal import Decimal

from conta import Conta

from .excecoes import ValorOperacaoInvalido


class ContaPoupanca(Conta):
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
