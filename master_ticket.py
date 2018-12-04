# Run this code continously until we run out of tickets
# Output how many tickets are remaining using the tickets_remaining variable
# Gather the user's name and sign it to a new variable
# Prompt the user by name and ask how many tickets they'd like
# Calculate the price (number of tickets multiplied by the price) and assign it to a variable
# Output the price to the screen
# Prompt user if they want to proceed. Y/N?
# If they want to proceed print to the screen SOLD! to confirm the purchase
# Notify the user that the tickets are sold out :(
# Expect a ValueError to happen and handle it appropiately...remember to test it out!
# Raise a ValueError if the request is for more tickets than are available
# Include the error text in the output
# Create the calculate_price function. It takes number of tickets and returns: how_many * TICKET_PRICE
# Create a new constant for the $2 service charge
# Add the service charge to the result

SERVICE_CHARGE = 2
TICKET_PRICE = 10 
tickets_remaining = 100


def calculate_price(how_many):
    return how_many * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining...".format(tickets_remaining))
    print("Price per ticket: ${}".format(TICKET_PRICE))

    try:
        name = input("What is your name? ")
        how_many = int(input("How many tickets would you like to purchase, {}? ".format(name)))
        
        if how_many > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    
    except ValueError as err:
        print("Oh, no! We ran into an issue. {}. Please try again: ".format(err))

    else:
        price = calculate_price(how_many)
        print ("Your total for {} tickets is: ${} USD.".format(how_many, price))
        answer = input("Would you like to proceed to checkout? Y/N: ")

        # TODO: Gather credit card information and process it.
        if answer.lower() == 'y':
            print("SOLD!")
            tickets_remaining -= how_many
        else:
            print("Thank you {}, please come again!".format(name))

print("Oh, no! We ran out of tickets, please come back later")