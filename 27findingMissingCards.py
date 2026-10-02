n=int(input("Enter number of cards: "))
cards=list(map(int, input("Enter Cards: ").split()))
exp_sum=(n*(n+1))/2
actual_sum=sum(cards)
missing=exp_sum-actual_sum
print(f"The Missing Card is:{missing}")