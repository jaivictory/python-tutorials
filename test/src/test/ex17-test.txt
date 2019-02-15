from sys import argv

script, filename = argv

print(f"if we are going to erase {filename}.")
print(f"if you d'ont want that, hit ctrl-c(^C).")
print(f"if you d'ont want that, hit return.")

input("?")

print("opening the files.....")
target = open(filename,'w')

print("Truncating the file.Goodbye:")
target.truncate()

print("now i am going to ask you three lines.")

line1 = input("line 1 :what is your name?")
line2 = input("line 2 :how old are you?")
line3 = input("line 3 :where do you live")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it.")
target.close()
