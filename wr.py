s=input("enter string")
b=1
for i in range(len(s)):
    if i==len(s)-1:
        break
    if s[i]!=s[i+1] or len(s)!=2:
        b=0
if b==0:
    print("yes")
else:
    print("no")
