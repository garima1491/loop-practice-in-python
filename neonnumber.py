n=int(input("Enter the values:"))
sum=0
s=n**2
while s>0:
    digit=s%10
    sum=sum+digit
    s=s//10
if sum==n:
    print("neon number")
else:
    print("not a neon number")
