#==================={Conditions/ControlFlow}=====================#
'''

'elif' or else if is called in between if 
and else condition. Example format:

if the_function() or statement:
    # line one
    # line two
    # line three
else if
    # line one
    # line two
    # line three
else
    # line one
    # line two
    # line three

''' 
#EXAMPLE CODE

total_price = 500
thanksgiving = "Thank you, come again! Your change is "
invalid_change = "Insufficient Money."
error = "Cash register has stopped working. Kthnxbye"


def jollibee_receipt(customer_payment):
    change = customer_payment - total_price
    if customer_payment >= total_price:
        return thanksgiving + str(change) 
    elif customer_payment < total_price:
        return invalid_change
    else:
        return error

print(jollibee_receipt(550) + ".")
print(jollibee_receipt(400) + ".")
print(jollibee_receipt(500) + ".")

'''

Above there is just a static example code, 
you can always use a user input for it. 
As you can see in the code and its output, 
there is no error will be returned, but if you
removed the "=" comparator within the if statement,
everything's equal to total price will be an error.

You can replace the above code with this one
to try it out!
-----------------------------------------------
def jollibee_receipt(customer_payment):
    change = customer_payment - total_price
    if customer_payment > total_price:
        return thanksgiving + str(change) 
    elif customer_payment < total_price:
        return invalid_change
    else:
        return error

print(jollibee_receipt(550) + ".") #still the same
print(jollibee_receipt(400) + ".") #still the same
print(jollibee_receipt(500) + ".") #this will now return error.
-----------------------------------------------

'''
