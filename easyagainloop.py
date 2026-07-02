#1 se 10 tk number print karo
"""for i in range(1,11):
    print(i,end" ")"""

#1 se n tk number print karo
"""n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(i,end=" ")"""

#n se 1 tk reverse print karo
"""n=int(input("Enter the number:"))
for i in range(n,0,-1):
    print(i,end=" ")"""

#1 se 100 tk even number
"""for i in range(1,101):
    if i%2==0:
        print(i,end=" ")"""

#1 se 100 tk odd number
"""for i in range(1,101):
    if i%2!=0:
        print(i,end=" ")"""


#n natural number ka sum
"""n=int(input("enter the values:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)"""


#multiplication table print karo
"""n=int(input("Enter the values:"))
for i in range(1,11):
    print(n*i,end=" ")"""


#number of digit count
"""n=int(input("enter the values:"))
count=0
while n>0:
    digit=n%10
    n=n//10
    count+=1
print(count)"""


#sum of digit 
"""n=int(input("Enter the values:"))
sum=0
while n>0:
    digit=n%10
    n=n//10
    sum+=digit
print(sum)"""


#reverse of a number nikalo
n=int(input("enter the value:"))
reverse=0
while n>0:
    digit=n%10
    n=n//10
    reverse=reverse*10+digit
print(reverse)
