# TODO Create an empty list to maintain the player names
# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
# TODO print the number of players on the team
# TODO Print the player number and the player name
# The player number should start at the number one
# TODO Select a goalkeeper from the above roster
# TODO Print the goal keeper's name
# Remember that lists use a zero based index

players = []
add_players = input("Would you like to add a player to the list? (Yes/No): ")
while add_players.lower() == 'yes':
    name = input("\nEnter the name of the player to add to the team: ")
    players.append(name)
    add_players = input("Would you like to add another player? (Yes/No): ")

print("\nThere are {} players on the team.".format(len(players)))

player_number = 1
for player in players:
    print("Player {}: {}".format(player_number, player))
    player_number += 1

keeper = input("Please select the goal keeper by selecting the player number. (1-{}): ".format(len(players)))
keeper = int(keeper)
print("Greeat!! The goalkeeper for the game will be {}".format(players[keeper -1]))
