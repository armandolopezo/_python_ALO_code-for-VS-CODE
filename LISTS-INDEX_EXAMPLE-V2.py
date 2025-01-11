planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
print("     *****************************************************************************          ")
# for i, planet in enumerate(planets, start=1):
#    print(f"planeta {i} es {planet}")
# print("     *****************************************************************************          ")
for contador in planets:
    print(contador)
    indice=planets.index(contador) + 1
    print(indice)
    print(f"planeta {indice} es {contador} \n") 



