# Knowing the total cost that a customer makes at the supermarket and the amount
# of money with which he/she is paying, calculate and show the change.

def sale():
    price_product = float(input("Enter the product's price: $"))
    amount_paid = float(input("Enter the amount paid by the customer: $"))
    
    if price_product and amount_paid != float:
        print("Please enter numeric values only. Decimals are also accepted.")
    else:
        total_change = price_product - amount_paid
        print("Your change is ${} USD.".format(float(abs(total_change))))

sale()