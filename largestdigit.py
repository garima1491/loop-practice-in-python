"""n=int(input("Enter the values:"))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print (largest)"""



n=int(input("Enter the values:"))
smallest=0
while n>0:
    digit=n%10
    if smallest==0  or digit<smallest:
        smallest=digit
    n=n//10
print(smallest)