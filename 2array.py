a=int(input())
n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
if n2[::-1]==n1:
    print("yes")
else:
    print("no")
