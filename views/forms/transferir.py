from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Static

from views.componentes.input_dinheiro import DinheiroInput


class TelaTransferir(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Transferência", classes="titulo"),
            Static("Digite o número da conta destino:", id="instr_conta"),
            Input(placeholder="Número da conta", id="conta_destino"),
            Static("Digite o valor a ser transferido:", id="instr_valor"),
            DinheiroInput(placeholder="Valor", id="valor"),
            Button("Confirmar", id="confirmar"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="form_transferir",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.set_focus(self.query_one("#valor"))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "confirmar":
                conta = self.query_one("#conta_destino", Input).value
                valor = self.query_one("#valor", Input).value
                print(f"Transferência para {conta}: R$ {valor}")
            case "voltar":
                self.app.pop_screen()
