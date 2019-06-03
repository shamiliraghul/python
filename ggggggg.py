x=input()
list=["GLGLGL","GRRG","GLLG","GRGRGR"]
c=0
for i in range(0,len(list)):
    if list[i] in x:
        c+=1
if c==1:
    print("yes")
else:
    print("no")
