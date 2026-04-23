from api.stock_api import get_current_stock_price, get_stock_history
from models.portfolio import get_portfolio, update_portfolio, initialize_portfolio


# run portfolio check
initialize_portfolio()

# testing portfolio
print(get_portfolio())
into_portfolio = {"test": 2}
update_portfolio(into_portfolio, "portfolio")
print(get_portfolio())

# getting user info about which stock, interval and start/end date
company_stock_suffix = input("What stock do you want to look at? ")
what_data = input("Do you want historical data? (y/n) ")
if what_data.lower() == "y" or what_data.lower() == "yes":
    stock_interval = input(
        "In what interval do you want your stocks? (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo) "
    )
    stock_start = input("When should the data start? (yyyy-mm-dd) ")
    stock_end = input("When should the data end? (yyyy-mm-dd) ")

    # getting stock history
    print(get_stock_history(company_stock_suffix, stock_interval, stock_start, stock_end))

# getting current stock price
print(f"Current price: {get_current_stock_price(company_stock_suffix)}")
