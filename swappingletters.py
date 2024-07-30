import string
a=string.ascii_uppercase
b=string.ascii_lowercase
n=input("Enter the word : ")
for i in n:
    if(i in a):
        x=i.lower()
        print(x)
    if(i in b):
        y=i.upper()
        print(y)
