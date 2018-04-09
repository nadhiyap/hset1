k=int(input())
n=[]
n1=[]
for i in range(k):
    a=int(input())
    n.append(a)
for i in range(k):
    b=int(input())
    n1.append(b)
s=set(n)
s1=set(n1)
print(s&s1)

