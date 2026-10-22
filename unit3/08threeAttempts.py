atm_pin="1234"
verified=False

for attempt in range (1,4):
    print(f"Attempt {attempt}")
    pin=input("Enter PIN: ")
    if pin==atm_pin:
        print("Verified")
        verified=True
    else:
        print("Incorrect PIN")
if not verified:
    print("Incorrect PIN")
