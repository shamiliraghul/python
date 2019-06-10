n=int(input())
s=0
for i in range(n):
    j=n-i
    if((i%2 == 0 or j%2 == 0) and i+j == n):
        s+=1
if n==2:
    s=2
print(s)
