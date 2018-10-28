#==================={Conditions/ControlFlow}=====================#

'''
AND:
1) True AND True = True
2) True AND False = False
3) False AND True = False
4) False AND False = False
--------------------------
OR:
1) True OR True = True
2) True OR False = True
3) False OR True = True
4) False OR False = False
--------------------------
NOT:
1) A = True | NOT A = False
2) A = False | NOT A = True 

Boolean operators aren't just evaluated from left to right.
Just like with arithmetic operators,
there's an order of operations for boolean operators:

1. not - evaluated first
2. and - evaluated after not
3. or - evaluated last

'''

# and - a boolean operator that returns TRUE when expressions on both sides of and are true.

1 < 2 and 2 < 3 # True
1 < 2 and 2 > 3 # False

# EXAMPLES

condition_one = 1 > 10 and 2 < 1 # False AND False
print(condition_one)

condition_two = 1 == -4 and 4 >= 16 ** 0.5 # False AND True
print(condition_two)

condition_three = 19 % 4 != 300 / 10 / 10 and 20 % 5 == 1 + 11 # True AND False
print(condition_three)

condition_four = -(1 ** 2) < 2 ** 10 and 10 % 10 <= 20 - 10 * 2 # True AND True
print(condition_four)

condition_five = 2 ** 0 != 2 and 10 / 5 == 1 + 1 # True AND True
print(condition_five)
print("------------------------------")

'''
Example for multiple boolean operators
1. False or not True and True == False
2. False and not True or True == True
3. True and not (False or False) == True
4. not not True or False and not True == True
5. False or not (True and True) == False

Check the given demonstration below.
'''
print('Multiple boolean Operators Demonstration:')

first_condition = False or not True and True 
print('1. False or not True and True = ' + str(first_condition))

second_condition = False and not True or True
print('2. False and not True or True = ' + str(second_condition))

third_condition = True and not (False or False)
print('3. True and not (False or False) = ' + str(third_condition))

fourth_condition = not not True or False and not True
print('4. not not True or False and not True = ' + str(fourth_condition))

fifth_condition = False or not (True and True)
print('5. False or not (True and True) = ' + str(fifth_condition))
