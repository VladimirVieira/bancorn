from decimal import Decimal

import pytest

from domain.conta import Conta
from domain.conta_bonus import ContaBonus
from domain.conta_poupanca import ContaPoupanca
from domain.excecoes import SaldoInsuficiente, ValorOperacaoInvalido
from dto.conta_dto import (
    CadastrarContaDTO,
    RenderJurosDTO,
    SacarDepositarDTO,
    TipoConta,
    TransferirDTO,
)
from service.conta_service import ContaService
from tests.mock.fake_conta_repository import FakeContaRepository
from tests.mock.fake_operacao_repository import FakeOperacaoRepository


@pytest.fixture
def conta_service():
    conta_repo = FakeContaRepository()
    operacao_repo = FakeOperacaoRepository()
    return ContaService(conta_repo, operacao_repo)


def test_cadastrar_corrente_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789012", saldo_inicial=Decimal("500.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("123456789012")

    assert isinstance(conta, Conta)
    assert not isinstance(conta, ContaPoupanca)
    assert not isinstance(conta, ContaBonus)
    assert conta._saldo == Decimal("500.00")


def test_cadastrar_poupanca_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("123")

    assert isinstance(conta, ContaPoupanca)
    assert conta._saldo == Decimal("100.00")


def test_cadastrar_bonus_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="456", saldo_inicial=Decimal("0.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("456")

    assert isinstance(conta, ContaBonus)
    assert conta._saldo == Decimal("0.00")
    assert conta._pontuacao == 10


def test_consultar_corrente_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789014", saldo_inicial=Decimal("300.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("123456789014")

    assert isinstance(conta, Conta)
    assert conta._saldo == Decimal("300.00")


def test_consultar_poupanca_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    conta = conta_service.consultar_conta("123")

    assert isinstance(conta, ContaPoupanca)
    assert conta._saldo == Decimal("100.00")


def test_consultar_bonus_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="456", saldo_inicial=Decimal("0.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    conta: ContaBonus = conta_service.consultar_conta("456")

    assert isinstance(conta, ContaBonus)
    assert conta._saldo == Decimal("0.00")
    assert conta._pontuacao == 10


def test_depositar_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    creditar_dados = SacarDepositarDTO(valor=Decimal("50.00"))
    conta_service.depositar("123", dados=creditar_dados)

    assert conta_service.consultar_conta("123")._saldo == Decimal("150.00")


def test_depositar_em_bonus_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="789", saldo_inicial=Decimal("200.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    depositar_dados = SacarDepositarDTO(valor=Decimal("1050.00"))
    conta_service.depositar("789", dados=depositar_dados)

    conta = conta_service.consultar_conta("789")

    assert conta._saldo == Decimal("1250.00")
    assert conta._pontuacao == 20


def test_depositar_valor_negativo_com_erro(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    creditar_dados = SacarDepositarDTO(valor=Decimal("-50.00"))
    with pytest.raises(ValorOperacaoInvalido):
        conta_service.depositar("123", dados=creditar_dados)


def test_creditar_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789017", saldo_inicial=Decimal("600.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    credito_dto = SacarDepositarDTO(valor=Decimal("100.00"))
    conta_service.depositar("123456789017", dados=credito_dto)
    assert conta_service.consultar_conta("123456789017")._saldo == Decimal("700.00")


def test_sacar_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789020", saldo_inicial=Decimal("900.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("100.00"))
    conta_service.sacar("123456789020", dados=debito_dto)
    assert conta_service.consultar_conta("123456789020")._saldo == Decimal("800.00")


def test_sacar_valor_negativo_com_erro(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789021", saldo_inicial=Decimal("1000.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("-100.00"))
    with pytest.raises(ValorOperacaoInvalido):
        conta_service.sacar("123456789021", dados=debito_dto)


def test_sacar_valor_permitindo_saldo_minimo_em_conta_corrente_com_sucesso(
    conta_service,
):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("100.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("150.00"))
    conta_service.sacar("123456789022", dados=debito_dto)

    assert conta_service.consultar_conta("123456789022")._saldo == Decimal("-50.00")


def test_sacar_valor_permitindo_saldo_minimo_em_conta_bonus_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("100.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("150.00"))
    conta_service.sacar("123456789022", dados=debito_dto)

    assert conta_service.consultar_conta("123456789022")._saldo == Decimal("-50.00")


def test_sacar_valor_permitindo_saldo_minimo_em_conta_poupanca_com_sucesso(
    conta_service,
):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("100.00"))
    conta_service.sacar("123456789022", dados=debito_dto)

    assert conta_service.consultar_conta("123456789022")._saldo == Decimal("0.00")


def test_sacar_valor_com_saldo_menor_que_o_minimo_em_conta_corrente_com_erro(
    conta_service,
):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("50.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("1100.00"))

    with pytest.raises(SaldoInsuficiente):
        conta_service.sacar("123456789022", dados=debito_dto)


def test_sacar_valor_com_saldo_menor_que_o_minimo_em_conta_bonus_com_erro(
    conta_service,
):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("50.00"), tipo=TipoConta.BONUS
    )
    conta_service.cadastrar_conta(dados)
    debito_dto = SacarDepositarDTO(valor=Decimal("1100.00"))

    with pytest.raises(SaldoInsuficiente):
        conta_service.sacar("123456789022", dados=debito_dto)


def test_sacar_valor_com_saldo_menor_que_o_minimo_em_conta_poupanca_com_erro(
    conta_service,
):
    dados = CadastrarContaDTO(
        numero="123456789022", saldo_inicial=Decimal("50.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    sacar = SacarDepositarDTO(valor=Decimal("150.00"))

    with pytest.raises(SaldoInsuficiente):
        conta_service.sacar("123456789022", dados=sacar)


def test_transferir_valor_negativo_com_erro(conta_service):
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
    with pytest.raises(ValorOperacaoInvalido):
        conta_service.transferir(transferir_dados)


def test_transferir_saldo_insuficiente_com_erro(conta_service):
    dados_origem = CadastrarContaDTO(
        numero="123456789025", saldo_inicial=Decimal("50.00"), tipo=TipoConta.CORRENTE
    )
    dados_destino = CadastrarContaDTO(
        numero="123456789026", saldo_inicial=Decimal("500.00"), tipo=TipoConta.CORRENTE
    )
    conta_service.cadastrar_conta(dados_origem)
    conta_service.cadastrar_conta(dados_destino)
    transferir_dados = TransferirDTO(
        origem="123456789025", destino="123456789026", valor=Decimal("2000.00")
    )
    with pytest.raises(SaldoInsuficiente):
        conta_service.transferir(transferir_dados)


def test_transferir_entre_bonus_com_sucesso(conta_service):
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


def test_render_juros_poupanca_com_sucesso(conta_service):
    dados = CadastrarContaDTO(
        numero="123", saldo_inicial=Decimal("100.00"), tipo=TipoConta.POUPANCA
    )
    conta_service.cadastrar_conta(dados)
    render_dados = RenderJurosDTO(taxa_percentual=Decimal("5.00"))
    conta_service.render_juros("123", dados=render_dados)
    conta = conta_service.consultar_conta("123")

    assert conta._saldo == Decimal("105.00")
