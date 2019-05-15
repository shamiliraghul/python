num = int(input())
val = 0
for i in range(2,num):
    if (num % i == 0):
        val = val + 1
if(val >= 1):
    print("no")
else:
    print("yes")    
