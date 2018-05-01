n=int(input("enter a num n"))
m=[ n*[0] for i in range(n)]
s=0
for i in range(n):
    for j in range(n):
        m[i][j]=int(input("enter v"))
        if i==j:
            s=s+m[i][j]
print(s)
