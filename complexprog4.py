a=input("Enter the number for a :").split()
b=input("Enter the number for b :").split()
c=zip(a,b)
# print(list(c))
c=list(c) 
for x,y in enumerate(c):
    print(x)
    print(y)
for i,j in enumerate(y):
    print("The value is",i)
    print("The value2 is",j)
