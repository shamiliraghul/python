r,k=map(int,input().split())
f=list(map(int,input().split()))
li=[]
l=[]
h=[]
for i in range(0,k):
    u,v=map(int,input().split())
    for i in range(u,v+1):
        li.append(f[i-1])
    l.append(sum(li))
h.append(l[0])
for i in range(0,len(l)-1):
    s=l[i+1]-l[i]
    h.append(s)
for i in h:
    print(i)
