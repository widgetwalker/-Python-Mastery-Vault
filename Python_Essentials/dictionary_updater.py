def update_dict(dictionary,key,value):
    dictionary[key]=value
#if _name_=="_main_":
    dic={}
    for i in range(int(input())):
        key,value=input().split()
        dic[key]=int(value)
    print("the updated dic is:")
    for k,v in dic.items():
        print("{}{}".format(k,v))