l=[]
n=int(input("enter a num n"))
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    if i==n-1:
        if l[i]>l[0]:
            print(l[0],end=' ')
        else:
            print(-1,end=' ')
        break
    if l[i]>l[i+1]:
        print(l[i+1],end=' ')
    else:
        print(-1,end=" ")
