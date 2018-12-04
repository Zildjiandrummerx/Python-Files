#!/usr/bin/python3

def vendingmachine ():
    totalCoins = 0
    coins = 0 
    finished = False
    accetableCoins = [0,10,20,50,100]
    while finished == False:
        try:
            coins = int (input ("Please enter your coins: "))
            while coins not in accetableCoins:
                print ("Sorry, this input is not valid.")
                print ("Only 10p, 20p, 50p and 100p are accepted.")
            totalCoins = coins + totalCoins
        except ValueError:
            print ("The value you have entered is not acceptable.")
            print ("Please try again.")
            coins = int (input ("Please enter your coins: "))
            while coins not in accetableCoins:
                print ("Sorry, this input is not valid.")
                print ("Only 10p, 20p, 50p and 100p are accepted.")
                coins = int (input ("Please enter your coins: "))  
        if coins == 0:
            finished = True
    print ("Your input has been accepted.")
    print ("You now have {0}p in your bank.".format (totalCoins))
    print ("You now need to choose your product(s)")
    print ("")
    # Now we need to print the PRODUCT LIST:
    print ("Here are the items you can purchase: ")
    print ("0. Item 1  -  Cost:  60p")
    print ("1. Item 2  -  Cost:  70p")
    print ("2. Item 3  -  Cost:  55p")
    print ("3. Item 4  -  Cost:  80p")
    print ("4. Item 5  -  Cost:  45p")
    print ("5. Item 6  -  Cost:  30p")
    print ("")
    