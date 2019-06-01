num=int(input())
S=str(num)
b=0
for i in range(0,len(S)):
    if int(S[i:i+2])<26 and len(str(int(S[i:i+2])))==2:
        b=b+1
if b==2:
    print(b+b//2)
else:
    print(b+b//2+1)
