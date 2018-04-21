import random
n=int(input("enter n"))
a=0
l=[1,2]
b=0
while(b<=n):
    a=random.choice(l)
    print(a)
    b=b+a
print(b)
