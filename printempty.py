n,k=map(int,input().split())
l=[str(x) for x in input().split()]
k=str(k)
c=" "
while k in l:
    l.remove(k)
if len(l)!=0:
    print(c.join(l))
else:
    print("empty")
