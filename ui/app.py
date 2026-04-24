from textual.app import App, ComposeResult
from textual.widgets import Static, Button, DataTable
from textual.containers import Grid, Container

from models.portfolio import initialize_portfolio, get_portfolio


ROWS = [
    ("aapl", "Apple", 10054),
    ("ifx.de", "Infineon", 52),
    ("nvda", "Nvidia", 130),
    ("goog", "Google", 150),
    ("meta", "Meta", 20),
]


class mainLayout(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        with Grid():
            yield DataTable()
            yield Static("Test")
            yield Static("Getting market details...")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.add_columns("Symbol", "Name", "current price")
        table.add_rows(ROWS[0:])
        print(get_portfolio())


if __name__ == "__main__":
    app = mainLayout()
    app.run()
