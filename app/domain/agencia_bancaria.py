from typing import List, Optional, Tuple
from .conta import Conta

class AgenciaBancaria(object):
    
    def __init__(self) -> None:
        self.contas: List[Conta] = []



    def comparaConta(self, testeconta: int) -> bool:
        for id in self.contas:
            if id.numero == testeconta:
                return True
        return False

    def cadastrarConta(self, numeroConta: int) -> bool:
        if not self.comparaConta(numeroConta):
            self.contas.append(Conta(numeroConta))
            return True
        return False


    def consultarSaldo(self, numeroConta: int) -> Optional[Tuple[int, float]]:
        for i in self.contas:
            if i.numero == numeroConta:
                return i.numero, i.saldo
        return None



    def atualizarCredito(self, numeroConta: int, valor: float) -> bool:
        for i in self.contas:
            if i.numero == numeroConta:
                i.saldo+=valor
                return True
        return False
 

    def atualizarDebito(self, numeroConta: int, valor: float) -> bool:
        for i in self.contas:
            if i.numero == numeroConta:
              i.saldo-=valor
              return True
        return False

    def realizarTransferencia(self, contaorigem: int, contadestino: int, valor: float) -> bool:
        origem: Optional[Conta] = None
        destino: Optional[Conta] = None

        for conta in self.contas:
            if conta.numero == contaorigem:
                origem = conta
            elif conta.numero == contadestino:
                destino = conta

        if origem and destino:
            origem.escolherDebito(valor)
            destino.escolherCredito(valor)
            return True
        return False