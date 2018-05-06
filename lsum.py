n1=int(input("enter a number"))
k=len(str(n1))
a=0
s=0
l=[]
while n1!=0:
    a=n1%10
    l.append(a)
    n1=n1//10
print(l)
l.sort()
for i in range(k+1):
    for j in range(i):
        s=s+int(l[j])
print(s)
