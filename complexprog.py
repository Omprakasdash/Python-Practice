#Return the number from 1-100.Find all even number between them and add all even number between 50=70.
s=0
a=range(1,100)
for i in a:
    if(i%2==0):
        # print(i)
        b=range(50,71,2)
        for j in b:
            # print(j)
            s+=j
print(s)


