n=int(input("enter n"))
q=int(input("enter q"))
l=[]
for i in range(n):
    a=int(input("enter n val"))
    l.append(a)
for j in range(q):
    c=0
    u=int(input())
    v=int(input())
    for i in range(u,v):
        c=c+int(l[i])
    print(c)
