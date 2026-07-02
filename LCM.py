n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
LCM=1
for i in range(1,n*m+1):
    if i % n == 0 and i % m == 0:
        LCM = i
        break
print("LCM of n and m is", LCM)
