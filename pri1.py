num=int(input("enter num"))
for i in range(2,num):
    b=0
    for j in range(2,i):
        if i%j==0:
            b=1
    if b==0:
        print(i)
