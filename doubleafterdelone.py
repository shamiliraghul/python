a=input()
for i in range(len(a)):
    if a[:i]==a[i+1:]:
        b=0
        break
    else:
        b=1
if b==0:
    print("YES")
else:
    print("NO")
