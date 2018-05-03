'''
In Python, and when programming in general,
we need to build systems for dealing with data
that changes over time. That data could be the
location of a plane, or the time of day, or the
television show you're currently watching.
The only important thing is that it may be
different at different times. Python uses variables
to define things that are subject to change.
'''

#Variable with a string value
greeting_message = "Welcome, Max!"

#Variable with an int value
current_exercise = 100

#Sample printing of variables with assigned values.
print(greeting_message)
print(current_exercise)
print("-------------")

#Updating Variables
#Example No.1
fish_in_clarks_pond = 50
print("Catching fish")
print("Current fish in Clarks Pond: 50")
print("Fish caught in Clarks Pond: 10")
number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught
print("Remaining count:")
print(fish_in_clarks_pond)
print("-------------")
'''
In the above example, we start with 50 fish in a local pond.
After catching 10 fish, we update the number of fish in
the pond to be the original number of fish in the pond
minus the number of fish caught. At the end of this code
block, the variable fish_in_clarks_pond is equal to 40.
'''
#Example No.2
money_in_wallet = 40
print("Current money in wallet: 40")
sandwich_price = 7.50
print("Sandwich Price: 7.50")
sales_tax = .08 * sandwich_price
print("Sales Tax: 0.08")
sandwich_price += sales_tax
'''
+= and -= operations will add the represented
variable to the equivalent variable,
and then the output will be the
new value of the represented variable.
+= goes for addition, and -= goes for subtraction.
'''
money_in_wallet -= sandwich_price
print("Sandwich Price with Tax:")
print(sandwich_price)
print("Current money in wallet after buying a sandwich:")
print(money_in_wallet)
'''
In the above example, we use the price of a sandwich
to calculate sales tax. After calculating the tax we
add it to the total price of the sandwich. Finally,
we complete the transaction by reducing our
money_in_wallet by the cost of the sandwich (with tax).
'''

#Credits to Codecademy!
