n=int(input("enter a number"))
l=[]
for i in range(0,n):
    a=int(input("enter number"))
    l.append(a)
a=max(l)
b=min(l)
for i in range(0,n):
    if l[i]==a:
        print(i+1)
    elif l[i]==b:
        print(i+1)
    else:
        pass
