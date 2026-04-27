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


def update_portfolio(content, location):
    with open("./models/portfolio.json", "r") as f:
        current_portfolio = json.load(f)

    current_portfolio[location].append(content)

    with open("./models/portfolio.json", "w") as f:
        f.write(json.dumps(current_portfolio, indent=4))

    return
