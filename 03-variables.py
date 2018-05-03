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
greeting_message = "Welcome, Human!"

#Variable with an int value
current_lifespan = 100

#Sample printing of variables with assigned values.
print(greeting_message)
print(current_lifespan)
print("-------------")

#Updating Variables
#Example No.1
fish_in_mother_pond = 50
print("Catching fish")
print("Current fish in Mother Pond: 50")
print("Fish caught in Mother Pond: 10")
number_of_fish_caught = 10
fish_in_mother_pond = fish_in_mother_pond - number_of_fish_caught
print("Remaining count:")
print(fish_in_mother_pond)
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
hamburger_price = 7.50
print("Hamburger Price: 7.50")
sales_tax = .08 * hamburger_price
print("Sales Tax: 0.08")
hamburger_price += sales_tax
'''
+= and -= operations will add the represented
variable to the equivalent variable,
and then the output will be the
new value of the represented variable.
+= goes for addition, and -= goes for subtraction.
'''
money_in_wallet -= hamburger_price
print("Hamburger Price with Tax:")
print(hamburger_price)
print("Current money in wallet after buying a hamburger:")
print(money_in_wallet)
'''
In the above example, we use the price of a hamburger
to calculate sales tax. After calculating the tax we
add it to the total price of the hamburger. Finally,
we complete the transaction by reducing our
money_in_wallet by the cost of the hamburger (with tax).
'''

#Reference: Codecademy
# :)
