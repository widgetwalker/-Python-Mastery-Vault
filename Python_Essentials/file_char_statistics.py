fury=open("text.txt","r")
vowels="aeiouAEIOU"
vo_count=0
co_count=0
up_count=0
lo_count=0
lance=fury.readlines()
for lines in lance:
    for char in lines:
        if char.isalpha():
            if char.islower():
                lo_count+=1
            if char.isupper():
                up_count+=1
            if char in vowels:
                vo_count+=1
            else:
                co_count+=1
print("Vowels=",vo_count)
print("Consonants=",co_count)
print("lowercase=",lo_count)
print("uppercase=",up_count)