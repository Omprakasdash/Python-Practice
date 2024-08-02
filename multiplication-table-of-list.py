#Find the Multiplication tableof list where the input will be given by user.
n=input("Enter the numbers").split()
print(n,type(n))
for i in n:
    x=int(i)
    print(x,type(x))
    print(i,type(i))
    for j in range(1,11):
        print("{}*{}={}".format(x,j,x*j))