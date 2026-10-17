
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input


class PruebaTextual(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Introduce los componentes del mumerador")
        yield Input(placeholder="Ejemplo: 1 ,3 ")
        yield Footer()


if __name__ == "__main__":
    PruebaTextual().run()

