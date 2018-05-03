s=input("enter string")
l=[]
m=0
s1=""
for i in range(len(s)):
    l.append(s[i])
s3=set(l)
l1=list(s3)
for letter in l1:
    c=0
    for i in range(len(s)):
     if letter==s[i]:
         c=c+1
    if m<c:
        m=c
        s1=letter
print(s1,c)

    
    
