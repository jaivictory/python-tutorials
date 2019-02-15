j = 9
for i in range(1, 10, 2 ):
    star= '*' if j%2==0 else'#'
    print(' ' * j + i *  star)
    j = j - 1


