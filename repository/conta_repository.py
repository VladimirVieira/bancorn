from decimal import Decimal
from typing import TypeAlias

from config.database import obter_conexao_banco
from domain.conta import Conta
from domain.conta_bonus import ContaBonus
from domain.conta_poupanca import ContaPoupanca
from repository.conta_repository_interface import ContaRepositoryInterface

TuplaConta: TypeAlias = tuple[str, Decimal, str, int]


def obter_tipo_conta(conta: Conta) -> str:
    match conta:
        case ContaPoupanca():
            return "poupanca"
        case ContaBonus():
            return "bonus"
        case _:
            return "corrente"


class ContaRepository(ContaRepositoryInterface):
    def criar_conta(self, conta: Conta) -> None:
        with obter_conexao_banco() as conn, conn.cursor() as cursor:
            cursor.execute(
                """
                    INSERT INTO contas (numero, saldo, tipo, pontos, agencia_id)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                (
                    conta.numero,
                    conta.obter_saldo(),
                    obter_tipo_conta(conta),
                    getattr(conta, "_pontuacao", 0),
                    None,
                ),
            )

    def persistir_conta(self, conta: Conta) -> None:
        with obter_conexao_banco() as conn, conn.cursor() as cursor:
            cursor.execute(
                """
                    UPDATE contas
                    SET saldo = %s, tipo = %s, pontos = %s
                    WHERE numero = %s
                    """,
                (
                    conta.obter_saldo(),
                    obter_tipo_conta(conta),
                    getattr(conta, "_pontuacao", 0),
                    conta.numero,
                ),
            )

    def listar_contas(self) -> list[str]:
        with obter_conexao_banco() as conn, conn.cursor() as cursor:
            cursor.execute("SELECT numero pontos FROM contas")
            numeros_conta: list[tuple[str]] = cursor.fetchall()

        return [conta[0] for conta in numeros_conta]

    def obter_conta(self, numero: str) -> Conta:
        with obter_conexao_banco() as conn, conn.cursor() as cursor:
            cursor.execute(
                "SELECT numero, saldo, tipo, pontos FROM contas WHERE numero = %s",
                (numero,),
            )
            result = cursor.fetchone()

        if not result:
            raise ValueError(f"Conta com número {numero} não encontrada.")

        conta: TuplaConta = result

        return self._mapear_conta(conta)

    def _mapear_conta(self, dados: TuplaConta) -> Conta:
        numero, saldo, tipo, pontos = dados
        saldo = Decimal(saldo)

        match tipo:
            case "poupanca":
                return ContaPoupanca(numero, saldo)
            case "bonus":
                conta = ContaBonus(numero)
                conta._pontuacao = pontos  # noqa: SLF001
                return conta
            case _:
                return Conta(numero, saldo)
