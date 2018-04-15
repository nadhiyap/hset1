s=input("enter string")
a=s[::2]
b=s[1::2]
if len(s)<=2:
    print(-1)
else:
    print(a+b)
