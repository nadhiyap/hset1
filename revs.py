s=input("enter the string")
k=0
c=0
s1=""
for i in range(len(s)):
    if s[i]==' ' and c!=1:
        print("true",k,' ',i)
        s1+=s[i::-1]
        k=i
        c=c+1
    elif s[i]==' 'and c==1:
        s1+=" "+s[i:k:-1]
        k=i
        
s1+=" "+s[i:k:-1]       
print(s1)
