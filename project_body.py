import requests
import os
from dotenv import load_dotenv

load_dotenv("project.env")

API_KEY = os.getenv("EXCHANGE_RATE_API")

def exchange_currency():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"]


def exchange_rate_tool():
    print("Exchange rate tool")
    print("USD > ....")
    amount = float(input("Enter the amount: "))
   
    currency_u_have = input("Enter the currency you have: ").upper().strip()
    currency_u_want = input("Enter the currency you want: ").upper().strip()

    if not currency_u_have or not currency_u_want:
        print("Incorrect currency. Check again and enter the correct currency")
        return

    print("Fetching currency wait....")

    rates = exchange_currency()

    if currency_u_have not in rates or currency_u_want not in rates:
        print("One or both currencies are not supported.")
        return

    amount_in_usd = amount / rates[currency_u_have]
    final_amount = amount_in_usd * rates[currency_u_want]

    print(f"\n{amount} {currency_u_have} = {final_amount:.2f} {currency_u_want}")


# Call the function
exchange_rate_tool()