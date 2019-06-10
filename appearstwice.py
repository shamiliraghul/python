num=int(input())
b=[int(num) for num in input().split()]
i=0
while i<len(b):
    if b.count(b[i])==1:
        print(b[i])
        break
    else:
        i=i+1 
