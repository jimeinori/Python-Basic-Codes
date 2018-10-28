#==================={Conditions/ControlFlow}=====================#
'''
The same with the 14-conditions.py
IF syntax will be like this:

if the_function() or statement:
    # line one
    # line two
    # line three

Depends on how you would implement the IF condition.
But by default, IF will execute the following lines
if the_function() or statement will return True.
See the demonstration code below.
'''
#EXAMPLE 1
def first_function():
    if 1 + 1 == 2:
        return "The statement is TRUE."
def second_function():
    if not True or True == True and True:
        return "The statement is TRUE again."
def third_function():
    if 7 > 100 == True:
        return "The statement is TRUE!"

print(first_function())
print(second_function())
print(third_function())

'''
You see how the third_function()'s output?
It says "None" because the condition given
did not return True. 
'''
