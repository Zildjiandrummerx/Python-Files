# Create a function named first_4 that returns the first four items 
# from whatever iterable is given to it.

def first_4(list):
    return list[0:4]

# Make a new function named first_and_last_4. It'll accept a single 
# iterable but, this time, it'll return the first four and last four 
# items as a single value.

def first_and_last_4(single):
    return single[:4] + single[-4::1]

# create a new function named odds that returns every item with an odd 
# index in a provided iterable. For example, it would return the items 
# at index 1, 3, and so on.

def odds(items):
    return items[1::2]

# Make a function named reverse_evens that accepts a single iterable as 
# an argument. Return every item in the iterable with an even index...in reverse.
# For example, with [1, 2, 3, 4, 5] as the input, the function would return [5, 3, 1].

def reverse_evens(iterable):
    return iterable[::2][::-1]