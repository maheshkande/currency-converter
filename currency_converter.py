import requests

API_KEY = "6644fcb3d2e560c327e9a726"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

def convert_currency(from_currency, to_currency, amount):
    url = f"{BASE_URL}/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data["result"] == "success":
        converted_amount = data["conversion_result"]
        print(f"\n💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("\n❌ Conversion failed. Please check the currency codes and try again.")

# ----- Run the App -----
print("💰 Currency Converter")

try:
    from_curr = input("From currency (e.g., INR): ").upper()
    to_curr = input("To currency (e.g., USD): ").upper()
    amount = float(input("Amount to convert: "))

    convert_currency(from_curr, to_curr, amount)

except ValueError:
    print("❌ Please enter a valid number for amount.")

