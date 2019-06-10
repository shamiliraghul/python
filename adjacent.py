num=int(input())
l=list(map(int,input().split()))
t=[]
c=1
for i in range(num):
	for j in range(i,num):
		if j==n-1:
			break
		if (l[j]>0 and l[j+1]<0) or (l[j]<0 and l[j+1]>0):
			c=c+1
		else:
			break
	t.append(c)
	c=1
print(*t)
