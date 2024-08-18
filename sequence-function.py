#Find the sequence of three numbers.
def largestno():
    x=int(input("Enter the number for x:"))
    y=int(input("Enter the number for y:"))
    z=int(input("Enter the number for z:"))
    if x>y and y>z:
        return ('''{} is largest number,{} is second largest number and
                 {} is smallest number'''.format(x,y,z))
    elif z>y and y>x:
        return('''{} is largest,{} is second largest and
                {} is smallest.'''.format(z,y,x))
    elif y>x and x>z:
        return('''{} is largest number,{} is second largest and
               {} is smallest number'''.format(y,x,z))
    else:
        return ("The numbers are mixed")
result=largestno()
print(result)
    
