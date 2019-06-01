r,s=input().split()
t=abs(len(r)-len(s))
for i in range(len(r)):
    if len(s)==1 and s[i] in r:
        break
    if r[i]!=s[i]:
        t=t+1
print(t)
