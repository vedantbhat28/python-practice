import json
transactions=["Deposit 500", "Withdraw 100", "Balance"]
record=json.dumps(transactions, indent=2)
print(record)