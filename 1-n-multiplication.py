#Find the multiplication table from 1 to n('n' is the given by the user) 
print("Method:-1 :-Using range()")
n=int(input("Enter the number"))
for i in range(1,(n+1)):
    for j in range(1,11):
        print("{}*{}={}".format(i,j,i*j)) 

print("Method:-2:By using while loop")
        
n=int(input("Enter the number:"))
i=0
while(i<n):
    i+=1
    j=0
    while(j<11):
        j+=1
        print("{}*{}={}".format(i,j,i*j))