n=int(input("enter the values:"))
p=1
while n>0:
    digit=n%10
    p=p*digit
    n=n//10
print(p)