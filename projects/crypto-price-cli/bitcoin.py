import sys
import requests


def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # CoinCap v3 API endpoint
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
    "Authorization": "Bearer de00860979f3fc6a80c4720326877e8dad2e7a38944eec508a556b052d5af21f"
}


    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Error fetching Bitcoin price")

    total_cost = bitcoins * price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
