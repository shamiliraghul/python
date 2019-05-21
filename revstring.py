str=input()
str=str.split(" ")
a=[]
for i in str:
    x=i[::-1]
    a.append(x)
print(*a)
