#==================={Conditions/ControlFlow}=====================#
'''

You probably know this at this point.
The else statement 'complements' the if statement.
Example format:

if the_function() or statement:
    # line one
    # line two
    # line three
else
    # line one
    # line two
    # line three

'''
#EXAMPLE CODE

age = 20
output_true = "Employee's age is 20"
output_false = "Employee's age is not 20"

#1st Function
def first_employee():
    if age == 20:
        return output_true
    else:
        return output_false

#2nd Function
def second_employee():
    if age == 15:
       return output_true
    else:
      return output_false

print(first_employee())
print(second_employee())

'''

In this example, I've replaced the default True/False output
into string alternatives. I've made two strings, each one of them
represents the True output and the False output relating to the
given condition.

As obvious as it is, if the age is 20, it will return the "output_true"
if the given age within the function is not 20, it will return the 
"output_false" string.

'''
