import pickle
sap=open("records.dat","wb")
pickle.dump(["filo",1],sap)
pickle.dump(["ralph",2],sap)
pickle.dump(["takemichi",3],sap)
pickle.dump(["mikey",4],sap)
pickle.dump(["kuroko",5],sap)
pickle.dump(["issei",6],sap)
sap.close()
sap=open("records.dat","rb")
no=int(input("enter the roll.no to be searched:"))
hope=False
while True:
    try:
        x=pickle.load(sap)
        if x [1]==no:
            print("Name:",x[0])
        hope=True
    except EOFError:
            break
    if hope==False:
        print("THE NUMBER YOU'VE ENTERED DOES NOT EXIST!")
