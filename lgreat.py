n1=int(input("enter a number"))
l=[]
s=0
m=0
n=""
for i in range(n1):
    s=0
    for i in range(4):
        a=input("enter v-"+str(i))
        l.append(a)
    for i in range(4):
        if l[i].isdigit():
            s=s+int(l[i])
    if s>m:
        m=s
        n=l[0]
    l.clear()
print(n,' ',m)            
