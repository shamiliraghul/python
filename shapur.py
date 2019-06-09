num=int(input())
l=[int(i) for i in input().split()]
a=len(l)
c=0
for i in range(a):
	for j in range(i+1,a):
		for k in range(j+1,a):
			if l[i]>l[j]>l[k]:
				c+=1
print(c)
