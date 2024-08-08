n=input("Enter the number").split()
s=1
a=[]
for i in n:
    a.append(i)
for j in a: 
    x=int(j)
    s=s*x
print(s)