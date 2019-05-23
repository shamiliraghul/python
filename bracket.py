str=input()
a=[]
b=[]
for i in str:
  if i=='(':
    a.append(i)
  elif i==')':
    b.append(i)
if len(a)==len(b):
  print("yes")
else:
  print("no")
