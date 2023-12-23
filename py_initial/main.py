#code to import modules and vars from modulesß
from first import *
import functions.func1 as f1
import functions.func2

f1.func()
print("\nValue pulled from another file",i)
functions.func2.func()
print("\nThis is main file")

#I/O operations for opening or outputting to txt or other format files
#1. Read content of a file n print it out
file1=open("nodejs_data_files/example_input_data_1.data",'r')
print("\nReading content from txt file:\n===============\n",file1.read(),"\n===============\n")

f=open("nodejs_data_files/example_input_data_1.data",'r')
print("\n\nTrying to sort the content of the file\n\n")

file=f.read()
print(file)
print("\n\n\n\n")


#2. Write content into a file, read it n print it out
f2=open("test2.txt",'w')
content="sample content to be placed in a txt file"
f2.write(content)
f2.close()
f2=open("test2.txt",'r')
print("\nReading content from 2nd txt file:\n===============\n",f2.read(),"\n===============\n")

#3. Handling I/O errors
try:
    f3=open("test3.txt",'r')
    print(f3.read())
except FileNotFoundError:
    print("Attempted file is not present at designated location")
except IOError:
    print("Issue looks to be with File Permissions. Check that!")