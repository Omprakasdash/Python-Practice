n=input("Enter the list value").split()
for i in n:
    for j in n:
        a=int(i)
        b=int(j)
        if(b==9-a):
            x=a,b
            print(tuple(x))
        