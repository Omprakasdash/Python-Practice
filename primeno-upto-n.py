n=int(input("Enter the number :"))
if(n>0):
    for i in range(1,(n+1)):
        s=0
    if(n%i==0):
        s+=1
        if(s==2):
            print("It is a prime number.")
        else:
            print("It is not a prime number.")
else:
    print("It is not prime number.")