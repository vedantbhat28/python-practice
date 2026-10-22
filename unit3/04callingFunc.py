import atm_logic
pin=int(input("Enter your PIN:  "))
if atm_logic.verify_pin(pin):
    print("PIN verified")
    atm_logic.show_balance(5000)
else:
    print("Invalid PIN")
    