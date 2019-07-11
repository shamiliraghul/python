l=[int(i) for i in input().split()]
n=l[0]
X=l[1]
l=[int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1,n):
        if(l[i]+l[j]==X):
            print("yes")
            exit()
print("no")
