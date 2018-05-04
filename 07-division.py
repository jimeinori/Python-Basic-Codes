'''
In Python 2, when we divide two integers,
we get an integer as a result.
When the quotient is a whole number, this works fine:
ex: quotient = 6/2
The value of quotient is now 3, which makes sense
'''

'''
However, if the numbers do not divide evenly,
the result of the division is truncated into an integer.
In other words, the quotient is rounded down to a whole number.
This can be surprising when you expect to receive
a decimal and you receive a rounded-down integer:
ex: quotient = 7/2
the value of quotient is 3,
even though the result of the division here is 3.5
'''

'''
To yield a float as the result instead,
programmers often change either the
numerator or the denominator (or both) to be a float:
ex: quotient1 = 7./2
the value of quotient1 is 3.5
ex: quotient2 = 7/2.
the value of quotient2 is 3.5
ex: quotient3 = 7./2.
the value of quotient3 is 3.5
'''

#Code Example:
#Without Remainder
item_count = 200
distribution_count = 10
item_per_distribution = item_count / distribution_count
print(item_per_distribution)

#With Remainder
item_count_2 = 250
distribution_count_2 = 30
item_per_distribution_2 = item_count_2 / distribution_count_2
print(item_per_distribution_2)

#Reference: Codecademy
# :)
