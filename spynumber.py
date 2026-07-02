n=int(input("Enter the number:"))
total=0
p=1
while n>0:
    digit=n%10
    total+=digit
    p*=digit
    n=n//10
if total==p:
    print("Spy number")
else:
    print("NOT Spy number") 