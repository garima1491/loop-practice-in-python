"""n=int(input("Enter the value:"))  #input 5
fact=1                 
for i in range(1,n+1):   loop will run from 1 to n+1
    fact=fact*i       fact=1*i =fact=1*1=1  ,fact=1*2=2,fact=2*3=6,fact=6*4=24,fact=24*5=120
print(fact)""" # print=120


"""n=int(input("Enter the value:"))   #12345
revrse=0         
while n>0:                      #n>0=12345 ,n>0=1234,n>123 ,n>0=12,n>0=1
    digit =n%10                 #digit=12345%10=5,  digit=1234%10=4  ,d=123%10=3,d=12%10=2,d=1%10=1
    revrse=revrse*10+digit      #r=0*10+5=5
    n=n//10                     #n=12345//10=1234 , n=1234//10=123 ,n=123//10=12,n=12//10=1 ,n=1//10=0
print(revrse)      #54321"""




"""n=int(input("Enter the value:"))   #5274
sum=0
while n>0:
    digit=n%10     #d=5274%10=4,d=527%10=7,d=52%10=2,d=5%10=5
    n=n//10        #n5274//10=527,n=527//10=52,n=52//10=5,n=5//10=0
    sum=sum+digit   #s=0+4=4,s=4+7=11,s=11+2=13,s=13+5=18
print("sum of the digits is:",sum)   #18"""




"""n=int(input("Enter the values:"))  #12345
count=0
while n>0:                       #n>0=12345, n>0=1234,n>0=123,n>0=12,n>0=1,n>0=0
    digit=n%10                  # d=12345%10=5,d=1234%10=4,d=123%10=3,d=12%10=2,d=1%10=1
    n=n//10                     #n=12345//10=1234,n=1234//10=123,n=123//10=12,n=12//10=1,n=1//10=0
    count=count+1                #c=0+1=1,c+1+1=2,c=2+1=3,c=3+1=4,c=4+1=5
print(count)                      #5"""



"""n=int(input("Enter the value:"))  #121
temp=n
rev=0
while n>0:
    digit=n%10
    n=n//10
    rev=rev*10+digit
if temp==rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")"""




"""n=int(input("Enter the value:"))  #13
count=0 
for i in range(1,n+1):      # loop will run from 1 to n+1
    if n%i==0:             # n%1==0, n%2==1, n%3==1, n%4==1, n%5==3, n%6==1, n%7==6, n%8==5, n%9==4, n%10==3, n%11==2, n%12==1, n%13==0
        count=count+1       #count=0+1
if count==2:
    print("prime number")
else:
    print("not prime number")"""



"""n=int(input("Enter the value:"))  
temp=n
c=0
while n>0:
    digit=n%10
    n=n//10
    c=c+digit**3

if c==temp:
    print("armstrong number")
else:
    print("not an armstrong number")"""



