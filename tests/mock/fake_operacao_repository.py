from decimal import Decimal

from domain.conta import Conta, Operacao, TipoOperacao
from repository.operacao_repository_interface import OperacaoRepositoryInterface


class FakeOperacaoRepository(OperacaoRepositoryInterface):
    def __init__(self) -> None:
        self._operacoes: list[Operacao] = []

    def cadastrar_operacao(
        self, origem: Conta, destino: Conta | None, valor: Decimal, tipo: TipoOperacao,
    ) -> None:
        operacao = Operacao(
            tipo=tipo,
            valor=valor,
            origem=origem.numero,
            destino=destino.numero if destino else None,
        )
        self._operacoes.append(operacao)
