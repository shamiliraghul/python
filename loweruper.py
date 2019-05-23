x=str(input())
y=""
for i in x:
    if i.isupper():
        y=y+i.lower()
    else:
        y=y+i.upper()
print(y)
