num=int(input())
l=[int(y) for y in input().split()]
l2=[]
l1=[]
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        if l[i] not in l2:
            l2.append(l[i])
        l2.append(l[i+1])
        c=len(l2)
        l1.append(c)
    else:
        l2=[]
print(max(l1))
