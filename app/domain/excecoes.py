class ContaJaExiste(Exception):
    def __init__(self, mensagem: str = 'Conta já existe') -> None:
        super().__init__(mensagem)

class ContaNaoEncontrada(Exception):
    def __init__(self, mensagem: str = 'Conta não encontrada') -> None:
        super().__init__(mensagem)

class ValorTransferenciaInvalido(Exception):
    def __init__(self, mensagem: str = 'O valor da transferência deve ser maior que zero') -> None:
        super().__init__(mensagem)

class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Erro: Saldo insuficiente para efetuar a operação."):
        super().__init__(mensagem)

class ValorOperacaoInvalido(Exception):
    def __init__(self, mensagem="Erro: Valor inválido para efetuar a operação."):
        super().__init__(mensagem)
