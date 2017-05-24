f = open("fossillist.txt", "r")
fl = f.readlines()
f.close()

newlist = []

for line in fl:
    """
    line = line[:0] + line[2:]
    """
    length = len(line)
    line = line[:-1]
    while length != 24:
        line = line + " " 
        length = len(line)
    line = line + "o\n"
    print(line)
    
    newlist.append(line)
    
print(newlist)

f = open("fossillist.txt","w")
for line in newlist:
    f.write(line)
    
f.close()