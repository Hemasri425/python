class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def addCustomers(self, customers_list):
        self.customers.extend(customers_list)
        print('Customers have been added to the Bank')

    def addAccounts(self, accounts_list):
        self.accounts.extend(accounts_list)
        print('Accounts have been added to the Bank')

    def getInfo(self):
        print("=== Bank Customers ===")
        print([customer.name for customer in self.customers])
        print("--------------------------")
        print("=== Bank Accounts ===")
        print([account.account_number for account in self.accounts])
        print("--------------------------")


class Customer:
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name
        self.accounts = []  # A customer can have multiple accounts

    def openAccount(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} opened for {self.name}")

    def getAccounts(self):
        print(f"\nAccounts for {self.name}:")
        for acc in self.accounts:
            print(f"Account Number: {acc.account_number} | Balance: {acc.balance}")


class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner  # Customer object
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transaction_history.append(("Deposit", amount))
        print(f"Deposited {amount} to Account {self.account_number}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        self.transaction_history.append(("Withdraw", amount))
        print(f"Withdrew {amount} from Account {self.account_number}. New Balance: {self.balance}")

    def getBalance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")
        return self.balance

    def getTransactionHistory(self):
        print(f"\nTransaction History for Account {self.account_number}:")
        for txn in self.transaction_history:
            print(f"{txn[0]} of {txn[1]}")
        print("--------------------------")

bank = Bank()
c1 = Customer(1, "Hemasri")
c2 = Customer(2, "Ramyasri")
a1 = Account("A1001", c1, balance=5000)
a2 = Account("A1002", c2, balance=2000)
a3 = Account("A1003", c1, balance=10000) 
c1.openAccount(a1)
c1.openAccount(a3)
c2.openAccount(a2)
bank.addCustomers([c1, c2])
bank.addAccounts([a1, a2, a3])
bank.getInfo()
a1.deposit(1500)
a1.withdraw(3000)
a1.withdraw(5000) 
a1.getBalance()
a1.getTransactionHistory()
c1.getAccounts()
c2.getAccounts()


