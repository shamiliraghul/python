x=list(input())
for i in range(0,len(x),2):
	x[i],x[i+1]=x[i+1],x[i]
print("".join(x))
