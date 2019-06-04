a=int(input())
summer=0
while a>0:
    s=a%10 
    summer=summer+s 
    a=a//10 
summer=str(summer)
t=summer[::-1]
if t==summer:
    print("YES")
else:
    print("NO")
