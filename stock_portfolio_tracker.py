# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker
# Note: The stock prices below are sample prices, not live market prices.

stock_prices = {
    "TCS": 4000,
    "INFOSYS": 1500,
    "WIPRO": 500,
    "RELIANCE": 2500,
    "HCL": 1600,
    "AAPL": 180,
    "TSLA": 250
}

portfolio = []
total_investment = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks and Sample Prices:")
for stock, price in stock_prices.items():
    print(f"{stock} - Rs. {price}")

while True:
    stock_name = input("\nEnter stock name (or DONE to finish): ").strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose a stock from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })
    total_investment += investment

    print("Stock added successfully!")
    print(f"Investment for {stock_name} = Rs. {investment}")

print("\n" + "=" * 40)
print("       PORTFOLIO SUMMARY")
print("=" * 40)

if not portfolio:
    print("No stocks were added.")
else:
    for item in portfolio:
        print(f"\nStock: {item['stock']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Price per stock: Rs. {item['price']}")
        print(f"Investment: Rs. {item['investment']}")

    print("\n" + "-" * 40)
    print(f"TOTAL INVESTMENT: Rs. {total_investment}")
    print("-" * 40)

    try:
        with open("stock_portfolio_report.txt", "w", encoding="utf-8") as report:
            report.write("STOCK PORTFOLIO TRACKER REPORT\n")
            report.write("=" * 35 + "\n\n")
            report.write("Note: Sample prices for the CodeAlpha Task 2 demo; not live market prices.\n\n")
            for item in portfolio:
                report.write(f"Stock: {item['stock']}\n")
                report.write(f"Quantity: {item['quantity']}\n")
                report.write(f"Price per stock: Rs. {item['price']}\n")
                report.write(f"Investment: Rs. {item['investment']}\n\n")
            report.write(f"TOTAL INVESTMENT: Rs. {total_investment}\n")
        print("\nReport saved as stock_portfolio_report.txt")
    except OSError:
        print("\nUnable to save the report.")

print("\nThank you for using Stock Portfolio Tracker!")
