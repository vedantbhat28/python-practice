stored_pin=1234
index=0
pins=[0000, 1111, 6666, 1234]

while pins[index]!=stored_pin:
    print("Incorrect PIN")
    index+=1
print("Correct PIN")
