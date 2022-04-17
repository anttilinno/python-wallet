import yaml
import requests
from json.decoder import JSONDecodeError

try:
    with open("wallet.yaml") as f:
        my_dict = yaml.safe_load(f)
except FileNotFoundError:
    exit("File not found!")

url = "https://api.coingecko.com/api/v3/simple/price"

wallet_current_state = []
total_current_value = 0

for coin in my_dict["coins"]:
    try:
        price_dict = requests.get(
            url,
            params={
                "ids": coin["id"],
                "vs_currencies": "eur"}).json()
        token_price = price_dict[coin["id"]]["eur"]

        wallet_current_state.append({
            "id": coin["id"],
            "symbol": coin["symbol"],
            "name": coin["name"],
            "amount": coin["amount"],
            "price": token_price,
            "value": token_price * coin["amount"]
        })

        total_current_value += token_price * coin["amount"]
    except JSONDecodeError as e:
        exit("Request did not produce JSON response!")
    except TypeError as e:
        exit("JSON object is not a str, bytes, or bytearray")

print(total_current_value)
print(wallet_current_state)
