from decimal import Decimal
from typing import List

from conta_poupanca import ContaPoupanca
from conta import Conta
from excecoes import ContaJaExiste, ContaNaoEncontrada


class AgenciaBancaria:
    def __init__(self) -> None:
        self.contas: List[Conta] = []

    def criar_conta(self, numero: str) -> Conta:
        if any(c.numero == numero for c in self.contas):
            raise ContaJaExiste()
        nova_conta = Conta(numero)
        self.contas.append(nova_conta)
        return nova_conta
        
    def criar_conta_poupanca(self, numero: str, saldo_inicial: Decimal) -> ContaPoupanca:
        if any(c.numero == numero for c in self.contas):
            raise ContaJaExiste()
        nova_conta = ContaPoupanca(numero, saldo_inicial)
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
        conta_origem = self.buscar_conta(origem_numero)
        conta_destino = self.buscar_conta(destino_numero)
        conta_origem.transferir(valor, conta_destino)
