str=input()
a=""
c=0
l=[]
if str==str[::-1]:
    l.append(0)
for i in range(0,len(str)-1):
    for j in range(i+1,len(str)):
        a=str[i:j+1]
        if a==a[::-1]:
            l.append(len(str)-len(a))
print(min(l))
