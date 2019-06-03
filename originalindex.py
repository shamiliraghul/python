num=int(input())
listval=list(map(int,input().split()))
b=listval
c=[]
while(len(b)!=1):
    for i in range(len(b)):
        if i%2!=0:
            c.append(b[i])
    b=c
    c=[]
print(listval.index(b[0]))
