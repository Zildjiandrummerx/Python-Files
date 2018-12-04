# Let's play with the *args pattern.
# Create a function named multiply that takes any number of arguments. 
# Return the product (multiplied value) of all of the supplied arguments. 
# The type of argument shouldn't matter.

def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(multiply())