from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Button, Static, Input
from textual.containers import Vertical, Horizontal
from textual.events import Ready

class TelaDepositar(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("[b green]Depósito[/b green]"),
            Static("Digite o valor a ser depositado:"),
            Input(placeholder="Valor", id="valor"),
            Button("Confirmar", id="confirmar"),
            Button("Voltar", id="voltar", classes="voltar"),
        )
        yield Footer()

    async def on_ready(self, event: Ready) -> None:
        await self.set_focus(self.query_one("#valor"))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirmar":
            valor = self.query_one("#valor", Input).value
            print(f"Depósito: R$ {valor}")
        elif event.button.id == "voltar":
            self.app.pop_screen()
