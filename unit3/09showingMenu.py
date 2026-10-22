while(True):
    print("1.Balance 2.Withdraw 3.Deposit 4.Exit")
    choice=input("Enter your choice")
    if choice not in ["1", "2", "3","4"]:
        print("Invalid Choice")
        continue
    if choice=="4":
        print("GoodBye!")
        break
    elif choice=="1":
        print("balance: 5000")
    elif choice=="2":
        print("Money withdrawl")
    elif choice=="3":
        print("Money deposited")