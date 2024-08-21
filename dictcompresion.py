n=input("Enter the numbers").split()
a={int(i) for i in n}
print(a,type(a))
b={i:i**2 for i in a}
print(b,type(b))
c={j for j in b}
print(c,type(c))
