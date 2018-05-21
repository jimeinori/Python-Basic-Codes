#String methods let you perform specific tasks for strings.

'''

    len() - gets the length (the number of characters) of a string.
    lower() - you can use this to get rid of all the capitalization.
    upper() - makes your string all in capital letters.
    str() -  turns non-strings into strings.
'''

#len() example:
dog = "Chow Chow"
print("Dog: " + str(len(dog)) + " characters.")

#lower() example:
fish = "Bank Sea Bass"
print("Fish: " + fish.lower())

#upper() example:
meal = "adobong manok"
print("Meal: " + meal.upper())

#str() example:
yourmoney = 100.25
print("Your money: " + str(yourmoney))


'''
DOT NOTATION:
Methods that use dot notation only work with strings.

On the other hand, len() and str() can work on other data types.
'''

#String Formatting with %
'''
When you want to print a variable with a string,
there is a better method than concatenating strings together.
'''
#example1:
name = "Elliot"
print("Hello %s!" % (name))
'''
The % operator after the string is used to combine
a string with variables. The % operator will replace
the %s in the string with the string variable that comes after it.

If you'd like to print a variable that is an integer,
you can "pad" it with zeros using %02d.
The 0 means "pad with zeros", the 2 means to pad to 2 characters wide,
and the d means the number is a signed integer (can be positive or negative).
'''

#example2:
day = 12
print("03 - %s - 1998" % (day))
print("03 - %02d - 1998" % (day))

#example3:

string_1 = "mess"
string_2 = "hungry"

print("My life is a %s! 'Or maybe, I'm just %s." % (string_1, string_2))
#The first string you've set also will be the first string to be printed.

print("---------------------")
input("Press ENTER to exit.")
