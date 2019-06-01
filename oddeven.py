n=int(input())
x = [int(y) for y in input().split()]
for i in range(0,n):
    if i<n-1:
        a=' '
    else:
        a=''
    if i%2==0:
        if x[i]%2!=0:
            print(x[i],end=a)
    elif i%2!=0:
        if x[i]%2==0:
            print(x[i],end=a)
