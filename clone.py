n=input("Enter the data :").split()
a=[]
for i in n:
# print(n)
    if(i not in a):
        a.append(i)
print(a)