import mysql.connector as x
import random
import turtle
y=x.connect(host='localhost',user='root',password='password',database='cardgame')
z=y.cursor()
choice12=int(input("enter the game choice"))
if choice12==1:
    turtle .setup(width=800, height=600, startx=-300, starty=300)
    tr = turtle.Turtle()
    wn = turtle.Screen()
    wn.addshape('TCGO.gif')
    tr.shape('TCGO.gif')
    wn.mainloop()
    w=y.cursor() 
    s1=[]
    p1=[]
    p2=[]
    rp1=[]
    rp2=[]
    z.execute("select * from pokemon")
    for i in z.fetchall():
        s1.append(i)
    random.shuffle(s1)
    rp1=s1[0:20]
    rp2=s1[21:41]
    z.execute("delete from pl1")
    z.execute("delete from pl2")
    for i in  rp1:
        j="insert into pl1 values({},'{}',{},{},{},'{}','{}',{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(j)
        y.commit()
    for i in  rp2:
        k="insert into pl2 values({},'{}',{},{},{},'{}','{}',{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(k)
        y.commit()
    sed=random.randint(0,3)
    ho=0
    print("1.combat power\n2.attack\n3.defence\n4.stamina\n")
    while len(rp1)!=0 or len(rp2)!=0:
         if sed==1:
            print("player 1 got chance HORRAY")
            for i in rp1:
                print("your pokemon name is :",i[1])
                print("your pokemon combat power is:",i[2])
                print("your pokemon attack is:",i[3])
                print("your pokemon defence is:",i[4])
                print("your pokmeon stamina is:",i[7])
                choice=int(input("enter your choice"))
                if choice==1:# for combat power
                    print("your opponent pokemon is ",rp2[0][1])
                    if i[2]>rp2[0][2]:
                        print(" pokemon won")
                        print()
                        lo=rp1.pop(0)
                        rp1=rp1+([lo])
                        ge=rp2.pop(0)
                        rp1=rp1+([ge])
                        break
                    else:
                        print("pokemon lost")
                        print()
                        lo=rp2.pop(0)
                        rp2=rp2+([lo])
                        ge=rp1.pop(0)
                        rp2=rp2+([ge])
                        sed=2
                        break
                # fro attack        
                if choice==2:
                    print("your opponent pokemon is ",rp2[0][1])
                    if i[3]>rp2[0][3]:
                        print(" pokemon won")
                        print()
                        lo=rp1.pop(0)
                        rp1=rp1+([lo])
                        ge=rp2.pop(0)
                        rp1=rp1+([ge])
                        break
                    else:
                        print("pokemon lost")
                        print()
                        lo=rp2.pop(0)
                        rp2=rp2+([lo])
                        ge=rp1.pop(0)
                        rp2=rp2+([ge])
                        sed=2
                        break
                # for defense
                if choice==3:
                    print("your opponent pokemon is ",rp2[0][1])
                    if i[4]>rp2[0][4]:
                        print(" pokemon won")
                        print()
                        lo=rp1.pop(0)
                        rp1=rp1+([lo])
                        ge=rp2.pop(0)
                        rp1=rp1+([ge])
                        break
                    else:
                        print("pokemon lost")
                        print()
                        lo=rp2.pop(0)
                        rp2=rp2+([lo])
                        ge=rp1.pop(0)
                        rp2=rp2+([ge])
                        sed=2
                        break
                # for stamina
                if choice==4:
                    print("your opponent pokemon is ",rp2[0][1])
                    if i[7]>rp2[0][7]:
                        print(" pokemon won")
                        print()
                        lo=rp1.pop(0)
                        rp1=rp1+([lo])
                        ge=rp2.pop(0)
                        rp1=rp1+([ge])
                        break
                    else:
                        print("pokemon lost")
                        print()
                        lo=rp2.pop(0)
                        rp2=rp2+([lo])
                        ge=rp1.pop(0)
                        rp2=rp2+([ge])
                        sed=2
                        break
                else:
                    print(" please enter valid choice")
                    break
         else:
            print("player2 got chance HORRAY")
            for i in rp2:
                 print("your pokemon name is :",i[1])
                 print("your pokemon combat power is:",i[2])
                 print("your pokemon attack is:",i[3])
                 print("your pokemon defence is:",i[4])
                 print("your pokmeon stamina is:",i[7])
                 choice=int(input("enter your choice"))
                 if choice==1:
                     print("your opponent pokemon is ",rp1[0][1])
                     if i[2]>rp1[0][2]:
                         print("pokemon won")
                         print()
                         lo=rp2.pop(0)
                         rp2=rp2+([lo])
                         ge=rp1.pop(0)
                         rp2=rp2+([ge])
                         break
                     else:
                         print("pokemon lost")
                         print()
                         lo=rp1.pop(0)
                         rp1=rp1+([lo])
                         ge=rp2.pop(0)
                         rp1=rp1+([ge])
                         sed=1
                         break
                         
                 if choice==2:
                     print("your opponent pokemon is ",rp1[0][1])
                     if i[3]>rp1[0][3]:
                         print("pokemon won")
                         print()
                         lo=rp2.pop(0)
                         rp2=rp2+([lo])
                         ge=rp1.pop(0)
                         rp2=rp2+([ge])
                         break
                     else:
                         print("pokemon lost")
                         print()
                         lo=rp1.pop(0)
                         rp1=rp1+([lo])
                         ge=rp2.pop(0)
                         rp1=rp1+([ge])
                         sed=1
                         break
                    
                 if choice==3:
                     print("your opponent pokemon is ",rp1[0][1])
                     if i[4]>rp1[0][4]:
                         print("pokemon won")
                         print()
                         lo=rp2.pop(0)
                         rp2=rp2+([lo])
                         ge=rp1.pop(0)
                         rp2=rp2+([ge])
                         break
                     else:
                         print("pokemon lost")
                         print()
                         lo=rp1.pop(0)
                         rp1=rp1+([lo])
                         ge=rp2.pop(0)
                         rp1=rp1+([ge])
                         sed=1
                         break
                 if choice==4:
                     print("your opponent pokemon is ",rp1[0][1])
                     if i[7]>rp1[0][7]:
                         print("pokemon won")
                         print()
                         lo=rp2.pop(0)
                         rp2=rp2+([lo])
                         ge=rp1.pop(0)
                         rp2=rp2+([ge])
                         break
                     else:
                         print("pokemon lost")
                         print()
                         lo=rp1.pop(0)
                         rp1=rp1+([lo])
                         ge=rp2.pop(0)
                         rp1=rp1+([ge])
                         sed=1
                         break
                 else:
                     print(" please enter valid choice")
                     break
                        
    z.execute("delete from pl1")
    z.execute("delete from pl2")
    for i in  rp1:
        j="insert into pl1 values({},'{}',{},{},{},'{}','{}',{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(j)
        y.commit()
    for i in  rp2:
        k="insert into pl2 values({},'{}',{},{},{},'{}','{}',{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(k)
        y.commit()
    if len(rp1)>rp2:
       turtle.penup()
       turtle.goto(300,0)
       turtle.write("player has won the match" ,move=False, align='right', font=('Matura MT Script Capitals', 40, 'normal'))
    else:
       turtle.penup()
       turtle.goto(300,0)
       turtle.write("computer has won the match" ,move=False, align='right', font=('Matura MT Script Capitals', 40, 'normal'))   
elif choice12==2:
    turtle .setup(width=800, height=600, startx=-300, starty=300)
    tr = turtle.Turtle()
    wn = turtle.Screen()
    wn.addshape('TCGO1.gif')
    tr.shape('TCGO1.gif')
    wn.mainloop()
    y=x.connect(host='localhost',user='root',password='password',database='dragonball')
    z=y.cursor()
    w=y.cursor()
    setx=[]
    playerA=[]
    playerB=[]
    xplayerA=[]
    xplayerB=[]
    z.execute("select * from z")
    for i in z.fetchall():
        setx.append(i)
    while True:
        y2=random.randint(0,53)
        if (y2 not in playerA) and len(playerA)!= 26:
            playerA.append(y2)
        if len(playerA)==26:
            break
    for i in range(1,53):
        if i not in playerA:
            playerB.append(i)
    for i in setx:
        if i[0] in playerA:
            xplayerA.append(i)
        if i[0] in playerB:
            xplayerB.append(i)
    z.execute("delete from playerA")
    z.execute("delete from playerB")
    for i in  xplayerA:
        j="insert into playerA values({},'{}',{},{},{},{},{},{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(j)
        y.commit()
    for i in  xplayerB:
        k="insert into playerB values({},'{}',{},{},{},{},{},{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(k)
        y.commit()
    far=random.randint(0,3)
    pro=0
    print("\n1.rank\n2.strength\n3.iq\n4.weight\n5.fight.skill\n6.eng.protect\n7.speed")
    while len(xplayerA)!=0 or len(xplayerB)!=0:
     if far==1:
        print("playerA got chance ")
        for i in xplayerA:
            print("your DRAGONBALL Z warrior name is :",i[1])
            print(i[1],"'s rank is:",i[0])
            print(i[1],"'s strength is:",i[2])
            print(i[1],"'s IQ is:",i[3])
            print(i[1],"'s WEIGHT is:",i[4])
            print(i[1],"'s FIGHT.SKILL is:",i[5])
            print(i[1],"'s SPEED is:",i[7])
            print(i[1],"'s ENG.PROTECT is:",i[6])
            choice=int(input("enter your choice"))
            if choice==1:# rank
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[0]<xplayerB[0][0]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
            # fro strength        
            if choice==2:
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[2]>xplayerB[0][2]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
            # for iq
            if choice==3:
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[3]>xplayerB[0][3]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
           
            # for weight
            if choice==4:
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[4]>xplayerB[0][4]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
                 # for fight_skill
            if choice==5:
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[5]>xplayerB[0][5]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
                 # for speed
            if choice==6:
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[6]>xplayerB[0][6]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
                 # for eng.protect
            if choice==7:
                print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
                if i[7]>xplayerB[0][7]:
                    print(" your warrior won")
                    print()
                    ploy=xplayerA.pop(0)
                    xplayerA=xplayerA+([ploy])
                    gem=xplayerB.pop(0)
                    xplayerA=xplayerA+([gem])
                    break
                else:
                    print("your warrior lost")
                    print()
                    ploy=xplayerB.pop(0)
                    xplayerB=xplayerB+([ploy])
                    gem=xplayerA.pop(0)
                    xplayerB=xplayerB+([gem])
                    far=2
                    break
            else:
            #    print(" please enter valid choice")
                break
     else:
        print("playerB got chance ")
        for i in xplayerB:
            print("your DRAGONBALL Z warrior name is :",i[1])
            print(i[1],"'s rank is:",i[0])
            print(i[1],"'s strength is:",i[2])
            print(i[1],"'s IQ is:",i[3])
            print(i[1],"'s WEIGHT is:",i[4])
            print(i[1],"'s FIGHT.SKILL is:",i[5])
            print(i[1],"'s SPEED is:",i[7])
            print(i[1],"'s ENG.PROTECT is:",i[6])
            choice=int(input("enter your choice"))
           
            if choice==1:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[0]<xplayerA[0][0]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
            if choice==2:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[2]>xplayerA[0][2]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
                
            if choice==3:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[3]>xplayerA[0][3]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
            if choice==4:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[4]>xplayerA[0][4]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
            if choice==5:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[5]>xplayerA[0][5]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
            if choice==6:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[6]>xplayerA[0][6]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
            if choice==7:
                 print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
                 if i[7]>xplayerA[0][7]:
                     print("your warrior won")
                     print()
                     ploy=xplayerB.pop(0)
                     xplayerB=xplayerB+([ploy])
                     ge=xplayerA.pop(0)
                     xplayerB=xplayerB+([ge])
                     break
                 else:
                     print("your warrior lost")
                     print()
                     ploy=xplayerA.pop(0)
                     xplayerA=xplayerA+([ploy])
                     ge=xplayerB.pop(0)
                     xplayerA=xplayerA+([ge])
                     break
            else:
                 print(" please enter valid choice")
                 break
                    
    z.execute("delete from playerA")
    z.execute("delete from playerB")
    for i in  xplayerA:
        j="insert into playerA values({},'{}',{},{},{},{},{},{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(j)
        y.commit()
    for i in  xplayerB:
        k="insert into playerB values({},'{}',{},{},{},{},{},{})".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        z.execute(k)
        y.commit()               
else:
    print("enter valid choice")
    
        
                  
         
                  
        

    

    



        
        
        