from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input


class PruebaTextual(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Introduce los coeficientes del numerador:")
        yield Input(placeholder="Ejemplo: 1, 3", id="numerador")
        yield Static("", id="resultado")
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        texto = event.value
        resultado = self.query_one("#resultado", Static)
        resultado.update(f"Has escrito: {texto}")


if __name__ == "__main__":
    PruebaTextual().run()


