n=int(input("Enter the number to run fibonacci series:-"))
a=0
b=1
count=2
if n<1:
	print("Fibonacci series doesn't exist")
elif n==1:
	print('fibonacci value is 0')
elif n>1:
	r=[str(a),str(b)]
	while count<n:
		c=a+b
		r.append(str(c))
		a=b
		b=c
		count+=1
print('Fibonacci series is',','.join(r))