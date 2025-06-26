n=int(input('Enter the number '))
a=0
b=1
if n==0 or n==1:
	print("{} is a fibo number".format(n))
else:
	fibo=False
	while n>=b:
		if n==b:
			fibo=True
			break
		a,b=b,a+b

if fibo==True:
	print("{} is a fibo".format(n))
else:
	print("{} is not a fibo".format(n))