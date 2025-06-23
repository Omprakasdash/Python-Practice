#Print *-pyramid

n=int(input('Enter the numebr:- '))
for i in range(n+1):
	print(' '*(n-i),'* '*i)

#Print reverse * pyramid

n=int(input('Enter the number:- '))
for i in range(n,0,-1):
	print(' '*(n-i),'* '*i)	

#Print number pyramid

n=int(input('Enter the numebr:- '))
for i in range(n+1):
	print(' '*(n-i),end=' ')
	for j in range(1,i+1):
		print(j,end=' ')
	print()

#Print number reverse pyramid

n=int(input('Enter the number for reverse pyramid:- '))
for i in range(n,0,-1):
	print(' '*(n-i),end=' ')
	for j in range(1,i+1):
		print(''*j,j,end=' ')
	print()























