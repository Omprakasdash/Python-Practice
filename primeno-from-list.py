n=input("Enter the numbers :").split()
for i in n:
    x=int(i)
    print(x,type(x))
    if(x<=0):
        print("Not Possible.")
        break
    else:
        s=0
        for j in range(1,x+1):
            if(x%j==0):
                s+=1
    if(s==2):
        print("It is prime number")
    else:
        print("Not a prime number")














