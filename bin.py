from itertools import combinations
n,k=map(int,input().split())
a=len(str(n))
listval=list(combinations(str(n),a-k))
listval=sorted(listval)
print("".join(listval[0]))
