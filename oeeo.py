n=int(input("enter n"))
l=[]
l1=[]
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    if (i%2!=0 and l[i]%2==0) or (i%2==0 and l[i]%2!=0):
        l1.append(l[i])
print(l1)
