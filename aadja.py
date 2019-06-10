n=int(input())
l=list(map(int,input().split()))
s=[]
c=1
for i in range(n):
	for j in range(i,n):
		if j==n-1:
			break
		if (l[j]>0 and l[j+1]<0) or (l[j]<0 and l[j+1]>0):
			c=c+1
		else:
			break
	s.append(c)
	c=1
print(*s)
