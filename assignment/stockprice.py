class StockMarket:

    def __init__(self, name):
        self.name = name
        self.stocks = []
        self.traders = []
        self.transactions = []

    def addStocks(self, stock_list):
        self.stocks.extend(stock_list)
        print("Stocks are added to the Market")

    def addTraders(self, trader_list):
        self.traders.extend(trader_list)
        print("Traders are added to the Market")

    def recordTransaction(self, transaction):
        self.transactions.append(transaction)

    def generateReport(self):
        market_cap = sum(s.price * s.available_quantity for s in self.stocks)
        print("=========== Market Report ===========")
        print(f"Market Name: {self.name}")
        print(f"Total Stocks: {len(self.stocks)}")
        print(f"Total Traders: {len(self.traders)}")
        print(f"Total Transactions: {len(self.transactions)}")
        print(f"Market Capitalization: {market_cap}")
        print("=====================================")


class Stock:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.available_quantity = quantity
        self.history = [(price, "Initial Price")]
        self.average_price = price

    def updatePrice(self, new_price, reason="Market Update"):
        self.history.append((new_price, reason))
        self.price = new_price
        self.average_price = sum(p for p, _ in self.history) / len(self.history)
        print(f"Stock {self.name} price updated to {new_price}")

    def getHistory(self):
        print(f"Price history of {self.name}: {self.history}")


class Trader:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.portfolio = {}  # {stock_name: quantity}
        self.history = []    # (BUY/SELL, stock, qty, price)

    def buyStock(self, stock, qty, market):
        if stock.available_quantity >= qty:
            stock.available_quantity -= qty
            self.portfolio[stock.name] = self.portfolio.get(stock.name, 0) + qty
            transaction = (self.name, "BUY", stock.name, qty, stock.price)
            self.history.append(transaction)
            market.recordTransaction(transaction)
            print(f"{self.name} bought {qty} shares of {stock.name} at {stock.price}")
        else:
            print("Not enough stock available!")

    def sellStock(self, stock, qty, market):
        if self.portfolio.get(stock.name, 0) >= qty:
            self.portfolio[stock.name] -= qty
            stock.available_quantity += qty
            transaction = (self.name, "SELL", stock.name, qty, stock.price)
            self.history.append(transaction)
            market.recordTransaction(transaction)
            print(f"{self.name} sold {qty} shares of {stock.name} at {stock.price}")
        else:
            print("Not enough shares to sell!")

    def getPortfolio(self):
        print(f"Portfolio of {self.name}: {self.portfolio}")

    def getHistory(self):
        print(f"Transaction history of {self.name}: {self.history}")


# =============================
# Example Usage (like cab code)
# =============================
m1 = StockMarket("National Stock Exchange")

# Create Stocks
s1 = Stock("TCS", 3500, 1000)
s2 = Stock("Infosys", 1600, 2000)

# Create Traders
t1 = Trader(1, "Alice")
t2 = Trader(2, "Bob")

# Add to Market
m1.addStocks([s1, s2])
m1.addTraders([t1, t2])

# Update Stock Prices
s1.updatePrice(3600, "Quarterly Results")
s2.updatePrice(1550, "Market Dip")

# Buy and Sell
t1.buyStock(s1, 10, m1)
t1.buyStock(s2, 20, m1)
t2.buyStock(s2, 30, m1)
t1.sellStock(s2, 5, m1)

# Check Portfolio and History
t1.getPortfolio()
t1.getHistory()

# Stock History
s1.getHistory()

# Market Report
m1.generateReport()
