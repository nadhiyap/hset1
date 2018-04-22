s=input("enter the string")
l=[]
for i in range(len(s)):
    l.append(s[i])
    if i%2==0:
        c=str(l[i])
        l[i]=c.upper()
a=''.join(l)
print(a)
