import sys
# asks the user to enter their input as an integer with 1 corresponding to water, 2 corresponding to cola, and 3
# corresponding to gatorade. Note that int() is used to change the user's input (which is a string) to an integer.
order = int(input("Enter your order number as an integer. (1, 2, or 3)"))
if order == 1:
 # water is $1.00, thus a variable, disPrice is created and assigned 1.00 if the user enters 1 for water
 disPrice = 1.00
elif order == 2:
 # cola is $1.50
 disPrice = 1.50
elif order == 3:
 # gatorade is $2.00
 disPrice = 2.00
else:
 # ends the program and prints the message "Please try again." if order does not equal 1, 2, or 3
 sys.exit("Please try again.")
# 2.
# the amount of each coin the user puts in: note that int() is used to convert the user's input (which is a string) to
# an integer
quarters = int(input("Enter the number of quarters as an integer."))
dimes = int(input("Enter the number of dimes as an integer."))
nickels = int(input("Enter the number of nickels as an integer."))
pennies = int(input("Enter the number of pennies as an integer."))
# 3.
# variable that holds the total value of all the coins the user has put into the vending machine.
total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
# 4.
if total >= disPrice:
 # the .2 in %.2f means that the float that is replacing the %f placeholder will be displayed to 2 places after the
 # decimal place (eg 0.00). The (total - disPrice) gets the user's change by getting the difference of the amount
 # the user put in and the cost of the item they ordered from the vending machine.
 print("Your change is $" + "%.2f" % (total - disPrice) + ". Have a nice day.")
else:
 # prints "Please try again." if total < disPrice
 print("Please try again.")
