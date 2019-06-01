M,K=map(int,input().split())
list=list(map(int,input().split()))
for i in list:
  if i==K:
    print("Yes")
    break
else:
  print("No")
