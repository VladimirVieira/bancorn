from app.domain.conta import Conta, TipoOperacao
from app.domain.conta_bonus import ContaBonus
from app.domain.conta_poupanca import ContaPoupanca
from app.dto.conta_dto import (
    CadastrarContaDTO,
    CreditarDebitarDTO,
    RenderJurosDTO,
    TransferirDTO,
    TipoConta,
)
from app.repository.conta_repository_interface import ContaRepositoryInterface
from app.repository.operacao_repository_interface import OperacaoRepositoryInterface


class ContaService:
    def __init__(
        self,
        conta_repo: ContaRepositoryInterface,
        operacao_repo: OperacaoRepositoryInterface,
    ):
        self.conta_repo = conta_repo
        self.operacao_repo = operacao_repo

    def cadastrar_conta(self, dados: CadastrarContaDTO) -> None:
        match dados.tipo:
            case TipoConta.POUPANCA:
                conta = ContaPoupanca(dados.numero, dados.saldo_inicial)
            case TipoConta.BONUS:
                conta = ContaBonus(dados.numero, dados.saldo_inicial)
            case _:
                conta = Conta(dados.numero, dados.saldo_inicial)
        self.conta_repo.criar_conta(conta)

    def listar_numeros_contas(self) -> list[str]:
        return self.conta_repo.listar_contas()

    def consultar_conta(self, numero: str) -> Conta:
        return self.conta_repo.obter_conta(numero)

    def creditar(self, dados: CreditarDebitarDTO) -> None:
        conta = self.conta_repo.obter_conta(dados.numero)
        conta.creditar(dados.valor)
        self.conta_repo.persistir_conta(conta)
        self.operacao_repo.cadastrar_operacao(
            conta, None, dados.valor, TipoOperacao.DEPOSITO
        )

    def debitar(self, dados: CreditarDebitarDTO) -> None:
        conta = self.conta_repo.obter_conta(dados.numero)
        if dados.valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        if conta._saldo < dados.valor:
            raise ValueError("Saldo insuficiente.")
        conta.debitar(dados.valor)
        self.conta_repo.persistir_conta(conta)
        self.operacao_repo.cadastrar_operacao(
            conta, None, dados.valor, TipoOperacao.SAQUE
        )

    def transferir(self, dados: TransferirDTO) -> None:
        origem = self.conta_repo.obter_conta(dados.origem)
        destino = self.conta_repo.obter_conta(dados.destino)
        if dados.valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        if origem._saldo < dados.valor:
            raise ValueError("Saldo insuficiente.")
        origem.transferir(dados.valor, destino)
        self.conta_repo.persistir_conta(origem)
        self.conta_repo.persistir_conta(destino)
        self.operacao_repo.cadastrar_operacao(
            origem, destino, dados.valor, TipoOperacao.TRANSFERENCIA
        )

    def render_juros(self, dados: RenderJurosDTO) -> None:
        conta = self.conta_repo.obter_conta(dados.numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(dados.taxa_percentual)
            self.conta_repo.persistir_conta(conta)
