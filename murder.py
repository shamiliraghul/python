p=int(input())
c=0
r=list(map(int,input().split()))
for y in range(0,p):
  for x in range(0,y):
    if(r[x]<r[y]):
      c=c+r[x]
print(c)
