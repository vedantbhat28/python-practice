balance=5000
amount=None
print("1.Balance\n2.Withdraw Amount\n3.Deposit Amount\n4.STOP")
cmd=int(input())
if(cmd==1):
    print(f"Your balance is: {balance}")
elif(cmd==2):
    amount=int(input("Enter amount to be withdrawn: "))
    if(amount>0 and amount<=balance):
        balance-=amount
        print(f"Amount withdrawn. New balance: 2{balance}")
    elif(amount<0):
        print(f"Invalid amount.")
    else:
        print("Insuffient balance.")
elif(cmd==3):
    amount=int(input("Enter amount to be deposited:"))
    if(amount>0):
        balance+=amount
        print(f"Amount deposited. New balance: {balance}")
    else:
        print("Invalid amount")
elif(cmd==4):
    print("GoodBye!")    
else:
    print("Invalid choice")
    