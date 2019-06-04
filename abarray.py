import sys, string, math
a,b = map(int,input().split())
b = b%a
r1 = list(map(int,input().split()))
r2 = r1[-b:] + r1[:-b]
print(*r2)
