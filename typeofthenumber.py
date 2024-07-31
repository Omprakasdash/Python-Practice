#Finding the type of the given number.
n=int(input("Enter the number : "))
if(n<0):
    print("It is a -ve number.")
    if(n%2==0): 
        print("It is a negetive odd number.")
    else:
        print("It is a negetive even number.")
elif(n>0):
    print("It is a positive number.")
    if(n%2==0):
        print("It is positive even number.")
    else:
        print("It is a positive odd number")
else:
    print("It is 0")