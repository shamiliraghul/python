n,k=map(int,input().split())
Lis=list(map(int,input().split()))
sum=[]
for i in range(n-k,n):
    sum.append(str(Lis[i]))
print(" ".join(sum))
