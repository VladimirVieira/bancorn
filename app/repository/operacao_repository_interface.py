from abc import ABC, abstractmethod
from decimal import Decimal
from app.domain.conta import Conta, TipoOperacao

class OperacaoRepositoryInterface(ABC):
    @abstractmethod
    def cadastrar_operacao(self, origem: Conta, destino: Conta | None, valor: Decimal, tipo: TipoOperacao) -> None:
        pass
