import os

# Create a new empty list named shopping_list
shopping_list = []

# Function that helps clean the screen after each interaction
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Create a function name add_to_list that declares a parameter named item
    # Add the item to the list
def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press enter to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position -1, item) 
    else:
        shopping_list.append(item)
    
    show_list()

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help menu.
Enter 'SHOW' to display all items on the list.
Enter 'REMOVE' to delete an item from your list.
""")

# Define a function named show_list that print all the items in the list
def show_list():
    clear_screen()
    print("Here's your list: ")

    for index, item in enumerate(shopping_list):
        print(" {}. {}".format(index+1, item))
    print("-" * 10)

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        # Call add_to_list with new_item as an argument
        add_to_list(new_item)

show_list()