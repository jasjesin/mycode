# Basic Practice:
# http://codingbat.com/python
#
# More Mathematical (and Harder) Practice:
# https://projecteuler.net/archives
#
# List of Practice Problems:
# http://www.codeabbey.com/index/task_list
#
# A SubReddit Devoted to Daily Practice Problems:
# https://www.reddit.com/r/dailyprogrammer
#
# A very tricky website with very few hints and touch problems (Not for beginners but still interesting)
# http://www.pythonchallenge.com/

abc = 'Jas get a job FAST'
print(abc[::-1])           # reverses string
print(abc[3:])             # start from 3rd index
print(abc[:4])             # go up to 4th index, but not including 4th index
print(abc[4:9:2])          # slice from index 4 to 9, hop by 2
print(abc[2::4])           # start from index 2, hop by 4

# string interpolation -- stick a variable into a string
# 2 methods -- .format() & f-strings (formatted string literals)
# {} r called placeholders for variables that r going to be inserted
# Benefit, we can specify which positional variable to be used when
print('{1} Get a {0} {2}'.format('Job', 'Jas', 'FAST..!!'))
print('{b} Get a {0} {c}'.format('Job', b='Jas', c='FAST..!!'))
print('Get JOB before {d:1.2f}'.format(d=01.312023))
# in d:1.2f
#   -- 1 is width or white spaces before value starts
#   -- 2 is no. of decimals to restrict value to.
# f-strings r introduced from py 3.6 onwards
d=01.312023
print(f'Get JOB before {d:1.2f}')

# String & List are ordered object, i.e., can be indexed, sorted or sliced
#        values can b accessed via index no.s
# Trade-off -- cant be used as a key-value store
# Diff. b/w str & lists -- strings r immutable, i.e,
#                we cant update value at an index in str, gives below error
# TypeError: 'str' object does not support item assignment
#                        in list, we can.
my_string = 'abcdef'
print(my_string[3])
# my_string[3] = 'z'  # <-- this gives error
print(my_string)
try_list = ['abc', 2, 5.6823, 'def', "xyz"]
print(try_list)
try_list.append(6)
print(try_list)
popped_item = try_list.pop()
print(popped_item, try_list, sep='\n')
try_list.pop(2)   # takes index no. to pop item from
print(try_list)
try_list = [98.9, 2, 5.6823, 32.14]  # sort happens of same data type only
# i.e., either all int/float combo or all strings but no combo of str & int
sorted_list = try_list.sort()  # sort happens in-place, n fn returns None
print(try_list, sorted_list, type(try_list), type(sorted_list), sep='\n')
# indexing & slicing works same way in lists as well
print(try_list[2], try_list[1:], try_list[:2], sep='\n')

# Dictionaries  -- stores key-value pairs & accessed via keys
# Trade-off     -- unordered, cant b sorted or accessed via index no.s
# Application   -- prices in a store, or anywhere key-value store is needed
# Dictionary can store lists as well as nested dictionaries
nested_dict = {'name': 'jz',
               'id': 95391,
               'address': {'street number': 1000,
                           'street': 'walcott',
                           'city': 'MH'},
               'family': [1, 'sid', 'srt']}
print(nested_dict)
print(nested_dict['address'])
print(nested_dict['address']['city'])  # stacking key calls to get value
print(nested_dict['family'][1])
print(nested_dict['family'][2].upper())
nested_dict['country'] = 'US'  # add / update new entries in dictionary
print(nested_dict)
print(nested_dict.keys())
print(nested_dict.values())
print(nested_dict.items())  # returns key-value pairs in tuples

# tuples -- immutable
# application -- wen u pass objects to programs n want to make sure
#                that those values do not get accidentally changed
# tuple is a vry convenient resource of Data Integrity
t = [1, 'a', 6, 'd', 'a']
print(t.count('a'))
print(t.index('a'))     # provides index of 1st occurrence
print(t.index(1))

# Sets -- unordered collection of unique values, i.e., no duplicate values
# wen trying to add duplicate values, set ignores duplicates
myset = set()
myset.add(1)
myset.add(1)
myset.add(2)
myset.add(1)
print(myset)
# cast a list to a set, to fetch only unique values.
list_wid_duplicates = [1, 2, 3, 3, 3, 2, 1]
new_set = set(list_wid_duplicates)
print(list_wid_duplicates, new_set, sep='\n')
print(set('Mississippi'))

# Booleans -- vry imp when dealing wid control flow n logic
print(3.0 == 3)  # returns True cuz python doesn't cares for data type
#                  to be int or float as long as value is same
print(1 < 2 < 3)  # gives True
print(8 > 8 > 1)
print(4 > 2 < 3)
print(2 < 5 != 7)
print(2 < 5 and 5 > 7)
print(2 == 5 or 5 > 7)
print(not 9 == 9)
print(not 8 != 8)
# Find square root of a number
# number = int(input("Enter number to find square root of: "))
number = 625
print(int(number ** 0.5))

# for-loops
for _ in 'Jas get JOB FAST':  # common convention to use _ if var not needed
    print(_)

# tuple unpacking, pretty common format in py programs, i.e.,
# collection of tuples in a list
test_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
for _ in test_list:
    print(_)

for a, b in test_list:
    print(a, b, sep='\n')  # this is called tuple unpacking, i.e.,
    #                        to unpack values of tuple

# dictionary can leverage tuple unpacking wid output returned from items
dict1 = {'k1': 1, 'k2': 2, 'k3': 3}
for i in dict1:  # ONLY iterates through keys, NOT values
    print(i)

for k, v in dict1.items():
    print(k, v)  # This is precisely wht unpacking does for tuples

# continue -- helps skip 1 round of loop. Example:
my_string = 'Jas get a JOB'
for i in my_string:
    if i == 'a':
        continue  # skips presence of a in the iteration
    print(i)

# Generators -- range(), enumerate(), zip()
#              spl fn tht generates info instead of saving to memory
print(range(0, 10))  # doesn't give 0 to 9 as output as it's a generator
print(list(range(2, 11, 3)))  # adds output in a list, more efficient way

for num in range(3, 9, 2):    # starting count, max, step/skip count
    print(num)

# when we need a counter, we can use enum. Ex:
index_count = 0
word = 'abcde'
for _ in word:
    print(f'index: {index_count}, letter: {word[index_count]}')
    index_count += 1

# more efficient way is using enumerate that returns tuples >>
for _ in enumerate(word):  # returns position/location & data pair
    print(_)
""" -- think about it
number = 10
for _, value in enumerate(number):  # returns position/location & data pair
    # if number is not prime, then print
    print(_)
"""

# zip() concatenates lists together n returns output in tuple pair
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [100, 300, 750]
print(list(zip(list1, list2, list3)))  # type cast in list or iterate
for _ in zip(list1, list2, list3):  # contributes to zip unpacking
    print(_)
# these can be unpacked by picking one of the values like >>
for a, b, c in zip(list1, list2, list3):  # contributes to zip unpacking
    print(b)


# if lists r uneven, then it returns up to max common length items
list1 = [1, 2, 3, 5, 8, 9]
list2 = ['a', 'b', 'c', 'z', 'x', 'p', 't', 'n']
list3 = [100, 300, 750, 230]
print(list(zip(list1, list2, list3)))  # type cast in list or iterate
for _ in zip(list1, list2, list3):  # matches till shortest length of 3 lists
    print(_)

# in operator -- vry useful fir chking if value exists or not
print('z' in list2)
print('h' in list2)

# min(), max() math functions n random library
from random import shuffle, randint
# shuffle -- in-place fn, operates in-place n doesnt return anything
print(list1)
print(shuffle(list1))  # returns none, just shuffles
print(list1)
new_list = shuffle(list3)  # returns none, as highlighted by this underline
print(new_list)
print(randint(4, 87))
random_number = randint(3, 37)  # this one returns n can be saved
print(random_number)

# list comprehension -- flattened out for-loop, takes less space
#                       but takes same computational time
even_number = [x for x in range(1,23) if x % 2 == 0 ]
print(even_number)
even_odd = [x if x % 2 == 0 else 'Odd' for x in range(3, 11)]
print(even_odd)
# nested loop in list comprehension
nested_list = [x*y for x in list1 for y in list3]
print(nested_list)
