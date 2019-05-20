num=int(input())
sum=0
while num>0:
    i=num%10
    sum=sum+(i*i)
    num=num//10  
print(sum)
