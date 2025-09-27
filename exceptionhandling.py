remaining_balance=20
def withdrawl_(x):
    if x < 0:
        raisevalueerror("input can't be negative")
    else:
        print("balance is:",remaining_balance)
print(withdrawl_(2))      