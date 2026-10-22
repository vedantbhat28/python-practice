from datetime import datetime
balance=5000
amount=2000
if(amount>0 and amount<=balance):
    balance-=amount
    stamp=datetime.now().strftime("%D %M %Y %H %M")
    print(f"Reciept time: {stamp}")
else:
    print("invalid amount")