import re

"""# Do practise this too
# https://developers.google.com/edu/python/regular-expressions

a = "Jas, get JOB fast"
# returns 1st occurrence location if matched
# returns None, if not matched
print(re.search("Jas", a), re.search("a", a), re.search("Dil", a), sep='\n')
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
print(re.search("Jas", a).span(), re.search("a", a).string, re.search("JOB", a).span(), re.search("Dil", a), sep='\n')
# returns all matched in a list.
# returns empty list, if not matched
print(re.findall("Jas", a), re.findall("a", a), re.findall("Dil", a), sep='\n')
# splits and provides sub-strings in a list, by removing specified letter or word
# we can restrict no. of searched instances as well
print(re.split("Jas", a), re.split("a", a),
      re.split("\s", a), re.split("\s", a, 1), sep='\n')
# replace
print(re.sub('\s', '9', a), re.sub('\s', '9', a, 2), sep='\n')
"""

#Read Text from File

def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines() # or read()

#Write Text to File

def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

#Append Text to File

def append_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)


text = "get a JOB FAST"
filename = "basics"

#write_to_file(filename, text)
#append_to_file(filename, text)
print(read_file(filename))

# for line in read_file(filename):
#     print(line)

