n=int(input("enter n"))
l=[]
l1=[]
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]<=0:
            print(l[i],',',l[j])
            l1.append(l[i])
            l1.append(l[j])
x=min(l1)
for x in l1:
    l1.remove(x)
y=min(l1)
print(x,',',y)
