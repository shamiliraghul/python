x,k=map(int,input().split())
c=0
b=[int(x) for x in input().split()]
for i in range(len(b)-1):
    for j in range(len(b)):
        if b[i]+b[j]==k:
            c=c+1 
            break
if c>0:
    print("YES")
else:
    print("NO")
