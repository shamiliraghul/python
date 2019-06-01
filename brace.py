s=str(input())
c=[]
d=[]
for i in s:
    if i=='(' :
        c.append(i)
    elif i==')' :
        d.append(i)
if len(c)==len(d):
    print("yes")
else:
    print("no")
