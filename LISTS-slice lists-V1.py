# A slice creates a new list. It doesn't modify the current list.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
planets_after_earth = planets[3:8]
print(planets_after_earth)
planets_after_earth = planets[3:]
print(planets_after_earth)

