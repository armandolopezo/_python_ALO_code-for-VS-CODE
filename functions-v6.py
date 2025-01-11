"""
Mixing arguments and keyword arguments
Sometimes, a function needs a combination of arguments and keyword arguments. 
In Python, this combination follows a specific order. Arguments are always declared first, followed by keyword arguments.

Update the arrival_time() function to take a required argument, which is the name of the destination:
"""
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

"""
arrival_time()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: arrival_time() missing 1 required positional argument: 'destination'

"""
# The function now requires a destination argument.
# The destination argument is a required positional argument.
# The hours argument is a keyword argument with a default value of 51.
# The function calculates the arrival time based on the current time and the hours argument.
# The function returns the arrival time in the specified format.
# The function call without the destination argument raises a TypeError.
# The function call with the destination argument returns the arrival time.

arrival_time("Moon")
print(arrival_time("Moon"))
# Moon Arrival: Monday 06:45 (example output)

arrival_time("Orbit", hours=0.13)
print(arrival_time("Orbit", hours=0.13))



