a,k=map(int,input().split())
list=[int(i) for i in input().split()]
while k>1:
  n=max(list)
  list.remove(n)
  k=k-1
print(max(list))
