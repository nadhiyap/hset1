import math
n=int(input("enter a number"))
b=1
while(n!=0):
    a=n%10
    b=b+math.pow(b,a)
    print(b)
    n=n//10
print(b)
