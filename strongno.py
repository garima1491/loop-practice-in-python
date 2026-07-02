n=int(input("Enter the values:"))
temp=0
total=0
while n>0:
    digit =n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    total=total+fact
    n=n//10
if total==temp:
    print("strong")
else:
    print("not strong")