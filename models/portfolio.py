import json


def initialize_portfolio():
    try:
        with open("./models/portfolio.json", "r") as f:
            f.read()
    except FileNotFoundError:
        open("./models/portfolio.json", "x")
        normal_json_file = {"portfolio": []}
        with open("./models/portfolio.json", "w") as f:
            f.write(json.dumps(normal_json_file))


def get_portfolio():
    with open("./models/portfolio.json", "r") as f:
        current_portfolio = json.load(f)
    return current_portfolio


def update_portfolio(stock: str, name: str, quantity: int, buy_price: int) -> None:
    content = {}
    with open("./models/portfolio.json", "r") as f:
        current_portfolio = json.load(f)

    for current_stock in current_portfolio["portfolio"]:
        if current_stock["stock"] == stock:
            current_stock["quantity"] += quantity
            content = {}
            break
        else:
            content = {
                "stock": stock,
                "name": name,
                "quantity": quantity,
                "buy-price": buy_price,
                "current-price": "Awaiting prize...",
            }
    if content != {}:
        current_portfolio["portfolio"].append(content)

    with open("./models/portfolio.json", "w") as f:
        f.write(json.dumps(current_portfolio, indent=4))

    return
