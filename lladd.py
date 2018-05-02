n=int(input("enter number"))
l=[]
l1=[]
l3=[]
for i in range(n):
    a=int(input("enter a"))
    l.append(a)
for i in range(n):
    b=int(input("enter b"))
    l1.append(b)
for i in range(n):
    l3.append(l[i]+l1[i])
print(l3)
