try:
	arraysize=int(input())
	arry=list(map(int,input().split()))
	arry.sort()
	print(arry[1])
except ValueError:
	print("invalid")
