# methods r basically built-in fns in python
test_list = []
help(test_list.extend)  # provides documentation abt method
# use snake_casing for name of function, i.e., def name_of_function()
# classes use Camel casing, i.e., class Classname:
"""
    This multi-line comment is called as DocString
"""


# Standard convention is to use return, to return out of fn, to variable
# rather than typing print


# def add_fn(n1 type int, n2 type int):  # this enforces input to be of int
def add_fn(n1, n2):  # if no enforcement, then typecast inside fn
    return int(n1) + int(n2)


add_fn(2, 3)  # invoking this alone won't print output
#               as print sttmt not there inside fn
print(add_fn(3, 2))
print(add_fn('7', '2'))

list1 = [3, 4, 8, 9, 14, 16, 11, 19]


def check_even(sequence):
    return [num for num in sequence if num % 2 == 0]


print(check_even(list1))

work_hrs = [('a', 100), ('b', 789), ('c', 643)]


def employee_of_month(emp_details):
    max_hrs = 0
    employee_name = ''
    for name, hrs in emp_details:
        if max_hrs < hrs:
            max_hrs = hrs
            employee_name = name
    return f'Employee of Month is {employee_name} with {max_hrs} hrs'


print(employee_of_month(work_hrs))


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(7, 9))
print(lesser_of_two_evens(6, 10))


def animal_crackers(text):
    str_list = text.split()
    return str_list[0][0].lower() == str_list[1][0].lower()


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short. Provide name greated than 3 letters'


print(old_macdonald('macdonald'))


def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('I am home'))
print(master_yoda('We are ready'))


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))


# *args    -- returns list of positional args in a tuple
# **kwargs -- returns a dictionary of key-value pairs


def myfunc(*args):
    return [even for even in args if even % 2 == 0]


print(myfunc(6, 8, 7, 3, 2, 5, 4))


def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')


# Lambda expressions are a way to quickly create 1-time use anonymous fn
# map fn -- takes fn as an arg n a list to iterate through. Ex:


def square(num):
    return num ** 2


list1 = [3, 6, 2, 9, 11, 15, 4, 22, 18]

# lambda way to define same fn as above
square1 = lambda num_list: [num ** 2 for num in num_list]
print('lambda : ', square1(list1), sep='\n')

# map way of doing same work
print(list(map(square, list1)))  # executes fn for each value in list1

# lambda way >>
print('lambda way: ', list(map(lambda list1: list1 ** 2, list1)), sep='\n')


# filter fn returns an iterator yielding items of iterable, for which,
# we pass in the item into the fn, is true.
# basically, need to filter by fn ( tht returns true or false). Ex:


def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, list1)))

# lambda way >>
print('lambda way: ', list(filter(lambda num: num % 2 == 0, list1)), sep='\n')

# when a variable is created in Python, its stored in a namespace
# LEGB Rules for to decide scope of variable
#       Local - var defined inside a fn stays local to that fn
#           Ex: lambda num: num**2 <-- this var is local to lambda fn
#       Enclosing fn locals - var defined in local scope of nested fn
#       Global - var assigned at top-lvl of a module file
#       Built-in - var pre-assigned in built-in names module,
#                   lowest priority, library-lvl scope
# This is the order tht Python looks for vars in.
# Python starts out by checking local namespace,

a = 1  # <-- Global var, 3rd highest priority, module lvl scope


def num():
    a = 2  # <-- Enclosing fn local var, 2nd highest priority, more scope

    def print_num():
        a = 3  # <-- Local namespace, highest priority, least scope
        print(a)

    print_num()


num()


def up_low(s):
    print(f'Original String : {s}')
    d = {'upper': 0, 'lower': 0}
    for letter in s:
        if letter.isupper():
            d['upper'] += 1
        elif letter.islower():
            d['lower'] += 1
    print(f"No. of Upper case characters : {d['upper']}")
    print(f"    No. of Lower case characters : {d['lower']}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

