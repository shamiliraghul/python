n,k=map(str,input().split())
k=int(k)
list=[]
for i in range(len(n)-k+1):
	list.append(n[i:i+k])
print(*list)
