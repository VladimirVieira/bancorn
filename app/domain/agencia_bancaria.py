from decimal import Decimal

from .conta import Conta
from .excecoes import ContaJaExiste, ContaNaoEncontrada, ValorTransferenciaInvalido

class AgenciaBancaria:
    def __init__(self) -> None:
        self.contas: list[Conta] = []

    def criar_conta(self, numero: str) -> Conta:
        if any(c.numero == numero for c in self.contas):
            raise ContaJaExiste()
        
        nova_conta = Conta(numero)
        self.contas.append(nova_conta)
        
        return nova_conta

    def buscar_conta(self, numero: str) -> Conta:
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        raise ContaNaoEncontrada()
    
    def transferir(self, conta_origem: Conta, conta_destino: Conta, valor: Decimal) -> None:
        if valor <= 0:
            raise ValorTransferenciaInvalido
        
        conta_origem.debitar(valor)
        conta_destino.creditar(valor)
