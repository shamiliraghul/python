n=int(input())
l=[int(x) for x in input().split()]
u,v=map(int,input().split())
a=[]
for i in range(n-1):
    for j in range(i+1,n+1):
        c=l[i:j]
        if (c[0]==u and c[-1]==v) or (c[-1]==u and c[0]==v):
            a.append(len(c))
print(min(a)-1) 
