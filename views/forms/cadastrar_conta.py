from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Select, Static

from views.componentes.input_dinheiro import DinheiroInput

class CadastrarConta(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Formulário de Conta", classes="titulo"),
            Select(
                options=[
                    ("Conta Normal", "normal"),
                    ("Conta Poupança", "poupanca"),
                    ("Conta Bônus", "bonus"),
                ],
                prompt="Tipo de conta",
                id="tipo_conta",
            ),
            Input(placeholder="Número da conta", id="numero_conta"),
            Static("Valor inicial", id="valor_inicial_label"),
            DinheiroInput(placeholder="Valor inicial", id="valor_inicial"),
            Button("Cadastrar", id="cadastrar"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="form",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#valor_inicial").display = False
        self.query_one("#valor_inicial_label").display = False

    def on_select_changed(self, event: Select.Changed) -> None:
        self.query_one("#valor_inicial").display = event.value == "poupanca"
        self.query_one("#valor_inicial_label").display = event.value == "poupanca"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "cadastrar":
                tipo = self.query_one("#tipo_conta", Select).value
                numero = self.query_one("#numero_conta", Input).value
                valor_inicial = self.query_one("#valor_inicial", Input).value
                print(f"Conta cadastrada: Tipo={tipo}, Número={numero}, Valor inicial={valor_inicial}")
            case "voltar":
                self.app.pop_screen()
