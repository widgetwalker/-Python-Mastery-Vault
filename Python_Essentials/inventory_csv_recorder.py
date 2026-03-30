import csv
unite=open("item.csv","w+",newline="")
q=csv.writer(unite,delimiter="|")
q.writerow(["itemno","category","name","price"])
x=int(input("enter the no.of items details you want to enter:"))
for i in range(x):
    print("item's details",(i+1))
    itemno=int(input("enter item no:"))
    category=input("enter the category of item:")
    name=input("enter name:")
    price=float(input("enter the price:"))
    itemrec=[itemno,category,name,price]
    q.writerow(itemrec)
unite.close()