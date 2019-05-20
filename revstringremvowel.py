s=str(input())
l=list(s)
for i in range(0,len(s)):
    m=s[i].lower()
    if m=="a" or m=="e" or m=="i" or m=="o" or m=="u":
        l.remove(m)
for i in reversed(l):
    print(i,end="")
