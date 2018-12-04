# I need you to make a function named word_count. It should accept a single argument 
# which will be a string. The function needs to return a dictionary. The keys in the 
# dictionary will be each of the words in the string, lowercased. The values will be 
# how many times that particular word appears in the string.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(arg):
# you should lower case the string and split it into separate words
# split will create a list with separated words and you can loop over every single one
# and count how many identical words are in the list
    split = arg.lower().split()
    dictionary = {}
# loop over the list of separated words and split.count()
# will count how many times a special word is encountered in the list
    for key in split:
        dictionary[key] = split.count(key)
    return dictionary

string = input("Enter a long sentense: ")
print(word_count(string))