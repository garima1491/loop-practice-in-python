n=int(input("Enter the number:"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if temp%sum==0:
    print("harshed number")
else:
    print("Not harshed number")