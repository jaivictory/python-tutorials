# None object is returned by any function that dosen't explicity return '
def some_func():
    print('hii')
var = some_func()
print(var)


foo =print()
if foo == None :
    print(1)
else:
    print(2)

# dictionaries are data structure used to map  arbitrary keys to value
ages = {"Dave":24, "Mary":42,"john":58}
print(ages["Dave"])
print(ages["Mary"])
# dictionaries:trying to index a key that is not a part of the dictionaries return a KeyError



primary ={
    "red":[255, 0, 0],
    "green":[0, 255, 0],
    "blue":[0, 0, 255],
}
print(primary["red"])
print(primary["yellow"])


test = {}
print(test[0])


