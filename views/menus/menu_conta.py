from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from views.forms.depositar import TelaDepositar
from views.forms.sacar import TelaSacar
from views.forms.transferir import TelaTransferir


class MenuConta(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Conta 123456-78", classes="titulo"),
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
