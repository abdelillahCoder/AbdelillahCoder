# Enhanced currency converter with Bitcoin (BTC)
print("Welcome to the currency converter! 💱")

# Predefined exchange rates (example fictitious, adjust as needed)
exchange_rates = {
    "EUR": {"USD": 1.1, "MAD": 11.0, "GBP": 0.85, "CAD": 1.5, "AUD": 1.6, "JPY": 145.0, "CHF": 0.98, "CNY": 7.3, "INR": 90.0, "BRL": 5.6, "ZAR": 19.0, "BYN": 2.6, "BTC": 0.000027},
    "USD": {"EUR": 0.91, "MAD": 10.0, "GBP": 0.77, "CAD": 1.36, "AUD": 1.45, "JPY": 132.0, "CHF": 0.89, "CNY": 6.7, "INR": 82.0, "BRL": 5.1, "ZAR": 17.0, "BYN": 2.3, "BTC": 0.000024},
    "MAD": {"EUR": 0.091, "USD": 0.10, "GBP": 0.077, "CAD": 0.14, "AUD": 0.15, "JPY": 13.2, "CHF": 0.089, "CNY": 0.67, "INR": 8.2, "BRL": 0.51, "ZAR": 1.7, "BYN": 0.23, "BTC": 0.000009},
    "GBP": {"EUR": 1.18, "USD": 1.3, "MAD": 13.0, "CAD": 1.76, "AUD": 1.9, "JPY": 154.0, "CHF": 1.14, "CNY": 8.3, "INR": 95.0, "BRL": 6.0, "ZAR": 20.0, "BYN": 3.0, "BTC": 0.000023},
    "CAD": {"EUR": 0.67, "USD": 0.73, "MAD": 7.5, "GBP": 0.57, "AUD": 1.08, "JPY": 111.0, "CHF": 0.66, "CNY": 4.9, "INR": 60.0, "BRL": 3.8, "ZAR": 14.0, "BYN": 1.8, "BTC": 0.000016},
    "AUD": {"EUR": 0.63, "USD": 0.69, "MAD": 7.0, "GBP": 0.53, "CAD": 0.93, "JPY": 104.0, "CHF": 0.61, "CNY": 4.6, "INR": 57.0, "BRL": 3.6, "ZAR": 13.2, "BYN": 1.7, "BTC": 0.000015},
    "JPY": {"EUR": 0.0069, "USD": 0.0076, "MAD": 0.075, "GBP": 0.0065, "CAD": 0.0090, "AUD": 0.0096, "CHF": 0.0059, "CNY": 0.045, "INR": 0.53, "BRL": 0.037, "ZAR": 0.12, "BYN": 0.018, "BTC": 0.0000007},
    "CHF": {"EUR": 1.02, "USD": 1.12, "MAD": 11.2, "GBP": 0.88, "CAD": 1.52, "AUD": 1.64, "JPY": 147.0, "CNY": 7.4, "INR": 91.0, "BRL": 5.7, "ZAR": 19.0, "BYN": 2.8, "BTC": 0.000025},
    "CNY": {"EUR": 0.14, "USD": 0.15, "MAD": 1.5, "GBP": 0.12, "CAD": 0.2, "AUD": 0.22, "JPY": 20.0, "CHF": 0.14, "INR": 12.0, "BRL": 0.8, "ZAR": 2.3, "BYN": 0.35, "BTC": 0.00014},
    "INR": {"EUR": 0.011, "USD": 0.012, "MAD": 0.12, "GBP": 0.010, "CAD": 0.017, "AUD": 0.018, "JPY": 1.88, "CHF": 0.011, "CNY": 0.083, "BRL": 0.059, "ZAR": 0.21, "BYN": 0.027, "BTC": 0.00000012},
    "BRL": {"EUR": 0.18, "USD": 0.20, "MAD": 1.8, "GBP": 0.17, "CAD": 0.26, "AUD": 0.28, "JPY": 26.0, "CHF": 0.18, "CNY": 1.3, "INR": 17.0, "ZAR": 3.8, "BYN": 0.52, "BTC": 0.000021},
    "ZAR": {"EUR": 0.053, "USD": 0.059, "MAD": 0.53, "GBP": 0.050, "CAD": 0.071, "AUD": 0.076, "JPY": 7.9, "CHF": 0.053, "CNY": 0.38, "INR": 4.6, "BRL": 0.26, "BYN": 0.071, "BTC": 0.0000038},
    "BYN": {"EUR": 0.38, "USD": 0.44, "MAD": 4.4, "GBP": 0.33, "CAD": 0.56, "AUD": 0.59, "JPY": 55.0, "CHF": 0.36, "CNY": 2.8, "INR": 37.0, "BRL": 1.9, "ZAR": 14.0, "BTC": 0.00018},
    "BTC": {"EUR": 37000, "USD": 40000, "MAD": 440000, "GBP": 34000, "CAD": 56000, "AUD": 60000, "JPY": 5400000, "CHF": 41000, "CNY": 310000, "INR": 3700000, "BRL": 200000, "ZAR": 800000, "BYN": 5550},
}

# Available currencies
print("Available currencies: EUR, USD, MAD, GBP, CAD, AUD, JPY, CHF, CNY, INR, BRL, ZAR, BYN, BTC")
source_currency = input("Enter the source currency: ").upper()
target_currency = input("Enter the target currency: ").upper()

# Check if the conversion is available
if source_currency in exchange_rates and target_currency in exchange_rates[source_currency]:
    amount = float(input(f"Enter the amount in {source_currency}: "))
    rate = exchange_rates[source_currency][target_currency]
    converted_amount = amount * rate
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")
else:
    print("Conversion not available between these currencies.")
