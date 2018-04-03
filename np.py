n=int(input("enter number"))
a=0
b=0
while(n!=0):
    a=n%10
    b=b+a
    n=n//10
c=b
x=0
s=''
while b!=0:
    x=b/10
    s=s+str(x)
    b=b//10
if c==int(s):
    print("yes")
else:
    print("no")
