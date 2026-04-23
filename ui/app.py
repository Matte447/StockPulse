from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Grid, Container


class mainLayout(App):
    CSS_PATH = "style.tcss"

    def compose(self):
        with Grid():
            with Container():
                yield Button("1")
                yield Button("2")
                yield Button("3")
            yield Static("Test")


if __name__ == "__main__":
    app = mainLayout()
    app.run()
