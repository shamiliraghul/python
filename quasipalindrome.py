num=input()
if num==num[::-1]:
    print("yes")
else:
    value=num.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=num.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
