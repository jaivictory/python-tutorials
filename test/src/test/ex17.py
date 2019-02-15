# this example teach you py script to copy one file to another.
from sys import argv
# we import another handy command named exists,this returns true if file exists
#and false if file dosen't exist
from os.path import exists
script, from_file, to_file = argv

print(f" coping from {from_file} to {to_file} ")

# we could do this two or one line , how ?
in_file = open(from_file)
indata =in_file.read()

print(f"The input file is{len(indata)} bytes long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready , hit return to continue,CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)
print('Alright, all done.')
out_file.close()
in_file.close()