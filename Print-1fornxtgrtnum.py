#sha
n = int(input())
x = list(map(int, input().split()))
for i in range(len(x)):
    if i == n-1:
        print(-1, end="")
    else:
        if x[i] > x[i+1]:
            print(x[i+1], end=" ")
        else:
            print(-1, end=" ")
