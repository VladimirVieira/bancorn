from decimal import Decimal

from textual import events
from textual.reactive import reactive
from textual.widgets import Input


class DinheiroInput(Input):
    cents = reactive(0)

    def on_mount(self):
        self.can_focus = True
        self.focus()
        self.value = "R$ 0,00"

    def watch_cents(self, cents):
        reais = cents // 100
        centavos = cents % 100
        self.value = f"R$ {reais},{centavos:02d}"

    async def on_key(self, event: events.Key):
        k = event.key
        if k.isdigit():
            event.prevent_default()
            event.stop()
            self.cents = self.cents * 10 + int(k)
        elif k == "backspace":
            event.prevent_default()
            event.stop()
            self.cents = self.cents // 10
        elif len(k) == 1 and k.isprintable():
            event.prevent_default()
            event.stop()

    def get_value(self):
        return Decimal(self.cents) / Decimal(100)
