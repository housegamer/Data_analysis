#Reading files
f = open('inputFile.txt','r')
#to pass the pass a file
passFile = open('PassFile.txt','w')
#to pass a fail file
failFile = open('FailFile.txt','w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)
f.close()

