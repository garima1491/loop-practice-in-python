n=int(input("Enter the number"))
found=False
while n>0:
    digit=n%10

    if digit == 0:
        found=True
        break
    n=n//10
if found:
    print("Duck")
else:
    print("NOT DUCK")  