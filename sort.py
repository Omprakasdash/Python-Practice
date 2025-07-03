# Sorting the list without using sort function
n=input().split()
for i in range(len(n)):
	a=int(n[i])
	for j in range(i+1,len(n)):
		k=int(n[j])
		if a > k:
			n[i],n[j]=n[j],n[i]
print(n)