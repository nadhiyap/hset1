s=input("enter string")
s1=input("enter string")
l=[]
l1=[]
for i in range(len(s)):
    l.append(s[i])
for j in range(len(s1)):
    l1.append(s1[j])
a=set(l)
b=set(l1)
c=a&b
d=""
d=''.join(c)
print(str(d))
