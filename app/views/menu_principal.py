from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from app.views.acessar_conta import AcessarConta

from .formulario_conta import FormularioConta


class MenuPrincipal(Screen):
    CSS = """
    #menu {
        align: center middle;
        width: 40;
    }

    #title {
        content-align: center middle;
        height: auto;
        margin-bottom: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("[b green]BANCORN[/b green]", id="title"),
            Button("Acessar conta", id="acessar"),
            Button("Cadastrar conta", id="cadastrar"),
            Button("[b]Sair[/b]", id="sair", classes="voltar"),
            id="menu",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "acessar":
                self.app.push_screen(AcessarConta())
            case "cadastrar":
                self.app.push_screen(FormularioConta())
            case "sair":
                self.app.exit()
