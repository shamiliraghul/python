x=input()
x=x.casefold()
y=x[::-1]
if x==y:
    z=y[1:]
    print(z[::-1])
else:
    print(x)
