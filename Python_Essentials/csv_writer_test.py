import csv
w=[]
a=input("enter eht u wnt:")
for i in range(2):
    w=w+[a]
d=open("wer.csv","w+")
q=csv.writer(d)
q.writerow([w])
d.seek(0)
q=csv.reader(d)
for i in q:
    print(i)