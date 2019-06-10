num=int(input())
l=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
i=l.index(l[num-2])
j=a.index(l[i])
print(i-j)
