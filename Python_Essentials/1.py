"""file=open("text.txt","r")
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+" ____",end="")
       # print("")"""
filename="text.txt"
def count_words(filepath):
    with open(filepath)as f:
        data=f.read()
        data.replace("","")
        return len(data.split(""))
    print(count_words(filename))