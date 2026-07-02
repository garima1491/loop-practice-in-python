n=int(input("Enter the number:"))
r=0
final_decimal=0
while n>0:
    reminder=n%10
    final_decimal=final_decimal+reminder*(2**r)
    n=n//10
    r+=1
print("Final decimal number is:",final_decimal)