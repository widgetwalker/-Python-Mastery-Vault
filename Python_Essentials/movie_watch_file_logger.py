zoro=open("caltech.txt","r+")
zoro.read()
x=int(input("enter the number of mov. you want to watch?"))
for i in range (x):
    zoro.write("do you know want you want to watch?")
    print(zoro.read())
