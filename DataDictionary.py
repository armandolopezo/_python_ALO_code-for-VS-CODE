"""
Python uses curly braces ({ }) and the colon (:) to denote a dictionary.
 You can either create an empty dictionary and add values later, or populate it at creation time.
   Each key/value is separated by a colon, and the name of each key is contained in quotes as a string literal.
     Because the key is a string literal, you can use whatever name is appropriate to describe the value.

Let's create a dictionary to store the name of the planet Earth, and the number of moons Earth has:
"""
planet = {
    'name': 'Earth',
    'moons': 1
}
# Accessing Values in a Dictionary
print(planet)
print(" ************************************************************************************** ")
#  https://learn.microsoft.com/en-us/training/modules/python-dictionaries/2-dictionary-basics
# 
print(planet.get('name'))
print(planet.get('moons'))
print(" ************************************************************************************** ")
# planet['name'] is identical to using planet.get('name')
print(planet['name'])
print(planet['moons'])
print(" ************************************************************************************** ")
"""
Although the behavior of get and the square brackets ([ ]) is generally the same for retrieving items, there's one key difference.
 If a key isn't available, get returns None, and [ ] raises a KeyError.
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError
"""
wibble = planet.get('wibble') # Returns None
print("""  wibble = planet['wibble'] # Throws KeyError """)
print(" ************************************************************************************** ")
"""
Modify dictionary values
You can also modify values inside a dictionary object, by using the update method. This method accepts a dictionary as a parameter,
 and updates any existing values with the new ones you provide.
 If you want to change the name for the planet dictionary, you can use the following code, for example:

planet.update({'name': 'Makemake'})
# No output: name is now set to Makemake.
"""
planet.update({'name': 'Makemake'})
print(planet)
print(" ************************************************************************************** ")
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
print(planet)
print(" ************************************************************************************** ")
planet['name'] = 'Jupiter'
planet['moons'] = 79
print(planet)
print(" ************************************************************************************** ")
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
print(planet)
print(" ************************************************************************************** ")
"""
To remove a key, you use pop. pop returns the value and removes the key from the dictionary.
 To remove orbital period, you can use the following code:
 planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
"""
planet.pop('orbital period')
print(planet)
print(" ************************************************************************************** ")
"""
Complex data types - NESTED DICTIONARIES
You can also nest dictionaries inside other dictionaries.
 For example, you can create a dictionary that contains a dictionary for each planet in our solar system.

 # Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

"""
 # Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)
print(" ************************************************************************************** ")
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
print(" ************************************************************************************** ")


