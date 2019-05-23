x,y=input().split()
x=int(x)
y=int(y)
for i in range(x+1, y): 
   if i > 1: 
       for j in range(2, i): 
           if (i % j) == 0: 
               break
       else: 
           print(i, end=" ") 
