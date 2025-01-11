"""
Variable keyword arguments
For a function to accept any number of keyword arguments, you use a similar syntax. In this case, a double asterisk is required:
"""
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
# {'tanks': 1, 'day': 'Wednesday', 'pilots': 3}
print('***************************')
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
# 3 astronauts assigned for this mission:
# captain: Neil Armstrong
# pilot: Buzz Aldrin
# command_pilot: Michael Collins

"""
Because you can pass any combination of keyword arguments, make sure to avoid repeated keywords. Repeated keywords result in an error:
"""
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")
#  File "<stdin>", line 1
# SyntaxError: keyword argument repeated: pilot




