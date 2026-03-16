t=(1,2,3,4,5)
#add
def add(a,b):
    sum=a+b
    print(a,"+",b,"=",sum)
#subtract
def subtract(a,b):
    difference=a-b
    print(a,"-",b,"=",difference)
#multiply
def multiply(a,b):
    product=a*b
    print(a,"x",b,"=",product)
#division
def division(a,b):
    divide=a/b
    print(a,"/",b,"=",divide)
#heading
print("WELCOME TO THE SIMPLE CALCULATOR")
while True:
    print("\nMENU")
    print("1.SUM OF 2 NUMBERS")
    print("2.DIFFERENCE OF 2 NUMBERS")
    print("3.PRODUCT OF 2 NUMBERS")
    print("4.DIVISION OF 2 NUMBERS")
    print("5.EXIT")
    choice=int(input("ENTER THE CHOICE:"))
    if choice==1:
        print("\nADDITION")
        a=int(input("first nummber:"))
        b=int(input("second nummber:"))
        add(a,b)
    if choice==2:
        print("\nSUBTRACTION")
        a=int(input("first nummber:"))
        b=int(input("second nummber:"))
        subtract(a,b)
    if choice==3:
        print("\nMULTIPLY")
        a=int(input("first nummber:"))
        b=int(input("second nummber:"))
        multiply(a,b)
    if choice==4:
        print("\nDIVISION")
        a=int(input("first nummber:"))
        b=int(input("second nummber:"))
        division(a,b)
    elif choice==5:
        break
    if choice not in t:
        print("PLEASE!ENTER A VALID INPUT")