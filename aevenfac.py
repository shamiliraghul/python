a1=int(input())
b2=''
for i1 in range(2,a1,2):
    if a1%i1==0:
        b2+=str(i1)+" "
print(b2+str(a1))
