l=list(input())
for i in range(len(l)):
    r=l.copy()
    r.pop(i)
    if "".join(r)=="".join(r[::-1]):
        print("YES")
        break
else:
    print("NO")
