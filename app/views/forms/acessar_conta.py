from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Static

from app.views.menus.menu_conta import MenuConta


class AcessarConta(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Acessar Conta", classes="titulo"),
            Static("Digite o número da conta:", id="instrucoes"),
            Input(placeholder="Número da conta", id="numero_conta"),
            Button("Entrar", id="entrar"),
            Button("Voltar", id="voltar", classes="voltar"),
            id="form_acesso",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "entrar":
                numero = self.query_one("#numero_conta", Input).value
                self.app.push_screen(MenuConta())
            case "voltar":
                self.app.pop_screen()
