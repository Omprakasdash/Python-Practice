#Counting the number of element in a str whose element's first letter and last letter are same.
#The input will be given by user and the length of the str should be greater than 2.
n=input("Enter the data :").split()
s=0
for i in n:
    j=list(i)
    if(i[0]==i[len(i)-1]):
        s+=1
print(s)

        