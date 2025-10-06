prices=[100,105,98,110,120]
total=0
for p in prices:
    total+=p
    average=total/len(prices)
print("Average stock price:",average)