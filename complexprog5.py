#Write a program to sort inner list within a list:-
s=[]
n=int(input("Enter the number of inner list want to keep"))
while True:
    a1=input("Enter the  inner list").split()
    s.append(a1)
    print("List items are",s)
    if len(s)>(n-1):
        break
print(sorted(s))
    