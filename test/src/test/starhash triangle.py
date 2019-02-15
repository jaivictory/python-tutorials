n = 6
for j in range(1, n+1):
    for i in range (1, j+1):
        print("*" ,end=" ")
    print()
    length = 6
for x in range(1, length + 1):
 print(x * '*'+(length - x )* '#')


string = input("enter the string:")
length = len(string)
for row in range(length):
    for col in range (row +1):
        print(string[col],end=" ")
    print()