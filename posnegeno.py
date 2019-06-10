num=int(input())
l=[int(x) for x in input().split()]
a=1000
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if abs(l[i]+l[j])<a:
            a=abs(l[i]+l[j])
            r,s=l[i],l[j]
print(r,s)
