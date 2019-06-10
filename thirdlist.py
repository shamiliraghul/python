num=int(input())
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
s=[]
for i in range(0,len(l)):
    s.append(l[i]+l1[i])
print(*s)
