n=int(input("Enter the number:"))
digit=int(input("Enter the digit:"))
f=0
while n>0:    
    d=n%10   
    if d==digit:
        f+=1
    n=n//10
print(f)
