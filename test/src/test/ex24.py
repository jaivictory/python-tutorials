print("Let's practice everything.")
print('You\'d need to know \'but escapes with \\ that do:')
print('\n newline and \ttabs.')

poem = """
    /tThe lovely world
    with logic so firmly planted
    cannot discern \n the needs of love
    nor comprehend passion from intution
    and requires an explanation
    \n\t\twhere there is none.
    """

print("--------")
print(poem)
print("--------")


five = 10 - 2 + 3 - 6
print(f"this shoud be five : {five}")

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember this is the another way to format a string
print("with  a starting_point of: {}" .format(start_point))
# it's just like with an f"" string
print(f"We'd have{beans}beans, {jars}jars, and {crates}crates")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to appply a list to a format string
print("we'd have {} beans, {}jars, and {} crates.".format(*formula))



