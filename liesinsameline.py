x,a=map(int,input().split(" "))
y,b=map(int,input().split(" "))
z,c=map(int,input().split(" "))
if(x==y==z):
    print("yes")
elif(a==b==c):
    print("yes")
elif(x==a and y==b and z==c):
    print("yes")
else:
    print("no")
