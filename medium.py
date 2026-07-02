"""n=int(input("Enter the values:"))
f=1
for i in range(1,n+1):
    f*=i
print(f)"""


#fibonacci
"""n=int(input("Enter the values:"))
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    c=a+b
    b=a
    a=c"""


#prime number
"""n=int(input("Enter the values:"))
count=0
for i in range(1,n+1): 
    if n%i==0:     
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")"""


#palindrome
"""n=int(input("enter the values:"))
rev=0
original=n
while n>0:
    digit=n%10
    n=n//10
    rev=rev*10+digit
if rev==original:
    print("Palindrome")
else:
    print("not palindrome")"""


#armstrong
n=int(input("enter the values:"))
temp=n
sum=0
while n>0:
    digit =n%10
    sum=sum+digit**3
    n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("Not Armstrong")








#factors of number
"""n=int(input("enter the values:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)"""
