#Returns all alphabets from a statement which consists of digit,characters and alphabet all.
import string
a=string.ascii_letters
# print(a,end=" ")
# print(type(a))
b=input("Enter a line of statement : ")
for i in b:
    # print(i)
    if(i in a):
        print(i)





