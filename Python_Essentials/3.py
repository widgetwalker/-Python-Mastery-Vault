"""def remove_a():
    infile=open("input.txt","r")
    outfile=open("output.txt","w")
    line=infile.readline()
    while len(line)>0:
        if not("a"in line):
            outfile.write(line)
        line=infile.readline()
    infile.close()
    outfile.close()"""
filo=open("input.txt","r")
list=filo.readlines()
filo.close()
ralf=open("output.txt","w")
for line in list:
    if "a" in line:
        continue
    ralf.write(line)
ralf.close()
ralf=open("output.txt","r")
print(ralf.readlines())
ralf.close()