transactions=["Deposit 500", "Withdraw 100", "Balance"]
target=input("Search Transaction: ")
for i in transactions:
    if i==target:
        print(f"Transaction found{i}")
    break