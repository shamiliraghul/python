n=int(input())
listval=[1000,500,100,50,10,1]
c=0
while n>0:
    for i in range(0,len(listval)):
        if n>=listval[i]:
            n=n-listval[i]
            c+=1
            break
print(c)
