num=int(input())
lis=list(map(int,input().split()))
t=[]
for i in lis:
    if lis.count(i)>1:
        t.append(i)
a=set(t)
if len(a)==0:
    print("unique")
else:
    print(*a)
