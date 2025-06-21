from textual.app import App

from views.menus.menu_principal import MenuPrincipal


class MenuApp(App):
    TITLE = "BANCORN"
    BINDINGS = [("escape", "voltar", "Voltar")]
    CSS_PATH = "style.tcss"

    def on_mount(self) -> None:
        self.push_screen(MenuPrincipal())

    def action_voltar(self) -> None:
        if len(self.screen_stack) > 2:
            self.pop_screen()


if __name__ == "__main__":
    MenuApp().run()
