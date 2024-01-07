

#writes a file
f=open("example.txt","w")
f.write('file is updated ')
f.close()

#append to file
f=open("example.txt","a")
f.write('and updated further')
f.close()

#READS a File
f=open("example.txt","r")
print(f.read())
f.close()