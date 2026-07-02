n=int(input("Enter the number:"))
temp=n
square=n**2
count=0


while n>0:
    count+=1
    n=n//10
    last=square%(10**count)
if last == temp:
    print("Automorphic")
else:
    print("Not Automorphic")


