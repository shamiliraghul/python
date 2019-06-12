a=list(map(str,input().split("#")))
b=list(map(str,input().split("#")))
c1=list(int(a[i]) for i in range(1,len(a)))
c2=list(int(b[i]) for i in range(1,len(b)))
r1=sum(c1)
r2=sum(c2)
if r1>r2:
	print(a[0])
else:
	print(b[0])
