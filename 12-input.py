'''
raw_input():
If the prompt argument is present,
it is written to standard output without a trailing newline.
The function then reads a line from input,
converts it to a string (stripping a trailing newline), and returns that.
In Python 3, raw_input() was renamed as input().
'''
#raw_input() example:
name = input("What is your name? ")
course = input("What is your course? ")
age = input("And, your age is? ")

print("Hello there! So, your name is %s, your course is %s, "
      "and you're age is %s." % (name, course, age))
print("---------------------")
input("Press ENTER to exit.")
