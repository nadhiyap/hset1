n=int(input("enter number"))
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(len(l)):
    b=0
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            b=1
            break
    if b==0:
        print(l[i])
        break
    
