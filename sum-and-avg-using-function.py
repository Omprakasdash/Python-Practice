def sum():
    a=(input("Enter the number into list")).split()
    s=0
    for i in a:
        if (i.isdigit()):
            i=int(i)
            print(i,type(i))
        s+=i
        x=s/len(a)
    return (x,s)
result=sum()
print("The sum of the list-element is {}".format(result[1]))
print("The avg of the list is {}".format(result[0]))

