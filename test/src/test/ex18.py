# This one is like your scripts with arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

    # ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

    # this just take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this take no arguments
def print_none():
    print("i got nothing'.")

print_two("hot", "cold")
print_two_again("high","low")
print_one("first")
print_none()