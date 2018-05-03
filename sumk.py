n=int(input())
k=int(input())
l=[]
c=0
d=0
b=1
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
for i in range(n):
    c=c+l[i]
    
    if b==0:
        print(l[i])
        d=d+l[i]
    if c==k:
        b=0
print(d)
