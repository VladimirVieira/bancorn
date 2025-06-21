from decimal import Decimal

from fastapi import APIRouter, HTTPException

from dto.conta_dto import (
    CadastrarContaDTO,
    SacarDepositarDTO,
    RenderJurosDTO,
    TransferirDTO,
)
from repository.conta_repository import ContaRepository
from repository.operacao_repository import OperacaoRepository
from service.conta_service import ContaService

router = APIRouter()
conta_service = ContaService(
    conta_repo=ContaRepository(), operacao_repo=OperacaoRepository()
)


@router.post("/banco/conta/")
def cadastrar_conta(dados: CadastrarContaDTO) -> dict[str, str]:
    try:
        conta_service.cadastrar_conta(dados)
        return {"message": "Conta cadastrada com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/banco/conta")
def consultar_contas() -> list[str]:
    try:
        contas = conta_service.listar_numeros_contas()
        return contas
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/banco/conta/{numero}/saldo")
def consultar_saldo(numero: str) -> dict[str, Decimal]:
    try:
        conta = conta_service.consultar_conta(numero)
        return {"saldo": conta._saldo}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/banco/conta/{numero}/credito")
def credito(numero: str, dados: SacarDepositarDTO) -> dict[str, str]:
    try:
        conta_service.depositar(numero, dados)
        return {"message": "Crédito realizado com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/banco/conta/{numero}/debito")
def debito(numero: str, dados: SacarDepositarDTO) -> dict[str, str]:
    try:
        conta_service.sacar(numero, dados)
        return {"message": "Débito realizado com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/banco/transferencia")
def transferencia(dados: TransferirDTO) -> dict[str, str]:
    try:
        conta_service.transferir(dados)
        return {"message": "Transferência realizada com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/banco/conta/{numero}/rendimento")
def render_juros(numero: str, dados: RenderJurosDTO) -> dict[str, str]:
    try:
        conta_service.render_juros(numero, dados)
        return {"message": "Rendimento aplicado com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
