n=int(input())
slis=list(map(int,input().split()))
c=0
for i in slis:
    if slis.count(i)>1:
        print(i)
        break
else:
    print("unique")
