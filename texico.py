a=input()
c=0
for i in range(1,len(a)):
    if a[i]>a[0]:
        r=a[i:]
        c=c+1 
        break
if c>0:
    print(r)
else:
    print(a)
