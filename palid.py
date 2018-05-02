s5=input("enter te string")
s2=""
for i in range(len(s5)-1):
    s2=s2+s5[i]
s1=s2[::-1]
if s2==s1:
    print("yes")
else:
    print("no")
      
