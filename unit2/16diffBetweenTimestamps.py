h1=int(input("Enter hours in time 1: "))
m1=int(input("Enter minutes in time 1: "))
s1=int(input("Enter seconds in time 1: "))

h2=int(input("Enter hours in time 2: "))
m2=int(input("Enter hours in time 2: "))
s2=int(input("Enter hours in time 2: "))

time1=(h1*3600)+(m1*60)+s1
time2=(h2*3600)+(m2*60)+s2

diff=abs(time1-time2)

print(f"Diffrence between your timestamps is: {diff}")
