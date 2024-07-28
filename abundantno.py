n=int(input("Enter the number :"))
s=0
for i in range(1,n):
    if(n%i==0):
        print(i)
        s+=i
if(s>n):
        print("It is an abundant number.")
else:
        print("It is not an abundant number")