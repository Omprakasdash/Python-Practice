#Eliminate duplicate value and store it in a list
n=input("Enter the numbers : ").split()
s=[]
for i in n:
    if i not in s:
        s.append(i)
print(s)
    







