n=int(input())
listval=list(map(int,input().split()))
s=sorted(listval)
if (s==listval):
    print("yes")
else:
    print("no")
