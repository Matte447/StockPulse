import asyncio
from textual.app import App, ComposeResult
from textual.widgets import Static, DataTable
from textual.containers import Grid
from textual.worker import Worker

from models.portfolio import get_portfolio
from api.stock_api import get_current_stock_price


rows = []

for stock in get_portfolio()["portfolio"]:
    rows.append(
        (stock["stock"], stock["name"], stock["buy-price"], stock["current-price"])
    )
    print(stock)
print(rows)


async def update_current_price(symbol):
    price = get_current_stock_price(symbol)
    return price


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
        table.add_columns(
            ("Symbol", "symbol_col"),
            ("Name", "name_col"),
            ("buy price", "buy_col"),
            ("current price", "cur_col"),
        )
        for row in rows[0:]:
            table.add_row(*row, key=row[0])
        print(get_portfolio())

        self.run_worker(self.update_prices())

    async def update_prices(self):
        table = self.query_one(DataTable)
        for stock in rows:
            price = await update_current_price(stock[0])
            table.update_cell(stock[0], "cur_col", price)


if __name__ == "__main__":
    app = mainLayout()
    app.run()
