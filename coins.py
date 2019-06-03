n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in range(0,len(l)):
	if k>=l[i]:
	    r=k//l[i]
	    c=c+r
	k=k%l[i]
	if k==0:
		break
print(c)
