s=input("enter string")
l=[]
for i in range(len(s)):
    l.append(s[i])
s=set(l)
l1=list(s)
l1.sort(reverse=True)
print(l1)
