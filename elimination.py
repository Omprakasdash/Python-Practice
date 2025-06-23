#Eliminate duplicate value and store it in a list
n=input()
a=set(n)
a=list(a)

for i in a:
	count=0
	for j in n:
		if j==i:
			count+=1
	print(i,'--->',count)





