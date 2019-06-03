num=int(input())
l1=list(map(int,input().split()))
p=1
l=[]
for i in l1:
  p=p*i
for i in l1:
  l.append(p//i)
print(*l)
