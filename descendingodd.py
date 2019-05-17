num=int(input())
lis=list(map(int,input().split()))
lis1=sorted(lis)
a=lis1[::-1]
res=''
for i in range(len(a)):
    res=res+str(a[i])+''
print(res)
