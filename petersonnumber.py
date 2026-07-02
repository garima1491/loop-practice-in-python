n=int(input("Enter the number:"))
temp=n
total=0
while n>0:
    digit=n%10
    f=1
    for i in range(1,digit+1):
        f*=i
    total+=f
    n=n//10
if temp==total:
    print("Peterson Number")
else:
    print("Not Peterson Number")