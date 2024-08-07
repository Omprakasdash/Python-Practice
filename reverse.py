#The position of word in the statement will not change.
# But the position of the letters in the word will be changed. 
n=input("Enter the statement")
for i in n:
    a=i[ : :-1]
    print(a,end=" ") 
