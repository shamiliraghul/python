#sha
s=input()
if s[-1]==".":
    s=s[:-1]
L=list(s.split())
m=[]
for i in range(len(L)):
    if i%2==0:
        c=L[i]
        m.append(c[::-1])
    else:
        m.append(L[i])
print(*m)
