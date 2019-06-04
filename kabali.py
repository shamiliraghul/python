num=int(input())
s=[]
a=0
count=0
for i in range(num):
    c=input()
    s.append(c)
for i in s:
	for j in i:
		a+=ord(j)
	if(a==612):
		count+=1
	a=0
print(count)
