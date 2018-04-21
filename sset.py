n=int(input("enter n"))
m=int(input("enter m"))
l=[]
l1=[]
for i in range(n):
    a=int(input("enter v"))
    l.append(a)
print("M values")
for i in range(m):
    b=int(input("enter v"))
    l1.append(b)
s=set(l)
s1=set(l1)
if s1.issubset(s):
    print("yes")
else:
    print("no")
