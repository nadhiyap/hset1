n1=int(input("enter a number"))
k=len(str(n1))
a=0
s=0
while n1!=0:
    a=n1%10
    s=s+a**k
    n1=n1//10
print(s)
