from domain.conta import Conta, TipoOperacao
from domain.conta_bonus import ContaBonus
from domain.conta_poupanca import ContaPoupanca
from dto.conta_dto import (
    CadastrarContaDTO,
    RenderJurosDTO,
    SacarDepositarDTO,
    TipoConta,
    TransferirDTO,
)
from repository.conta_repository_interface import ContaRepositoryInterface
from repository.operacao_repository_interface import OperacaoRepositoryInterface


class ContaService:
    def __init__(
        self,
        conta_repo: "ContaRepositoryInterface",
        operacao_repo: "OperacaoRepositoryInterface",
    ):
        self.conta_repo = conta_repo
        self.operacao_repo = operacao_repo

    def cadastrar_conta(self, dados: CadastrarContaDTO) -> None:
        match dados.tipo:
            case TipoConta.POUPANCA:
                conta: Conta = ContaPoupanca(dados.numero, dados.saldo_inicial)
            case TipoConta.BONUS:
                conta = ContaBonus(dados.numero, dados.saldo_inicial)
            case _:
                conta = Conta(dados.numero, dados.saldo_inicial)
        self.conta_repo.criar_conta(conta)

    def listar_numeros_contas(self) -> list[str]:
        return self.conta_repo.listar_contas()

    def consultar_conta(self, numero: str) -> Conta:
        return self.conta_repo.obter_conta(numero)

    def depositar(self, numero: str, dados: SacarDepositarDTO) -> None:
        conta = self.conta_repo.obter_conta(numero)
        conta.depositar(dados.valor)
        self.conta_repo.persistir_conta(conta)
        self.operacao_repo.cadastrar_operacao(
            conta, None, dados.valor, TipoOperacao.DEPOSITO
        )

    def sacar(self, numero: str, dados: SacarDepositarDTO) -> None:
        conta = self.conta_repo.obter_conta(numero)
        conta.debitar(dados.valor)

        self.conta_repo.persistir_conta(conta)
        self.operacao_repo.cadastrar_operacao(
            conta, None, dados.valor, TipoOperacao.SAQUE
        )

    def transferir(self, dados: TransferirDTO) -> None:
        origem = self.conta_repo.obter_conta(dados.origem)
        destino = self.conta_repo.obter_conta(dados.destino)
        origem.transferir(dados.valor, destino)

        self.conta_repo.persistir_conta(origem)
        self.conta_repo.persistir_conta(destino)
        self.operacao_repo.cadastrar_operacao(
            origem, destino, dados.valor, TipoOperacao.TRANSFERENCIA
        )

    def render_juros(self, numero: str, dados: RenderJurosDTO) -> None:
        conta = self.conta_repo.obter_conta(numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(dados.taxa_percentual)
            self.conta_repo.persistir_conta(conta)
