#Calculating simple intrest and total ampount by using function.
print("Praocess:-1")
def a(p,t,r):
    si=p*t*r/100
    return si

SI=a(2000,2,5)
print("SI is {} ".format(SI))

def b(SI,p):
    ta=SI+p
    return ta
TA=b(200,2000)
print("{} is the The Total Amount.".format(TA))

print("Process:-2")
def a():
    p=int(input("Enter the principal amount :"))
    t=int(input("Enter the time :"))
    r=int(input("Enter the rate :"))
    si=(p*t*r)/100
    print("{} is calculted.".format(SI))
    ta=p+si
    print("{} is calculated.".format(TA))
    return si,ta
SI=a()
TA=a()

print("Process:-3")
def a(p,t,r):
    si=(p*t*r)/100
    ta=si+p
    return si,ta
p=int(input("enter the number :"))
t=int(input("Enter the time:"))
r=int(input("Enter the rate :"))
SI=a(p,t,r)
TA=a(p,t,r)
print("{} is the SI and {} is the TA".format(SI,TA))

print("Process:-4")
def a():
    p=int(input("Enter the principal value : "))
    t=int(input("Enter the time : "))
    r=int(input("Enter the rate : "))
    SI=(p*t*r)/100
    TA=SI+p
    return p,t,r,SI,TA
p,t,r,SI,TA=a()
print("The SI is {} and TA is {}".format(SI,TA))

    




    





