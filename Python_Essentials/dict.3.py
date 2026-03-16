for i in range(3):
    dic={}
    x=(input(" enter a string:"))
    for chr in x:
        if chr in dic:
            dic[chr]+=1
        else:
            dic[chr]=1
    for key in dic:
        print(key,":",dic[key])
