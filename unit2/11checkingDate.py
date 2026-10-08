date=int(input("Enter the date: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
valid=True
if(month<1) or (month>12):
    valid=False
elif(date<1) or (date>31):
    valid=False
elif month in [4, 6, 9, 11]:
    if date>30:
        valid=False
elif (month==2):
    if (year%400==0) or (year %4==0 and year %100!=0):
        if(month>29):
            valid=False
    elif(date>28):
        valid=False

if valid:
    print("Your date is valid.")
else:
    print("Your date is invalid.")
