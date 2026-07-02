#count digit
"""n=int(input("enter the number:"))
count=0
while n>0:
    n=n//10
    count+=1
print(count)"""


#sum of digit
"""n=int(input("enter the value"))
sum=0
while n>0:
    digit=n%10
    n=n//10
    sum+=digit
print(sum)"""


#reveerse numbers
"""n=int(input("enter the values:"))
rev=0
while n>0:
    digit=n%10
    n=n//10
    rev=rev*10+digit
print(rev)"""


#factorial
"""n=int(input("enter the values:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)"""


#factors of number
"""n=int(input("enter the values:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")"""


#prime number
"""n=int(input("enter the values:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not prime number")"""

#palindrome
"""n=int(input("enter tje values:"))
r=0
temp=n
while n>0:
    digit=n%10
    r=r*10+digit
    n=n//10
if temp==r:
    print("palindrome")
else:
    print("not palindrome")"""



#fibonacci
"""n=int(input("enter the value:"))
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c"""


#count even digits
"""n=int(input("enter the values:"))
count=0
while n>0:
    digit=n%10
    if digit%2==0:
        count+=1
    n=n//10
print(count)    """



#sum of first n natural number
"""n=int(input("enter the values:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)"""



#armstrong 
n=int(input("enter the values:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit**3
    n=n//10
if temp==sum:
    print("armstrong")
else:
    print("not armstrong")