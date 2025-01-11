# To sort a list, use the .sort() method on the list.
#  Python sorts a list of strings in alphabetical order and a list of numbers in numeric order:
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print(regular_satellite_moons)

regular_satellite_moons.sort()
print(regular_satellite_moons)

print("The regular satellite moons of Jupiter are", regular_satellite_moons)
