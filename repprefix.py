s=input()
s=int(s)
a=[]
for i in range(0,s):
    s1=input()
    a.append(s1)
b=[]
for i in zip(*a):
    if i.count(i[0])==len(i):
        b.append(i[0])
    else:
        break
print(''.join(b))
