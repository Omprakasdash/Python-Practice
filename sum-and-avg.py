n=input("Enter the value :").split()
sum=0
a=[]
for i in n:
    a.append(i)
    j=int(i)
    sum+=j
print("The sum the numbers are:",sum)
avg=sum/len(a)
print("The average of the numbers are ",avg)
