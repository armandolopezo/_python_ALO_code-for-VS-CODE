"""
Use function arguments in Python
Now that you know how to create a function with no inputs, the next step is to create functions that require an argument. 
Using arguments makes functions more flexible, because they can do more and conditionalize what they do.

Requiring an argument
If you're piloting a rocket ship, a function without required inputs is like a computer with a button to tell you the time. 
If you press the button, a computerized voice tells you the time. But a required input can be a destination to calculate travel distance.
Required inputs are called arguments to the function.

To require an argument, put it within the parentheses:
"""
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
# distance_from_earth()
# Output: TypeError: distance_from_earth() missing 1 required positional argument: 'destination'
distance_from_earth("Moon")
# Output: '238,855'
print(distance_from_earth("Moon"))
distance_from_earth("Saturn")
# Output: 'Unable to compute to that destination'
print(distance_from_earth("Saturn"))


