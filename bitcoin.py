import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_KEY")
    r.raise_for_status()
except requests.RequestException:
    sys.exit("Request failed")

price = float(r.json()["data"]["priceUsd"])
print(f"${price * amount:,.4f}")