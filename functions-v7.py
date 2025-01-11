"""
Use variable arguments in Python
In Python, you can use any number of arguments and keyword arguments without declaring each one of them. 
This ability is useful when a function might get an unknown number of inputs.

Variable arguments
Arguments in functions are required. But when you're using variable arguments, the function allows any number of arguments 
(including 0) to be passed in. The syntax for using variable arguments is prefixing a single asterisk (*) before the argument's name.

The following function prints the received arguments:
"""
def variable_length(*args):
    print(args)

variable_length()
()
variable_length("one", "two")
('one', 'two')
variable_length(None)
(None,)
"""
A rocket ship goes through several steps before a launch. Depending on tasks or delays, these steps might take longer than planned. 
Let's create a variable-length function that can calculate how many minutes until launch, given how much time each step is going to take:
"""
print(" ***** ")
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
sequence_time(4, 14, 18)
print(sequence_time(4, 14, 18))

sequence_time(4, 14, 48)
print(sequence_time(4, 14, 48))


    
