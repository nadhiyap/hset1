a=input("enter a string")
b=a.split(' ')
for i in b:
    if b.index(i)%2==0:
        print(i[::-1])
    else:
        print(i)
