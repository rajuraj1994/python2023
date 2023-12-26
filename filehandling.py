myfile=open('test.txt')
print(myfile)

# read the file content
print(myfile.read())

# if you want to print the paragraph starting from certain index number then do this
myfile.seek(5)
print(myfile.read())

# readlines: it will return the list of the lines in the file
myfile.seek(0)
print(myfile.readlines())
myfile.close()

# to write to an existing file
wfile=open('test.txt','w')
print(wfile)
wfile.write('there is new content in the file')
wfile.close()

# create a new file using w if the file is not exist 
newfile=open('try.txt','w')
print(newfile)
newfile.write('this is the first line added from program')
newfile.write('\nthis is the another line added from python')
newfile=open('try.txt','r')
newfile.seek(0)
print(newfile.read())

# append(a) -> this will create the new file 
# open('filename.ext','a+')


# delete a file 
import os
os.remove('hello.txt')






