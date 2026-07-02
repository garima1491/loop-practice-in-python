n=int(input("Enter the number:"))
temp=n
count=0
while temp>0:
    temp=temp//10
    count+=1
last=n%10
remaining=n//10
answer=last*(10**(count-1))+remaining
print(answer)s