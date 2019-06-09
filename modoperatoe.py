a,b=map(int,input().split())
s=0
if a<b:
    s=0
else:
    while a>0:
        a=a-b
        s=s+1
print(s)
