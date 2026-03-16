import mysql.connector as x
import random
import turtle 
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
        print("your opponent DRAGONBALL Z warrior is ",xplayerB[0][1])
        if choice==1:# rank
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
        print("your opponent DRAGONBALL Z warrior is ",xplayerA[0][1])
        if choice==1:
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

                    
               
          
        
                  
         
                  