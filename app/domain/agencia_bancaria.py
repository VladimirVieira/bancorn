from decimal import Decimal
from typing import List

from conta import Conta
from excecoes import ContaJaExiste, ContaNaoEncontrada, ValorTransferenciaInvalido


class AgenciaBancaria:
    def __init__(self) -> None:
        self.contas: List[Conta] = []

    def criar_conta_simples(self, numero: str, saldo_inicial: Decimal) -> Conta:
        if any(c.numero == numero for c in self.contas):
            raise ContaJaExiste()
        
        nova_conta = Conta(numero, saldo_inicial)
        self.contas.append(nova_conta)
        
        return nova_conta

    def buscar_conta(self, numero: str) -> Conta:
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        raise ContaNaoEncontrada()

    def consultar_saldo(self, numero: str) -> str:
        conta = self.buscar_conta(numero)
        return Conta.formatar_saldo(conta.obter_saldo())

    def creditar(self, numero: str, valor: Decimal) -> None:
        conta = self.buscar_conta(numero)
        conta.creditar(valor)

    def debitar(self, numero: str, valor: Decimal) -> None:
        conta = self.buscar_conta(numero)
        conta.debitar(valor)

    def transferir(
        self, origem_numero: str, destino_numero: str, valor: Decimal
    ) -> None:
        if valor <= 0:
            raise ValorTransferenciaInvalido()
        conta_origem = self.buscar_conta(origem_numero)
        conta_destino = self.buscar_conta(destino_numero)
        conta_origem.debitar(valor)
        conta_destino.creditar(valor)
