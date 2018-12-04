# I need you to create a new function for me. This one will be named sillycase and 
# it'll take a single string as an argument. sillycase should return the same string 
# but the first half should be lowercased and the second half should be uppercased.

# For example, with the string "Treehouse", sillycase would return "treeHOUSE".
# Don't worry about rounding your halves, but remember that indexes should be integers. 
# You'll want to use the int() function or integer division, //.

def sillycase(string):
    string_lower = string[:(len(string)//2)].lower()
    string_upper = string[:(len(string)//2)].upper()
    return (string_lower + string_upper)

