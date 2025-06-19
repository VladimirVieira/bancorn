from abc import ABC, abstractmethod
from app.domain.conta import Conta

class ContaRepositoryInterface(ABC):
    @abstractmethod
    def criar_conta(self, conta: Conta) -> None:
        pass

    @abstractmethod
    def persistir_conta(self, conta: Conta) -> None:
        pass

    @abstractmethod
    def listar_contas(self) -> list[str]:
        pass

    @abstractmethod
    def obter_conta(self, numero: str) -> Conta:
        pass
