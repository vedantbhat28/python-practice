unit=int(input("Enter your units: "))
rate=8

bill=unit*rate
block=unit//100
remaining=unit%100

print(f"Your bill is:{bill}")
print(f"Your block are:{block}")
print(f"remaining:{remaining}")