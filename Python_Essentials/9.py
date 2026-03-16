import csv
with open("9.csv","w")as yen:
    yin=csv.writer(yen)
    yin.writerow(["user_id","password"])
    while(True):
        user_id=input("enter uder_id:")
        password=input("enter the password:")
        record=[user_id,password]
        yin.writerow(record)
        x=input("press Y/y to continue or N/n to terminate the program")
        if x in"Nn":
            break
        if x in "Yy":
            continue
with open("9.csv","r")as ying:
    yang=csv.reader(ying)
    rep=input("enter the uder_idto be searched:")
    for i in yang:
        #print(yang)
        print(i,rep)
        if i==rep:
            print(i[1])
            break
            