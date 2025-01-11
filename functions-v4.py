"""
Multiple required arguments
To use multiple arguments, you must separate them by using a comma.
 Let's create a function that can calculate how many days it takes to reach a destination, given distance and a constant speed:
"""
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
days_to_complete(238855, 75)
print(days_to_complete(238855, 75))
"""
Functions as arguments
You can use the value of the days_to_complete() function and assign it to a variable, and then pass it to round() 
(a built-in function that rounds to the closest whole number) to get a whole number:
"""
total_days = days_to_complete(238855, 75)
round(total_days)
print(round(total_days))
round(days_to_complete(238855, 75))
print(round(days_to_complete(238855, 75)))
