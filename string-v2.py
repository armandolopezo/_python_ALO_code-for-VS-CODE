"""
You can enclose Python strings in single, double, or triple quotation marks.
However, when a string contains words, numbers, or special characters (a substring) that are also enclosed in quotation marks,
 you should use a different style. For example, if a substring uses double quotation marks,
   enclose the entire string in single quotation marks, as shown here:
   
   'The "near side" is the part of the Moon that faces the Earth.'

   Similarly, if there are single quotation marks (or an apostrophe, as in Moon's in the following example) anywhere within the string,
     enclose the entire string in double quotation marks:

     "We only see about 60% of the Moon's surface."
"""
fact = "The Moon has no atmosphere."
two_facts = fact + " No sound can be heard on the Moon."
print(two_facts)