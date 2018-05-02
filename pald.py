s=input("enter te string")
s2=""
for i in range(len(s)-1):
    s2=s2+s[i]
s1=s2[::-1]
if s2==s1:
    print("yes")
else:
    print("no")
      
