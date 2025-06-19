from decimal import Decimal
from app.domain.conta import Conta, TipoOperacao
from app.repository.operacao_repository_interface import OperacaoRepositoryInterface
from app.config.database import obter_conexao_banco

class OperacaoRepository(OperacaoRepositoryInterface):
    def cadastrar_operacao(self, origem: Conta, destino: Conta | None, valor: Decimal, tipo: TipoOperacao) -> None:
        with obter_conexao_banco() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO operacoes (tipo, valor, conta_origem_id, conta_destino_id)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (tipo.value, valor, origem.numero, destino.numero if destino else None),
                )
