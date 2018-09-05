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

'''

# and - a boolean operator that returns TRUE when expressions on both sides of and are true.

1 < 2 and 2 < 3 # True
1 < 2 and 2 > 3 # False

# EXAMPLES

condition_one = 1 > 10 and 2 < 1 # False AND False

condition_two = 1 == -4 and 4 >= 16 ** 0.5 # False AND True

condition_three = 19 % 4 != 300 / 10 / 10 and 20 % 5 == 1 + 11 # True AND False

condition_four = -(1 ** 2) < 2 ** 10 and 10 % 10 <= 20 - 10 * 2 # True AND True

condition_five = 2 ** 0 != 2 and 10 / 5 == 1 + 1 # True AND True

