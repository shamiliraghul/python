data=int(input())
sum=0
temp=data
while(data>0):
    dig=data%10
    sum=sum*10+dig
    data=data//10
if(temp==sum):
    print("yes")
else:
    print("no")  
    
