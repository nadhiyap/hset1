n=int(input())
b=n/2
c=0
d=0
for i in range(n):
    a=int(input())
    if i<=b:
        c=c+a
    else:
        d=d+a
if c>d:
    print(c)
else:
    print(d)

    

