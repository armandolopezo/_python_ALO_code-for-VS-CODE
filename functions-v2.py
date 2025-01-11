"""
Required and optional arguments
---------------------------------
In Python, several built-in functions require arguments. Some built-in functions make arguments optional. 
Built-in functions are immediately available, so you don't need to import them explicitly.

An example of a built-in function that requires an argument is any(). This function takes an iterable (for example, a list)
 and returns True if any item in the iterable is True. Otherwise, it returns False.
"""
print(any([True, False, False]))

print(any([False, False, False]))
# The any() function returns True if any item in the iterable is True. Otherwise, it returns False.
# The any() function is a built-in function in Python that requires an argument.
# the following line of code IF EXECUTED  will raise an error because the any() function requires an argument. 
# 
# any()
#
"""
You can verify that some functions allow the use of optional arguments by using another built-in function called str().
 This function creates a string from an argument. If no argument is passed in, it returns an empty string:
"""
str()
# The str() function is a built-in function in Python that allows the use of optional arguments.
print(str())
# The str() function returns an empty string when no argument is passed in.
str(15)
# The str() function returns a string representation of the number 15.
print(str(15))


