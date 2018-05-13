'''
One thing computers are capable of doing exceptionally well
is performing arithmetic. Addition, subtraction,
multiplication, division, and other numeric calculations
are easy to do in most programming languages, and Python is no exception.
'''

addition = 10 + 10
subtraction = 10 - 5
multiplication = 5 * 2
division = 10 / 2
combinations = 5 * 2 + 500 / 10 - 10
withparentheses = 10/2*(3 + 2)

'''
Above are a number of arithmetic operations,
each assigned to a variable.
The variable will hold the final result of each operation.
'''

#Output
print("Sum:")
print(addition)
print("Difference:")
print(subtraction)
print("Product:")
print(multiplication)
print("Dividend:")
print(division)
print("Combo Finale:")
print(combinations)
print("With Parentheses:")
print(withparentheses)

'''
Python also offers a companion to division called the modulo operator.
The modulo operator is indicated by % and returns
the remainder after division is performed.
'''

odd = 15 % 2
seven = 133 % 7

'''
In the above code block, we use the modulo operator
to find the remainder of 15 divided by 2.
Since 15 is an odd number the remainder is 1.

We also check the remainder of 133 / 7.
Since 133 divided by 7 has no remainder, 133 % 7 evaluates to 0.
'''

#Output
print("-----------")
print("Modulo #1:")
print(odd)
print("Modulo #2:")
print(seven)
print("---------------------")
input("Press ENTER to exit.")
