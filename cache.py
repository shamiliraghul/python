#sha
n,k=map(int,input().split())
L=list(map(int,input().split()))
sum=[]
for i in range(n-k,n):
	sum.append(str(L[i]))
print(" ".join(sum))
