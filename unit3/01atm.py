atm_pin="1234"
pin=int(input("Enter PIN: "))
if(pin==atm_pin):
    print("Verified")
else:
    print("Incorrect Pin")