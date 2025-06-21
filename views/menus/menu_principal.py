from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from views.forms.acessar_conta import AcessarConta

from views.forms.cadastrar_conta import CadastrarConta


class MenuPrincipal(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Conta", classes="titulo"),
            Button("Acessar conta", id="acessar"),
            Button("Cadastrar conta", id="cadastrar"),
            Button("Sair", id="sair", classes="voltar"),
            id="menu",
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "acessar":
                self.app.push_screen(AcessarConta())
            case "cadastrar":
                self.app.push_screen(CadastrarConta())
            case "sair":
                self.app.exit()
