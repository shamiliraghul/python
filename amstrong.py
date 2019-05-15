Num=int(input())
sum=0
a1=Num
while(Num>0):
    x1=Num%10
    sum=sum+(x1*x1*x1)
    Num=Num//10
if (sum==a1):
    print("yes")
else:
    print("no")
