planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
print(planet_moons)
"""
Obtain a list of moons and number of planets
Python dictionaries allow you to retrieve all the values and keys by using the values and keys methods, respectively.
 Each method returns a list containing the data, which can then be used like a regular Python list. You can determine the number
   of items by using len, and iterate through it by using for loops. In the dictionary you created, the planet names are keys 
   and the number of moons are the values.

Start by retrieving a list with the number of moons, and store this in a variable named moons. Then obtain the total number of planets and store that value in a variable named total_planets.
"""
moons = planet_moons.values()
print(planet_moons.keys())
print(moons)
total_planets = len(planet_moons.keys())
print(f" total planets:  {total_planets}")
"""
Determine the average number of moons
You will finish this exercise by determining the average number of moons. Start by creating a variable named total_moons;
 this will be your counter for the total number of moons. Then add a for loop to loop through the list of moons, adding each value to total_moons. 
Finally, calculate the average by dividing total_moons by total_planets and displaying the value.
"""
# Each planet has an average of 17.833333333333332 moons
total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')
# Each planet has an average of 17.833333333333332 moons

