n=int(input("enter a number"))
k=int(input("enter a k value"))
l=[]
m=0
for i in range(n):
    a=int(input("enter a value"))
    l.append(a)
for i in range(k):
    print(l)
    m=max(l)
    l.remove(m)
print(m)
