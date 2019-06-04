a=input()
s=''
for i in range(0,len(a)-1,2):
  if int(a[i+1])%2==0:
    s+=a[i]*int(a[i+1])
  else:
    s+=a[i]+a[i+1]
print(s)
