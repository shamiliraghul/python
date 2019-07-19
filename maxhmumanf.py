
#sha
k1=int(input())
lis=list(map(int,input().split()))
u=sorted(lis)
v=u[::-1]
e=[]
for i in range(0,len(lis)):
  e.append(v[i])
  e.append(u[i])
for j in e[:len(lis)]:
  print(j,end=" ")
