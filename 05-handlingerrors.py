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

#Reference: Codecademy
