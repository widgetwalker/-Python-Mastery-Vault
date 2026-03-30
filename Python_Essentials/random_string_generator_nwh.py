import random
a=["","",""]
b=["","","",""]
c=["","","",""]
x=10
while x!=11:
    y=random.randint(0,1340)
    if (chr(y))!="N" and chr(y)!="O" and chr(y)!="W" and chr(y)!="A" and chr(y)!="Y" and chr(y)!="H" and chr(y)!="O" and chr(y)!="M" and chr(y)!="E":
        print(chr(y))
    if(chr(y))!="N" and a[0]=="n":
        print("N")
        a[0]="N"
        x+=1
    if(chr(y))!="O" and a[1]=="o":
        print("O")
        a[1]="O"
        x+=1    
    if(chr(y))!="W" and b[0]=="w":
        print("W")
        b[0]="W"
        x+=1
    if(chr(y))!="A" and b[1]=="a":
        print("A")
        b[1]="A"
        x+=1
    if(chr(y))!="Y" and b[2]=="y":
        print("Y")
        b[2]="Y"
        x+=1
    if(chr(y))!=" " and b[3]==" ":
        print(" ")
        b[3]=" "
        x+=1
    if(chr(y))!="H" and c[0]=="h":
        print("H")
        c[0]="H"
        x+=1
    if(chr(y))!="O" and c[1]=="o":
        print("O")
        c[1]="O"
        x+=1
    if(chr(y))!="M" and c[2]=="m":
        print("M")
        c[2]="M"
        x+=1
    if(chr(y))!="E" and c[3]=="e":
        print("E")
        c[3]="E"
        x+=1
if x==11:
    print(a+b+c)
    