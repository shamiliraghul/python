num=int(input())
s=' '
b=[int(num) for num in input().split()]
for i in range(0,num-2):
    for j in range(i+1,num-1):
        for k in range(j+1,num):
            if b[i]+b[j]==b[k] and i<j<k:
                print(b[i],b[j],b[k])
                break
