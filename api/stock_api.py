import yfinance as yf


def get_current_stock_price(symbol):
    stock = yf.Ticker(symbol)
    try:
        return stock.get_fast_info().last_price
    except AttributeError:
        return "No data available"


def get_stock_history(symbol, interval, start_date, end_date):
    stock = yf.Ticker(symbol)
    history = stock.history(interval=interval, start=start_date, end=end_date)
    return history
