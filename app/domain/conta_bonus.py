from decimal import Decimal

from app.domain.conta import Conta


class ContaBonus(Conta):
    SALDO_MINIMO = -Decimal("1000.00")
    VALOR_PARA_PONTOS_DEPOSITO = 100
    VALOR_PARA_PONTOS_TRANSFERENCIA_ENVIADA = 200
    VALOR_PARA_PONTOS_TRANSFERENCIA_RECEBIDA = 150

    def __init__(self, numero: str, saldo_inicial: Decimal = Decimal("0.00")) -> None:
        super().__init__(numero, saldo_inicial)
        self._pontuacao = 10

    def obter_pontuacao(self) -> int:
        return self._pontuacao

    def depositar(self, valor: Decimal) -> None:
        super().depositar(valor)
        self._pontuacao += int(valor // self.VALOR_PARA_PONTOS_DEPOSITO)

    def transferir(self, valor: Decimal, conta: "Conta") -> None:
        super().transferir(valor, conta)
        self._pontuacao += int(valor // self.VALOR_PARA_PONTOS_TRANSFERENCIA_ENVIADA)

    def receber_transferencia(self, valor: Decimal) -> None:
        super().receber_transferencia(valor)
        self._pontuacao += int(valor // self.VALOR_PARA_PONTOS_TRANSFERENCIA_RECEBIDA)

    def __str__(self) -> str:
        return f"Conta Bônus {self.numero} - Saldo: {self.formatar_saldo(self._saldo)} - Pontuação: {self._pontuacao}"
