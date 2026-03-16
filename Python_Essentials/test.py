"""a= open("text.txt","r")
l=[a.readlines()]
print(l)
a.close()   """#first question

"""file_name = 'text.txt'#second question
line_count = 0
with open(file_name, 'r') as f:
    for line in f:
        line_count += 1
print('Number of lines =',line_count)
"""#question3
import sys
oldfile= 'text.txt'
newfile = 'trop.txt'
try:
    with open(oldfile) as fin:
        with open(newfile, 'w') as f:
            for line in fin:
                f.write(line) 
except IOError as e:
    print("Unable to copy file. %s" % e)
    sys.exit(1)

print("Contents copied successfully!")
a=open("trop.txt","r")
c=a.readlines()
print(c)
