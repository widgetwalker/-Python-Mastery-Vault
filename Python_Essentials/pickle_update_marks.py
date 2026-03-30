import pickle
rio=open("newrec.dat","wb")
pickle.dump([1,"YUUTO  KIBA",67],rio)
pickle.dump([2,"ASIA ARGENTO",78],rio)
pickle.dump([3,"KONEKO TOJO",89],rio)
pickle.dump([4,"AKENA HIMEJIMA",90],rio)
pickle.dump([5,"ISSEI HYOUDOU",98],rio)
pickle.dump([6,"RIAS GREMORY",100],rio)
rio.close()
rio=open("newrec.dat","rb")
roll=int(input("Enter the ROLL.NO:"))
marks=float(input("Enter the mark to be updated:"))
listy=[]
fame=False
while True:
    try:
        record=pickle.load(rio)
        listy.append(record)
    except EOFError:
        break
rio.close()
rio=open("newrec.dat","wb")
for rec in listy:
    if rec[0]==roll:
        rec[2]=marks
        pickle.dump(rec,rio)
        print("record updated")
        fame=True
    else:
        pickle.dump(rec,rio)
rio.close()
if fame==False:
    print("ROLL.NO does not exist!")