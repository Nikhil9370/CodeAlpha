# 1. Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 135
}

# 2. To store user stock entries
portfolio = {}
total_investment = 0

print("Welcome to the Stock Tracker!\n")
print("Available stocks:", ", ".join(stock_prices.keys()))

# 3. User input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Invalid number. Try again.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity
    print(f"Added {quantity} of {stock} at ${stock_prices[stock]} each.\n")

# 4. Show final report
print("\n--- Investment Summary ---")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# 5. Optional: Save to file
save = input("\nDo you want to save the summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("--- Investment Summary ---\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Summary saved to 'investment_summary.txt'")
