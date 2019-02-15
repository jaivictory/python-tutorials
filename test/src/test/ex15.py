#line 1-3 use argv to get a filename .
from sys import argv
script, filename = argv
#line 5 use a new command,open right now you just openerd a file takes parameter.
file = open(filename)
#line 7 just a little msg ,on line 8 we call a function on txt named read.
print(f"Here is your file {filename}:")
print(file.read())#file.read()says that,"hey file!Do you read command with no parameter

print("Type the filename again:")
file_again =input(" # ")

txt_again = open(file_again)

print(txt_again.read())



