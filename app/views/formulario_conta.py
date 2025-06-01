from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Select, Static


class FormularioConta(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("[b cyan]Formulário de Conta[/b cyan]", id="form_title"),
            Select(
                options=[
                    ("Conta Normal", "normal"),
                    ("Conta Poupança", "poupanca"),
                    ("Conta Bônus", "bonus"),
                ],
                prompt="Tipo de conta",
                id="tipo_conta",
            ),
            Input(placeholder="Nome da conta", id="nome_conta"),
            Button("Cadastrar", id="cadastrar_form"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="form",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "cadastrar_form":
                tipo = self.query_one("#tipo_conta", Select).value
                nome = self.query_one("#nome_conta", Input).value
                print(f"Conta cadastrada: Tipo={tipo}, Nome={nome}")
            case "voltar":
                self.app.pop_screen()
