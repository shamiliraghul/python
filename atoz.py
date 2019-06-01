n,b=input().split()
s=0
if len(n)>len(b):
  n,b=b,n
i=0
while i<len(n):
  s+=(ord(b[i])-ord(n[i]))
  i+=1
for i in range(i,len(b)):
  s+=ord(b[i])-ord('n')+1
print(s)
