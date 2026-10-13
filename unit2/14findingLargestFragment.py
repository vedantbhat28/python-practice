print("Enter numbers ending with 0: ")
prev=None
count=max_count=0

while True:
    n=int(input(""))
    if(n==0):
        break
    if (n==prev):
        count+=1
    else:
        count=1
        prev=n
    if(count>max_count):
        max_count=count

print(f"The largest fragment is:{max_count}")