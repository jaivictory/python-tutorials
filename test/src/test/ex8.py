#take the formatter string defined on line
formatter = "{} {} {} {}"

#format function,which tells to do a command line command named format
print(formatter.format(1 , 2, 3, 4))

#pass to format four arguments which matches 4{}s in the formatter variable
print(formatter.format("one","two","three","four"))

#this is like passing arguments to the command line command format
print(formatter.format(True, False, True,False))
#result of caling format on formatter is a new string that{} replaced with the 4 variables
print(formatter.format(formatter, formatter , formatter, formatter))
# so this is what we print is now printing out

print(formatter.format(
    "Learn everyday for 15 minutes something new",
    "what happened when you learn something new",
    "you experience something new",
    "the novelty centre of your brin got activated.",
))

























