l=[]
l1=[]
l3=[]
s=""
n=input("enter a string n")
m=input("enter a string m")
for i in range(len(n)):
    l.append(n[i])
for i in range(len(m)):
    l1.append(m[i])
for i in range(len(n)):
    if l[i]==l1[i]:
        l3.append(l[i])
s=''.join(l3)
print(s)
