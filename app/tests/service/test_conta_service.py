from decimal import Decimal

import pytest

from app.domain.conta import Conta
from app.domain.conta_bonus import ContaBonus
from app.domain.conta_poupanca import ContaPoupanca
from app.dto.conta_dto import (
    CadastrarContaDTO,
    CreditarDebitarDTO,
    RenderJurosDTO,
    TipoConta,
    TransferirDTO,
)
from app.service.conta_service import ContaService
from app.tests.mock.fake_conta_repository import FakeContaRepository
from app.tests.mock.fake_operacao_repository import FakeOperacaoRepository


@pytest.fixture
def conta_service():
    conta_repo = FakeContaRepository()
    operacao_repo = FakeOperacaoRepository()
    return ContaService(conta_repo, operacao_repo)


# Testes para Cadastrar Conta


def test_cadastrar_conta_corrente(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789012", saldo_inicial=Decimal("500.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    assert conta_service.conta_repo.obter_conta("123456789012")._saldo == Decimal(
        "500.00"
    )


def test_cadastrar_conta_poupanca(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    assert conta_service.conta_repo.obter_conta("123")._saldo == Decimal("100.00")


def test_cadastrar_conta_bonus(conta_service):
    dados = CadastrarContaDTO(
        numero="456", saldo_inicial=Decimal("0.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    assert conta_service.conta_repo.obter_conta("456")._saldo == Decimal("0.00")


# Testes para Consultar Conta
def test_consultar_conta_corrente(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789014", saldo_inicial=Decimal("300.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("123456789014")

    assert isinstance(conta, Conta)
    assert conta._saldo == Decimal("300.00")


def test_consultar_conta_poupanca(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("123")

    assert isinstance(conta, ContaPoupanca)
    assert conta._saldo == Decimal("100.00")


def test_consultar_conta_bonus(conta_service):
    dados = CadastrarContaDTO(
        numero="456", saldo_inicial=Decimal("0.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    conta: ContaBonus = conta_service.consultar_conta("456")

    assert isinstance(conta, ContaBonus)
    assert conta._saldo == Decimal("0.00")
    assert conta._pontuacao == 10


# Testes para Crédito
def test_creditar_valor_normal(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    creditar_dados = CreditarDebitarDTO(numero="123", valor=Decimal("50.00"))
    conta_service.creditar(creditar_dados)

    assert conta_service.consultar_conta("123")._saldo == Decimal("150.00")


def test_creditar_valor_negativo(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    creditar_dados = CreditarDebitarDTO(numero="123", valor=Decimal("-50.00"))
    with pytest.raises(Exception):
        conta_service.creditar(creditar_dados)


def test_credito_normal(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789017", saldo_inicial=Decimal("600.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    credito_dto = CreditarDebitarDTO(numero="123456789017", valor=Decimal("100.00"))
    conta_service.creditar(credito_dto)
    assert conta_service.consultar_conta("123456789017")._saldo == Decimal("700.00")


def test_debitar_valor_negativo(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    debitar_dados = CreditarDebitarDTO(numero="123", valor=Decimal("-50.00"))
    with pytest.raises(Exception):
        conta_service.debitar(debitar_dados)


def test_debitar_saldo_insuficiente(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    debitar_dados = CreditarDebitarDTO(numero="123", valor=Decimal("150.00"))
    with pytest.raises(Exception):
        conta_service.debitar(debitar_dados)


def test_debito_normal(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789020", saldo_inicial=Decimal("900.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = CreditarDebitarDTO(numero="123456789020", valor=Decimal("100.00"))
    conta_service.debitar(debito_dto)
    assert conta_service.consultar_conta("123456789020")._saldo == Decimal("800.00")


def test_debito_valor_negativo(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789021", saldo_inicial=Decimal("1000.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = CreditarDebitarDTO(numero="123456789021", valor=Decimal("-100.00"))
    with pytest.raises(ValueError):
        conta_service.debitar(debito_dto)


def test_debito_saldo_negativo(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("50.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = CreditarDebitarDTO(numero="123456789022", valor=Decimal("100.00"))
    with pytest.raises(ValueError):
        conta_service.debitar(debito_dto)


# Testes para Transferência
def test_transferir_valor_negativo(conta_service):
    dados_origem = CadastrarContaDTO(
        numero="123456789023", saldo_inicial=Decimal("1000.00"), tipo=TipoConta.CORRENTE
    )
    dados_destino = CadastrarContaDTO(
        numero="123456789024", saldo_inicial=Decimal("500.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados_origem)
    conta_service.cadastrar_conta(dados_destino)
    transferir_dados = TransferirDTO(
        origem="123456789023", destino="123456789024", valor=Decimal("-100.00")
    )
    with pytest.raises(ValueError):
        conta_service.transferir(transferir_dados)


def test_transferir_saldo_insuficiente(conta_service):
    dados_origem = CadastrarContaDTO(
        numero="123456789025", saldo_inicial=Decimal("50.00"), tipo=TipoConta.CORRENTE
    )
    dados_destino = CadastrarContaDTO(
        numero="123456789026", saldo_inicial=Decimal("500.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados_origem)
    conta_service.cadastrar_conta(dados_destino)
    transferir_dados = TransferirDTO(
        origem="123456789025", destino="123456789026", valor=Decimal("100.00")
    )
    with pytest.raises(ValueError):
        conta_service.transferir(transferir_dados)


def test_transferencia_entre_contas_bonus(conta_service):
    dados_origem = CadastrarContaDTO(
        numero="123456789027", saldo_inicial=Decimal("1000.00"), tipo=TipoConta.BONUS
    )
    dados_destino = CadastrarContaDTO(
        numero="123456789028", saldo_inicial=Decimal("1000.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados_origem)
    conta_service.cadastrar_conta(dados_destino)

    transferir_dados = TransferirDTO(
        origem="123456789027", destino="123456789028", valor=Decimal("500.00")
    )

    conta_service.transferir(transferir_dados)

    conta_origem = conta_service.consultar_conta("123456789027")
    conta_destino = conta_service.consultar_conta("123456789028")

    assert conta_origem._saldo == Decimal("500.00")
    assert conta_destino._saldo == Decimal("1500.00")
    assert conta_origem._pontuacao == 12
    assert conta_destino._pontuacao == 13


# Testes para Render Juros
def test_render_juros_poupanca(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    render_dados = RenderJurosDTO(numero="123", taxa_percentual=Decimal("5.00"))
    conta_service.render_juros(render_dados)
    assert conta_service.consultar_conta("123")._saldo == Decimal("105.00")


def test_render_juros(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789029", saldo_inicial=Decimal("1000.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    render_juros_dto = RenderJurosDTO(
        numero="123456789029", taxa_percentual=Decimal("5.00")
    )
    conta_service.render_juros(render_juros_dto)
    assert conta_service.consultar_conta("123456789029")._saldo == Decimal("1050.00")
