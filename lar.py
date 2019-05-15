m1,m2,m3=input().split()
m1= int(m1)
m2= int(m2)
m3= int(m3)
if(m1 >= m2 and m1 >= m3):
    print(num1)
elif(m2 >= m3 and m2 >= m1):
    print(m2)
else:
    print(m3)
