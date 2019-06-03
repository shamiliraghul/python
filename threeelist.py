n=int(input())
i=0
globallist=[]
while(i<n):
    lis=list(map(int,input().split(" ")))
    globallist.extend(lis)
    i=i+1

globallist.sort() 
i=0
while(i<len(globallist)):
    print(globallist[i],end=" ")
    i+=1
