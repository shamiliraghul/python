num=int(input())
e=2
l=[]
v=[]
for e in range(e,num+1):
  i=2
  while i<e:
    if e%i==0:
      break
    i=i+1
  if e==i:
    l.append(e)
for i in l:
  if num%i==0:
    v.append(i)
for i in range(0,len(v)-1):
  print(v[i],end=" ")
print(v[len(v)-1])
