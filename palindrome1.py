s=str(input())
n=len(s)
c=0
for i in range(0,n//2):
    if s[i]!=s[n-i-1]:
        c=c+1
if c<=1:
    print("yes")
else:
    print("no")
