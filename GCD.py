n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
GCD=0
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        GCD=i
print("GCD of n and m is",GCD)
       