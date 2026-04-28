import asyncio
from textual.app import App, ComposeResult
from textual.coordinate import Coordinate
from textual.widgets import Static, DataTable, Log
from textual.containers import Grid
from textual.screen import Screen

from models.portfolio import get_portfolio, initialize_portfolio
from api.stock_api import get_current_stock_price


initialize_portfolio()


async def update_current_price(symbol):
    price = get_current_stock_price(symbol)
    return price


class Dashboard(Screen):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        with Grid():
            yield DataTable()
            yield Static("Test")
            yield Log(id="console")

    def on_mount(self) -> None:
        self.refresh_portfolio()
        log = self.query_one(Log)
        log.write_line("Waiting for market data...")
        log.can_focus = False
        log.border_title = "Console"
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.add_columns(
            ("Symbol", "symbol_col"),
            ("Name", "name_col"),
            ("Quantity", "quan_col"),
            ("buy price", "buy_col"),
            ("current price", "cur_col"),
        )
        for row in self.rows[0:]:
            table.add_row(*row, key=row[0])
        self.run_worker(self.update_prices())

    async def update_prices(self):
        table = self.query_one(DataTable)
        for stock in self.rows:
            price = await update_current_price(stock[0])
            table.update_cell(stock[0], "cur_col", price)
        self.query_one(Log).write_line("Got market details!")

    def on_key(self, event) -> None:
        table = self.query_one(DataTable)
        log = self.query_one(Log)
        if event.key == "enter":
            log.write_line(
                f"{table.get_cell_at(Coordinate(table.cursor_row, 0))} was selected"
            )

    def refresh_portfolio(self) -> None:
        self.rows = []

        for stock in get_portfolio()["portfolio"]:
            self.rows.append(
                (
                    stock["stock"],
                    stock["name"],
                    stock["quantity"],
                    stock["buy-price"],
                    stock["current-price"],
                )
            )


class StockApp(App):
    SCREENS = {"dashboard": Dashboard}

    def on_mount(self) -> None:
        self.install_screen(Dashboard(), "Dashboard")
        self.push_screen("dashboard")


if __name__ == "__main__":
    app = StockApp()
    app.run()
