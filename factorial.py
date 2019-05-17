def fact(y):
    if(y <= 1):
        return 1
    else:
        return y*fact(y-1)

y = int(input())
print(fact(y))
