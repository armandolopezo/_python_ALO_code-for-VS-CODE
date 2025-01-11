"""
example: # running py arguments1.py 2023-01-01 # will produce the following output:
['backup.py', '2023-01-01']   
"""
import sys
print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

