n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    if(n%i==0):
        s+=1
if(s==2):
    print("It is a prime number.")
else:
    print("Not a prime number")
