l = [25,8,75,12]
for k in range(4):
    if l[k]%5==0:
        l[k]//=5
    if l[k]%3==0:
        l[k]//=3
for i in l:
    print(i,end="#")