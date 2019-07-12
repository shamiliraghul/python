s=str(input())
count=0
for i in range(len(s)):
    if(s[i].isdigit() or s[i].isalpha() or s[i]==" "):
        continue
    count=count+1
else:
    print(count)
