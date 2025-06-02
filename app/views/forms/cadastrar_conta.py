from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Select, Static


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
            Button("Cadastrar", id="cadastrar"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="form",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "cadastrar":
                tipo = self.query_one("#tipo_conta", Select).value
                numero= self.query_one("#numero_conta", Input).value
                print(f"Conta cadastrada: Tipo={tipo}, Nome={numero}")
            case "voltar":
                self.app.pop_screen()
