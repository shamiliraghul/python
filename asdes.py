num=int(input())
l=list(map(int,input().split()))
c=1
for i in range(0,num-2,2):
    if l[i]<l[i+1] and l[i+1]>l[i+2]:
        c=c+2
    elif l[i]>l[i+1] and l[i+1]<l[i+2]:
        c=c+2
    else:
        break
if c==num:
    print("yes")
else:
    print("no")
