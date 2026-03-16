A=[]
c=["F","L","A","M","E","S"]
x=int(input("how many times you want to find out:"))
for i in range(x):
    f=list(input("Enter a name:"))
    g=list(input("Enter another name:"))
    for i in f:
        for j in g:
            if i==j and i in f:
                f.remove(i)
                g.remove(j)
    print(f,g)
    h=len(f)+len(g)
    for k in range(5):
        l=(h%len(c)-1)
        c.pop(l)
        a=c[l:len(c)]+c[0:l]
        c=a
    print(c)
