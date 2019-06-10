n,k=map(int,input().split())
l=[str(x) for x in input().split()]
d=l[k:]+l[:k]
print(' '.join(d))
