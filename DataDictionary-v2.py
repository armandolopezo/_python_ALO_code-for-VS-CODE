# Enter code below
planet = {
    'name': 'Mars',
    'moons': 2
}
print(planet)

# Output: {'name': 'Mars', 'moons': 2}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
# Output: Mars has 2 moon(s)
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')
# Output: Mars has a polar circumference of 6752

