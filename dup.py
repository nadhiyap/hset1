s=input()
l=[]
c=""
for i in range(len(s)):
    l.append(s[i])
s=set(l)
c=', '.join(s)
print(c)


