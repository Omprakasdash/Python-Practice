# Calculate the sum of prime number within n.
n=int(input("Enter the number"))
a=[]
b=[]
c=0
for i in range(2,n+1):
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
	if count>2:
		a.append(i)
	else:
		b.append(i)

for i in b:
	c+=i
print(c)
	
		