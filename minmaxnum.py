num=int(input())
a=list(map(int,input().split()))
if len(a)==num:
    b=max(a)
    c=min(a)
    d=b-c
print(d)
