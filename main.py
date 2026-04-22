import yfinance as yf

company_stock_suffix = input("What stock do you want to look at? ")
stock = yf.Ticker(company_stock_suffix)
stock_interval = input("In what interval do you want your stocks? ")
stock_start = input("When should the data start? ")
stock_end = input("When should the data end? ")

print(stock.history(interval=stock_interval, start=stock_start, end=stock_end))
