#Now, let's focus on handling errors in Python!
'''
If the quotes are mismatched Python will notice them
and inform you that your code has an error
in its syntax because the line ended (called an EOL)
before the double-quote that was supposed to close the string appeared.
'''
#SyntaxError: EOL while scanning a string literal
#Ex: "How do you make a hotdog stand?'
'''
This means that a string wasn't closed,
or wasn't closed with the same quote-character that started it.
'''
print("How do you make a hotdog stand?")
print('You take away its chair!')
print("------------------------------")

'''
ValueError: Python automatically assigns a variable
the appropriate datatype based on the value it is given.
Sometimes we will want to convert variables to different datatypes.
For example, if we wanted to print out an integer as part
of a string, we would want to convert that integer to a string first.
We can do that using str().
'''
#Ex: int to str

age = 25
print("I am " + str(age) + " years old.")

'''
If we want to perform arithmetic operations on a string
with a numerical value, we must convert it to a
numeric datatype. We can do this using int().
'''
#Ex: str to int

number1 = "50"
number2 = "150"

string_addition = number1 + number2
int_addition = int(number1) + int(number2)
print("sum as string: " + string_addition)
print("sum as converted int: " + str(int_addition))

'''
If you use int() on a floating point number,
it will round the number down.
To preserve the decimal, you can use float().
But as per Python 3.5.2 documentation, int() expects
an number or string that contains an integer literal.
Meaning int() can only convert strings that contain integers.
'''

string_num = "5.5"
# This will not work on Python3: print(int(string_num))
# For this to work, use float() inside int().
print(int(float(string_num)))
print(float(string_num))

#Reference: Codecademy + Stackoverflow
# :)
