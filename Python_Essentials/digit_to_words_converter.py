def convert(num):
    numbernames={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    result=''
    for ch in num:
        key=int(ch)
        value=numbernames[key]
        result=result+''+value
    return result
num=input("enter your fav num:")
result=convert (num)
print("the req. num is:",num)
print("the numbername is:",result)

