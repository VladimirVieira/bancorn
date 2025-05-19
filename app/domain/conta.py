from decimal import Decimal

class Conta:
    def __init__(self, numero: str) -> None:
        self.numero = numero
        self._saldo = Decimal('0.00')

    def obter_saldo(self) -> Decimal:
        return self._saldo

    def creditar(self, valor: Decimal) -> None:
        self._saldo += valor

    def debitar(self, valor: Decimal) -> None:
        self._saldo -= valor

    @staticmethod
    def formatar_saldo(saldo: Decimal) -> str:
        return f'R$ {saldo:.2f}'

    def __str__(self) -> str:
        return f'Conta {self.numero} - Saldo: {self.formatar_saldo(self._saldo)}'
    
    def __hash__(self) -> int:
        return hash(self.numero)
