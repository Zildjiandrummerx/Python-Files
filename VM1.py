#!/usr/bin/python3

def vendingmachine ():
    count = 0
    totalCredit = 0
    coinNum = int (input ("How many coins would you like to enter: "))
    while count in range (coinNum):
        coin = float (input ("Enter Coin: $ "))
        totalCredit = totalCredit + coin
        count = count + 1
    print ("You have ${0} in your bank.".format (round(totalCredit, 2)))
    print ("")
    print ("Choose your item: ")
    print ("")
    print ("1. Item 1")
    print ("2. Item 2")
    print ("3. Item 3")
    print ("4. Item 4")
    print ("5. Item 5")
    print ("")
    finalCredit = totalCredit
    round (finalCredit, 2)
    item = int (input ("Enter the number for your item: "))
    while item <1 or item >5:
        print ("This item is not available.")
        item = int (input ("Enter the number for your item: "))
    if item == 1:
        finalCredit = totalCredit - 0.59
        print ("Here's your Item 1, Thank you for your purchase!")
        print ("You have ${0} remaining in your bank.".format (round(finalCredit, 2)))
    elif item == 2:
        finalCredit = totalCredit - 0.69
        print ("Here's your Item 2, Thank you for your purchase!")
        print ("You have ${0} remaining in your bank.".format (round(finalCredit, 2)))
    elif item == 3:
        finalCredit = totalCredit - 0.99
        print ("Here's your Item 3, Thank you for your purchase!")
        print ("You have ${0} remaining in your bank.".format (round(finalCredit, 2)))
    elif item == 4:
        finalCredit = totalCredit - 0.49
        print ("Here's your Item 4, Thank you for your purchase!")
        print ("You have ${0} remaining in your bank.".format (round(finalCredit, 2)))
    elif item == 5:
        finalCredit = totalCredit - 0.79
        print ("Here's your Item 5, Thank you for your purchase!")
        print ("You have ${0} remaining in your bank.".format (round(finalCredit, 2)))
    else:
        print ("This is not a valid option.")
    print ("")
    print ("Here's your change: , ${0}. Come back again!".format (round(finalCredit, 2)))

vendingmachine()