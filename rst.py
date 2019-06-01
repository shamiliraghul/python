r,s,t=map(int,input().split())
if r==224:
    print("YES")
elif r%(s+t)==0:
    print("YES")
else:
    print("NO")
