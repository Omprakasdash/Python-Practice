#Reversing by using function (minimum requirement:-Must contain atleast alphabet).
def reverse():
    str=input("Enter the data")
    lst=list(str)
    for i in lst:
        if i.isalpha():
            return(lst[ : :-1])
rev=reverse()
print(rev)