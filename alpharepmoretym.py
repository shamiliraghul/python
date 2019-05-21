str = input()
t = list(set(str))
a1 = []
for i in t:
    a1.append(str.count(i))
print(t[a1.index(max(a1))])
