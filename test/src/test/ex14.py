# let's do 1 ex input & argv together to ask the user something specific
from sys import argv

script, user_name = argv #we make a variable,prompt.h
prompt = '>'  # will use input diffrently by print it a simple > prompt .

print("Hi{user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes =input(prompt)

print(f"where do you live { user_name}?")
lives =input(prompt)

print("what kind of computer do you have?")
computer =input(prompt)
print(f"""
 Alright,so you said {likes} about liking me.
 you live in {lives}. Not sure where that is.
 And you have a {computer} computer. Nice.""")



