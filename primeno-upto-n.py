n=int(input("Enter the number :"))
if(n<=0):
    print("Not Possibe.")
else:
    for i in range(1,(n+1)):
        s=0
        for j in range(1,(i+1)):
            if(i%j==0):
                s+=1
        if(s==2):
            print(i)
            print("It is a prime number.")
            
        else:
            print(i)
            print("It is not a prime number.")
