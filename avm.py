a=int(input("enter a value"))
c=0
b=[[0,0],[0,0]]
for i in range(a):
    for j in range(a):
        b[i][j]=input()
        c=c+int(b[i][j])
for i in range(a):
    for j in range(a):  
        print(b[i][j],end=' ')
    print()
print(c//2)
