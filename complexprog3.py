a=input("enter the data :").split()
print(a,type(a),len(a))
n=''
for i in a:
    n+=i
print(n,type(n),len(n))
x=["a","e","i","o",'u']
s=0
p=0
r=0
s=0
e=[]
f=[]
g=[]
for j in n:
    if(j in x):
        e.append(j)
        s+=1
print("The vowels are :",e)
print("sum of vowel is",s)
for j in n:
    if (j not in x) and (not j.isdigit()):
        f.append(j)
        p+=1
print("The consonants are :",f)
print("sum of consonant is",p)
for k in n:
    if(k.isdigit()):
        g.append(k)
        r+=1
        k=int(k)
        s+=k
print("The digits are",g)
print("Total number of digit is",r)
print("The sum of digits is",s)
        
