from textual.app import App

from .menu_principal import MenuPrincipal


class MenuApp(App):
    TITLE = "BANCORN"
    BINDINGS = [("escape", "voltar", "Voltar")]

    CSS = """
    Screen {
        align: center middle;
    }
    #menu, #form {
        align: center middle;
        width: 40;
    }
    Button {
        width: 100%;
        border: round cyan;
        content-align: center middle;
    }

    .voltar {
        border: round red;
    }

    Input, Select {
        width: 100%;
        border: round green;
    }
    """

    def on_mount(self) -> None:
        self.push_screen(MenuPrincipal())

    def action_voltar(self) -> None:
        if len(self.screen_stack) > 2:
            self.pop_screen()


if __name__ == "__main__":
    MenuApp().run()
