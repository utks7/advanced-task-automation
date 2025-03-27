import csv
import random
import time
import matplotlib.pyplot as plt

# File to store portfolio data
PORTFOLIO_FILE = 'portfolio.csv'

# Initialize portfolio if file doesn't exist
def init_portfolio():
    try:
        with open(PORTFOLIO_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Stock', 'Quantity', 'Buy Price', 'Current Price'])
    except FileExistsError:
        pass

# Load portfolio from CSV
def load_portfolio():
    portfolio = []
    with open(PORTFOLIO_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Quantity'] = int(row['Quantity'])
            row['Buy Price'] = float(row['Buy Price'])
            row['Current Price'] = float(row['Current Price'])
            portfolio.append(row)
    return portfolio

# Save portfolio to CSV
def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Stock', 'Quantity', 'Buy Price', 'Current Price'])
        writer.writeheader()
        writer.writerows(portfolio)

# Simulate stock price changes
def simulate_prices():
    portfolio = load_portfolio()
    for stock in portfolio:
        change = random.uniform(-5, 5)  # Random fluctuation of -5% to +5%
        stock['Current Price'] *= (1 + change / 100)
    save_portfolio(portfolio)

# Add a new stock to the portfolio
def add_stock():
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    buy_price = float(input("Enter buy price: "))
    current_price = buy_price * random.uniform(0.9, 1.1)  # Simulate slight fluctuation
    
    portfolio = load_portfolio()
    portfolio.append({
        'Stock': stock,
        'Quantity': quantity,
        'Buy Price': buy_price,
        'Current Price': current_price
    })
    save_portfolio(portfolio)
    print(f"Added {quantity} shares of {stock} at {buy_price} each.")

# Remove a stock
def remove_stock():
    stock = input("Enter stock name to remove: ").upper()
    portfolio = load_portfolio()
    portfolio = [s for s in portfolio if s['Stock'] != stock]
    save_portfolio(portfolio)
    print(f"Removed {stock} from portfolio.")

# View portfolio with profit/loss calculation
def view_portfolio():
    portfolio = load_portfolio()
    total_value = 0
    total_investment = 0
    print(f"{'Stock':<10}{'Qty':<8}{'Buy Price':<12}{'Current Price':<15}{'Profit/Loss':<12}")
    print("-" * 55)
    for stock in portfolio:
        qty = stock['Quantity']
        buy_price = stock['Buy Price']
        current_price = stock['Current Price']
        profit_loss = (current_price - buy_price) * qty
        total_value += current_price * qty
        total_investment += buy_price * qty
        print(f"{stock['Stock']:<10}{qty:<8}{buy_price:<12.2f}{current_price:<15.2f}{profit_loss:<12.2f}")
    
    print(f"\nTotal Investment: {total_investment:.2f}")
    print(f"Current Value: {total_value:.2f}")
    print(f"Net Profit/Loss: {total_value - total_investment:.2f}")

# Display portfolio graph
def plot_portfolio():
    portfolio = load_portfolio()
    if not portfolio:
        print("Portfolio is empty!")
        return
    
    stocks = [stock['Stock'] for stock in portfolio]
    values = [stock['Current Price'] * stock['Quantity'] for stock in portfolio]
    
    plt.figure(figsize=(10, 5))
    plt.bar(stocks, values, color='skyblue')
    plt.xlabel('Stocks')
    plt.ylabel('Total Value')
    plt.title('Portfolio Value by Stock')
    plt.show()

# Menu for user interaction
def main():
    init_portfolio()
    while True:
        print("\n--- STOCK PORTFOLIO TRACKER ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Simulate Price Changes")
        print("5. Display Portfolio Graph")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            simulate_prices()
            print("Stock prices simulated.")
        elif choice == '5':
            plot_portfolio()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()