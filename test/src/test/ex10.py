#\t use for tab space or print a line in a tab space.
tabby_cat ="\tI'm tabbed in"
persian_cat ="I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." # double \\ in sting gives \ backslash back.
# in triple quote string text will print as it is but \t text will print in tab space.
fat_cat = '''
I'll do a list :
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass  
'''  # /t for tab space and \n for break line & print text on next line.

#  what to print they will recall as declared above cats mentioned
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
