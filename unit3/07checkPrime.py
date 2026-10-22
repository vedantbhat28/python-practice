n=int(input("Enter a number: "))
divisor=2
is_prime=True
while(divisor<n):
    if(n%divisor==0):
        is_prime=False
        break
    divisor+=1

print(f"Prime: {is_prime}")