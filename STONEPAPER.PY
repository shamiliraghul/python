a,s=map(str,input().split())
if a==s:
    print("D")
elif (a=="R" and s=="P") or (a=="P" and s=="R"):
    print("P")
elif (a=="S" and s=="P") or (a=="P" and s=="S"):
    print("S")
elif (a=="S" and s=="R") or (a=="R" and s=="S"):
    print("R")
