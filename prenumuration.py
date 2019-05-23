from itertools import permutations
x=input()
p=permutations(x)
for i in list(p):
    print(''.join(i))
