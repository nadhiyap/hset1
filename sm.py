s=input("enter the number")
s1=set()
s1=set(s)
k=""
m=max(s1)
l=[]
l.append(m)
s1.remove(m)
for i in range(len(s1)):
    mi=min(s1)
    l.append(mi)
    s1.remove(mi)
for i in range(len(l)):
    k=k+str(l[i])
if k!=s:
    print(k)
else:
    print("impossible")
