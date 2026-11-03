import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=220e0ca73331062611ba34fad3d12bb33440995a436b4acce3ad48289281f316")
    r.raise_for_status()
except requests.RequestException as e:
    sys.exit(f"Request failed: {e}")

price = float(r.json()["data"]["priceUsd"])
print(f"${price * amount:,.4f}")