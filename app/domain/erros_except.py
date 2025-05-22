
class SaldoError(Exception):
    def __init__(self, mensagem="Erro: Saldo insuficiente para efetuar a operação."):
        super().__init__(mensagem)