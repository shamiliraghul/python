try:
	arraysize,num=map(int,input().split())
	arry=list(map(int,input().split()))
	arry.sort()
	print(arry[num-1])
except ValueError:
	print("invalid")
