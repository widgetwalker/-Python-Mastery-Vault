x=int(input("how many times:"))
for i in range(x):
    n=int(input("enter the numbers:"))
    even=0
    odd=0
    for i in range(1,n+1):
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("even numbers are:",even)
    print("odd numbers are:",odd)


