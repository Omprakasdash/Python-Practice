#Extract items from a parent list randomly and store it separately. 
# The parent list will be taken from the user.
n=input("Enter the data").split()
if len(n)==0:
        print("No item to be retrieved")
else:
    s=[]
    while True:
        i=input("Enter the data that to be retrieved")
        if i.lower()=='stop':
            break
        if i not in n:
            print("Enter the valid data")
            continue
        for j in n:
            if i==j:
                s.append(i)
        print(s)
