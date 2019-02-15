#we put end=' ' at the end of each print line.
#this tells print not to end the line with a newline character and go to the next line.
print("How old are you? ", end=' ')
#python provides the function input()
#input can come in various ways for ex from database,another computers or mouse clicks etc
age = input()
print("How tall are you?", end=' ')
height=input()
# input has an optional parameter,which is the prompt string.
print("how much weight you have?", end=' ')
weight=input()

print(f"so you are {age} years old, {height} tall and {weight} heavy.")
print("Name :" , end=' ')
name =input()
print("Profession :" , end=' ')
profession = input()
print("Nationality:" , end=' ')
nationality = input()
print(f"congratulations!{name}, you won a prize to visit a zoo .")
print("what is your favourite place :" , end=' ')
place = input()
vehicles = ("aeroplane/train/ship/bus")
print("how would you like to go: " ,end=' ')
print(vehicles)
vehicle = input()
print(f"Ok, so {name} we are going to book a {vehicle} ticket to {place} on coming friday. ")

quit()