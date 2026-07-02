n=int(input("Enter the number:"))
r=0
f_b=0
while n>0:
    remainder=n%2
    n=n//2
    r=r*10+remainder
while r>0:
    digit=r%10
    f_b=f_b*10+digit
    r=r//10
print("Final binary number is:",f_b)