"""
Functions with no arguments
To create a function, you use the def keyword followed by a name, parentheses, and then the body with the function code:

def rocket_parts():
    print("payload, propellant, structure")

    In this case, rocket_parts is the name of the function. That name is followed by the empty parentheses, 
    which indicate that no arguments are needed. Last is the code, indented with four spaces. 
    To use the function, you must call it by its name by using parentheses:
"""
def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()
"""
The rocket_parts() function doesn't take any arguments and prints a statement. 
If you need to use a value that a function is returning, you can assign the function output to a variable:
"""
output = rocket_parts()
print(f"printing variable output: {output}")
# None
"""
The line output is None is a conditional statement in Python that checks whether the variable output
 is currently set to None. In Python,
   None is a special constant that represents the absence of a value or a null value.
     It is often used to signify that a variable has not been initialized or that it explicitly has no value.
     The is keyword in this statement is used for identity comparison. This means that output is None checks
       if output and None are the same object in memory. This is different from using the == operator, 
       which checks for value equality rather than identity. Using is for comparison with None is the
         recommended practice in Python because None is a singleton, meaning there is only one
           instance of None in a Python runtime.
This type of check is common in Python code to determine if a variable has been assigned a meaningful 
value or if it remains in its default, uninitialized state. For example, you might see this check 
before performing operations that require output to have a valid value, ensuring that the code does
 not run into errors due to output being None. This helps in writing robust and error-free code by
   handling cases where a variable might not have been set to a proper value before its usage.
"""
question1 = output is None
print(question1)
print(" ************ ")
print(output is None)
# True




