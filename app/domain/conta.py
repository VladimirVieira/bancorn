class Conta (object):

    def __init__(self, numero: int) -> None:
        self.numero: int = numero
        self.saldo: float = 0.0

    def verificarSaldo(self) -> float:
        return self.saldo

    def escolherCredito(self, valor: float) -> None:
        self.saldo += valor
    
    def escolherDebito(self, valor: float) -> None:
        self.saldo -= valor