s,r=map(int,input().split())
s=s^r
r=r^s
s=s^r
print(s,r)
