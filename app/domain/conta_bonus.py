from decimal import Decimal

from conta import Conta


class ContaBonus(Conta):
    VALOR_PARA_PONTOS_DEPOSITO = 100
    VALOR_PARA_PONTOS_TRANSFERENCIA = 200

    def __init__(self, numero: str) -> None:
        super().__init__(numero)
        self._pontuacao = 10

    def obter_pontuacao(self) -> int:
        return self._pontuacao

    def depositar(self, valor: Decimal) -> None:
        super().depositar(valor)
        self._pontuacao += int(valor // self.VALOR_PARA_PONTOS_DEPOSITO)

    def transferir(self, valor: Decimal, conta: "Conta") -> None:
        super().transferir(valor, conta)
        self._pontuacao += int(valor // self.VALOR_PARA_PONTOS_TRANSFERENCIA)

    def __str__(self) -> str:
        return f"Conta Bônus {self.numero} - Saldo: {self.formatar_saldo(self._saldo)} - Pontuação: {self._pontuacao}"
