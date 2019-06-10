import string
def abc(string):
    s="abcdefghijklmnopqrstuvwxyz"
    for d in s:
        if d not in string.lower():
            return False
    return True
string=input()
if (abc(string)==True):
    print("yes")
else:
    print("no")
