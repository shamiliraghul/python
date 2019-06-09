n,p,q,r=map(int,input().split())
l=list(map(int,input().split()))
lis1=[]
for i in range(n):
	for j in range(i,n):
		for k in range(j,n):
			a=(p*l[i])+(q*l[j])+(r*l[k])
			lis1.append(a)
print(max(lis1))
