# Activities & Practices

# 1st Activity about write your letter on console
print("1st Activity")
print("First three letters from your name are: ")
print("------------------")
print("M   M    OOO    BBBB  ")
print("MM MM   O   O   B   B ")
print("MM MM   O   O   B   B ")
print("M M M _ O   O _ BBBB  ")
print("M   M   O   O   B   B ")
print("M   M   O   O   B   B ")
print("M   M    OOO    BBBB  ")
print("------------------")
print("Mohammad Omar Bawakid  :)")

print("-----------------------------------------------------")

# 2nd Activity "Receipts for Lovely Loveseats"
# In the Activity, we'll be storing the names and prices
# of a furniture store's catalog in variables. You'll then
# process the total price and item list of customers,
# printing them to the output terminal. [simple version app]
print("2nd Activity")

lovely_loveseat_description = "Loveley Loveseat. Tufted polyster blend on wood bla bla bla.. | "
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high bla bla bla.. | "
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. | "
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0 
customer_one_itemization = ""

customer_one_total = customer_one_total + lovely_loveseat_price
customer_one_itemization = customer_one_itemization + lovely_loveseat_description

customer_one_total = customer_one_total + luxurious_lamp_price
customer_one_itemization = customer_one_itemization + luxurious_lamp_description

customer_one_total = customer_one_total + stylish_settee_price
customer_one_itemization = customer_one_itemization + stylish_settee_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total = customer_one_total + customer_one_tax

print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)