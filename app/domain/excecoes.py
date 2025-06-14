class ContaJaExiste(Exception):
    def __init__(self, mensagem: str = "Conta já existe") -> None:
        super().__init__(mensagem)


class ContaNaoEncontrada(Exception):
    def __init__(self, mensagem: str = "Conta não encontrada") -> None:
        super().__init__(mensagem)


class SaldoInsuficiente(Exception):
    def __init__(self, mensagem: str = "Saldo insuficiente para efetuar a operação.") -> None:
        super().__init__(mensagem)


class ValorOperacaoInvalido(Exception):
    def __init__(self, mensagem: str = "Valor inválido para efetuar a operação.") -> None:
        super().__init__(mensagem)


class SaldoInicialInvalido(Exception):
    def __init__(self, mensagem: str = "O valor informado para o saldo inicial não é permitido.") -> None:
        super().__init__(mensagem)