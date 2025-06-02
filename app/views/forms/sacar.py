from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Static

from app.views.componentes.input_dinheiro import DinheiroInput


class TelaSacar(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Saque", classes="titulo"),
            Static("Digite o valor a ser sacado:", id="instrucoes"),
            DinheiroInput(placeholder="Valor", id="valor"),
            Button("Confirmar", id="confirmar"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="form_sacar",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.set_focus(self.query_one("#valor"))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "confirmar":
                valor = self.query_one("#valor", Input).value
                print(f"Saque: R$ {valor}")
            case "voltar":
                self.app.pop_screen()
