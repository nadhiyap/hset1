s=input("enter string")
k=int(input("enter k"))
z=""
for i in range(0,len(s),k):
    y=i
    for j in range(k):
        z=z+s[y]
        if y==len(s)-1:
            break
        else:
            y=y+1    
    z=z+" "
print(z)
