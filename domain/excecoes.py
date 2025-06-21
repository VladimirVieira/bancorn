class ContaJaExisteError(Exception):
    def __init__(self, mensagem: str = "Conta já existe") -> None:
        super().__init__(mensagem)


class ContaNaoEncontradaError(Exception):
    def __init__(self, mensagem: str = "Conta não encontrada") -> None:
        super().__init__(mensagem)


class SaldoInsuficienteError(Exception):
    def __init__(
        self, mensagem: str = "Saldo insuficiente para efetuar a operação.",
    ) -> None:
        super().__init__(mensagem)


class ValorOperacaoInvalidoError(Exception):
    def __init__(
        self, mensagem: str = "Valor inválido para efetuar a operação.",
    ) -> None:
        super().__init__(mensagem)


class SaldoInicialInvalidoError(Exception):
    def __init__(
        self, mensagem: str = "O valor informado para o saldo inicial não é permitido.",
    ) -> None:
        super().__init__(mensagem)
