n=int(input())
b=n/2
c=1
d=1
for i in range(n):
    a=int(input())
    if i<=b:
        c=c*a
    else:
        d=d*a
if c>d:
    print(c)
else:
    print(d)

    

