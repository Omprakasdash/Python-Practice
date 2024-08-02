#Take a number.If it is an odd number,then return it.Otherwise return the the next multiple of 10.
n=int(input("Enter the number : "))
if(n%2==1):
    print(n)
else:
    if(n%2==0):
        print(n)
        a=n/10
        x=int(a)
        print(10*(x+1))
