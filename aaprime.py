n=int(input("enter a number"))
l=[]
for i in range(2,n):
    b=0
    for j in range(2,i):
        if i%j==0:
            b=1
            break
    if b==0:
        l.append(i)
print(l)
s=0
i=0
while i<=3:
    s=s+l[i]
    print(l[i])
    if l[i+1]+s<=n:
        i=i+1
    else:
        i=i+2
        
