from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from .depositar import TelaDepositar
from .sacar import TelaSacar
from .transferir import TelaTransferir


class TelaConta(Screen):
    CSS = """
    #painel_conta {
        align: center middle;
        width: 40;
    }

    #titulo_conta {
        content-align: center middle;
        margin-bottom: 1;
    }

    #saldo {
        content-align: center middle;
        margin-bottom: 2;
    }

    Button {
        width: 100%;
        border: round cyan;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("[b green]Conta 1234[/b green]", id="titulo_conta"),
            Static("[b]Saldo:[/b] R$ 1.500,75", id="saldo"),
            Button("Depositar", id="depositar"),
            Button("Sacar", id="sacar"),
            Button("Transferir", id="transferir"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="painel_conta",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "depositar":
                self.app.push_screen(TelaDepositar())
            case "sacar":
                self.app.push_screen(TelaSacar())
            case "transferir":
                self.app.push_screen(TelaTransferir())
            case "voltar":
                self.app.pop_screen()
