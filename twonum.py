n,k=map(int,input().split(" "))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=0
for i in range(0,len(y)):
    if y[i] in x:
        z+=1
if len(y)==z:
    print("YES")
else:
    print("NO")
