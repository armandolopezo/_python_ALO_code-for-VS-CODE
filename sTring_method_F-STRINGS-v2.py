"""
Using an expression doesn't require a function call. Any of the string methods are valid as well.
 For example, the string could enforce a specific casing for creating a heading:
"""
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
