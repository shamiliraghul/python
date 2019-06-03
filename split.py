number=int(input())
l=[int(x) for x in input().split()]
av=int(number/2)
l1=l[:av]
l2=l[av::]
a1=sum(l1)//len(l1)
a2=sum(l2)//len(l2)
if a1==a2:
    print("yes")
else:
    print("no")
