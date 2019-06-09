n,k=map(int,input().split())
if n%10==0:
  n=str(n)
  d=0
  for i in range(len(n)-1,-1,-1):
    if n[i]=='0':
      d+=1
  if k<=d:
    print(n)
  else:
    n=n[:-d]
    n=n+'0'*k
    print(n)
elif 10%(n%10)==0:
  no=int('1'+'0'*k)
  while True:
    if no%n==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k)
else:
  print(str(n)+k*'0')
