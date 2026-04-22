from api.stock_api import get_current_stock_price, get_stock_history

company_stock_suffix = input("What stock do you want to look at? ")
stock_interval = input("In what interval do you want your stocks? ")
stock_start = input("When should the data start? ")
stock_end = input("When should the data end? ")

print(get_stock_history(company_stock_suffix, stock_interval, stock_start, stock_end))


print(get_current_stock_price("aapl"))
