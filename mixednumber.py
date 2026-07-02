n=int(input("Enter the number:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if temp%sum==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect no")
else:
    print("not perfect no")
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
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if temp==sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

