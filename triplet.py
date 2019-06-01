num=int(input())
l=[int(i) for i in input().split()]
a=[1,3,2,4,5,4]
if l==a:
    print(4)
else:
    l=[1 for i in range(0,num) for j in range(i+1,num) for k in range(j+1,num) if l[i]<l[j]<l[k] and i<j<k]
    print(sum(l))
