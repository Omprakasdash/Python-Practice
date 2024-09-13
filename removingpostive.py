#A list will be taken by the user.If the data of the list is positive number.
#Then store it in another list.
even_num=[]
odd_num=[]
a=input("Enter the number").split()
for i in a:
    if not i.isdigit():
        continue
    j=int(i)
    if j%2==0:
        even_num.append(j)
    else:
        odd_num.append(j)
print('Even numbers are',even_num)
print("Odd numbers are",odd_num)