n=int(input())
listvalues=list(map(int,input().split()))
for i in listvalues:
    if listvalues.count(i)==1:
        print(i)
        break
