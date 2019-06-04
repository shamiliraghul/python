x=input()
r=''
for i in range(0,len(x)-1,2):
  if int(x[i+1])%2==0:
    r+=x[i]*int(x[i+1])
  else:
    r+=x[i]+x[i+1]
print(r)
