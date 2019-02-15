max = 6
for x in range (1, max + 1):
    for y in range(1, x + 1):
        print("*", end=" ")
    print()
# integer *(string), concatenate the  string in integer times
length = 6
for x in range(1, length + 1):
 print(x * '*'+(length - x )* '#')

