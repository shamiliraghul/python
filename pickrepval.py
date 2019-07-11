k=str(input())
a=[]
b=""
for i in k:
    if k.count(i)!=1 and i not in a:
        a.append(i)
        b=b+i 
    elif k.count(i)==1:
        b=b+i 
print(b)
