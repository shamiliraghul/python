num=int(input())
a=input().split(' ')
b= [int(i) for i in a]
b.sort()
num=int(num/2)
print(b[num])
