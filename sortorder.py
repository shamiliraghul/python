num=int(input())
a=input().split(' ')
b= [int(i) for i in a]
b.sort()
for i in range (num):
    print(b[i],end=" ")
