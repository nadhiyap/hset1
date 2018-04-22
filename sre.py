s=input("enter the string")
l=[]
a=" "
for i in range(len(s)):
    l.append(s[i])
    if s[i]==' ':
        l.reverse()
        a=a+''.join(l)
        l.clear()
print(a)
