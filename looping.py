# TODO: Ask the user by name if they understand Python while loops
# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops. 
# TODO: Outside the while loop, congratulate the user for understanding while loops
 
name = input("What's your name? ")
answer = input("{}, do you understand Python while loops?\n(Enter yes/no): ".format(name))

while answer.lower() != 'yes':
    print("Ok, {}, Some...Explanation...".format(name))

    answer = input("{}, now do you understand Python while loops?\n(Enter yes/no): ".format(name))    

print("Congratulations, {}! You are now ready to code!".format(name))