######################
# String Manipulation
######################
a = "Jas, get get JOB fast"
# provides location of 1st occurence of letter or word
# -1 if not found. Ex: 3rd is not found.
print(a.find('a'), a.find("get"), a.find("D"))
# provides count of occurences of letter or word
# 0 if not found. Ex: 3rd is not found.
print(a.count('a'), a.count('get'), a.count('Dil'))
# splits n returns list of sub-strings, removes the searched letter or word
# returns same, if split criteria not met
print(a.split('a'), a.split('get'), a.split('Dil'), a.split(' '), sep='\n')
# returns True or False, if condition met
print(a.startswith('J'), a.startswith('Jas'), a.startswith('Dil'))
print(a.endswith('t'), a.endswith('fast'), a.endswith('Dil'))
# repeat
print(a*3)
# replace
print(a.replace('get JOB', 'BEST JOB'))
# upper/lower
print(a.upper())
print(a.lower())
# 1st letter of each word in upper case, rest all lower
print(a.title())
# 1st letter of entire string in upper case, rest all made lower
print(a.capitalize())
# swaps case from lower <-> upper, for each letter in the string
print(a.swapcase())
# reverse entire string,
# reverse fn is not directly avl, need to use it thru join
print(''.join(reversed(a)))
# or better, use >>
print(a[::-1])
# strip a string
b = "*****Hello, My name is JAs****"
c = "Hello*****, My name is JAs****"
d = "    Hello, My name is JAs    "
e = "Hello      , My name is JAs"
# can strip off stuff only from beginning or trailing, not in-between string
print(a.strip('*'), c.strip('*'), d.strip(), e.strip(), sep='\n')
print('lstrip', a.lstrip('*'), c.lstrip('*'), d.lstrip(), e.lstrip(), sep='\n')
print('rstrip', a.rstrip('*'), c.rstrip('*'), d.rstrip(), e.rstrip(), sep='\n')

word = "Hello World"
print(word.isalnum())        # check if all char are alphanumeric
print(word.isalpha())        # check if all char in the string are alphabetic
print(word.isdigit())        # test if string contains digits
print(word.istitle())        # test if string contains title words
print(word.isupper())        # test if string contains upper case
print(word.islower())        # test if string contains lower case
print(word.isspace())        # test if string contains spaces
print(word.endswith('d'))    # test if string endswith a d
print(word.startswith('H'))  # test if string startswith H
