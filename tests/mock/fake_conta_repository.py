from domain.conta import Conta
from repository.conta_repository_interface import ContaRepositoryInterface


class FakeContaRepository(ContaRepositoryInterface):
    def __init__(self):
        self._contas: list[Conta] = []

    def criar_conta(self, conta: Conta) -> None:
        if any(c.numero == conta.numero for c in self._contas):
            raise Exception("Conta já existe.")
        self._contas.append(conta)

    def persistir_conta(self, conta: Conta) -> None:
        for i, c in enumerate(self._contas):
            if c.numero == conta.numero:
                self._contas[i] = conta
                return
        raise Exception("Conta não encontrada.")

    def listar_contas(self) -> list[str]:
        return [c.numero for c in self._contas]

    def obter_conta(self, numero: str) -> Conta:
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        raise Exception("Conta não encontrada.")
