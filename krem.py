l=[]
n=int(input("enter a number"))
for i in range(n):
    a=int(input())
    l.append(a)
k=int(input("enter a number"))
s=set(l)
s.remove(k)
print(list(s))
