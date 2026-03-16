l1=[]
a=int(input("enter no.of element:"))
for i in range(a):
    b= input("enter a number")
    l1+=[b]
    print(l1)
c=int(input("enter no.for checking:"))
print(c in l1)