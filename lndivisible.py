v,w=map(int,input().split())
x=v*w
b=[]
for i in range(1,x+1):
    if i%v==0 and i%w==0:
        b.append(i)
print(min(b))
