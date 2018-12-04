# The function disemvowel takes a single word as a parameter and 
# then returns that word at the end.
# I need you to make it so, inside of the function, all of the 
# vowels ("a", "e", "i", "o", and "u") are removed from the word. 
# Solve this however you want, it's totally up to you!
# Be sure to look for both uppercase and lowercase vowels!

def disemvowel(word):
    result = ''
    for letter in word:
        if letter.lower() not in 'aeiou':
            result += letter
    return result

word = input("Enter any word: ")
print(disemvowel)
