"""
Work with arguments in functions
Required arguments in functions are used when functions need those arguments to work properly. 
In this exercise, you'll construct a fuel report that requires information from several fuel locations throughout the rocket ship.
"""
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)
"""
Use keyword arguments in Python - OPTIONAL ARGUMENTS
Optional arguments in functions are used when functions can work without them.
Keyword argument values must be defined in the functions themselves.
 When you're calling a function that's defined with keyword arguments, it isn't necessary to use them at all.
"""
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
print(" ***************** ")
arrival_time()
print(arrival_time())

arrival_time(hours=0)
print(arrival_time(hours=0))

