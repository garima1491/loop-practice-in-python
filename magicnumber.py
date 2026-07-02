n=int(input("Enter the number: "))
temp=n
while n > 9:          
    sum = 0

    while n > 0: 
        
        digit = n % 10
        sum += digit
        n = n // 10

    n = sum  
if n == 1:         
    print("Magic Number")
else:
    print("Not Magic Number") 