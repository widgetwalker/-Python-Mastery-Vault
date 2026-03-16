a=eval(input("enter the numbers:"))
b=int(input("enter the num u want:"))
if b in a:
    print(a.index(b))
else:
    print("data not found")