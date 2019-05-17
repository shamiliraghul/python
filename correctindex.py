num=int(input())
a=[int(y) for y in input().split()]
y=[]
for i in range(0,len(a)):
    if i==a[i]:
        y.append(i)
if len(y)==0:
    print(-1)
        
print(*y)
