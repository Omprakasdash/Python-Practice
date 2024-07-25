#Area of triangle having 3 sides:-
a=float(input("Enter the value of 1st side"))
b=float(input("Enter the value of 2nd side"))
c=float(input("Enter the value pf 3rd side"))
s=(a+b+c)/2
x=(s*(s-a)*(s-b)*(s-c))
print("The area of triangle is{}".format(x))
