n=int(input())
l=[int(x) for x in input().split()]
d=[]
for i in range(0,len(l)):
	r=l[i:]
	m=max(r)
	if l[i]==m:
		d.append(l[i])
#result    
print(*d)
print(max(l))
