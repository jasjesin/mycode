dictA = {
    "name": "jas",
    "age": 39,
    "need": "get a job ASAP",
    "date": "b4 xmas"
}

dictB = {
    "name": "jz",
    "age": 39,
    "need": "get a stable job",
    "date": "ASAP"
}

# experiment to see diff in content returned for key, values n items
"""
print(type(dictA))
print(dictA)
print("\n========================\nKeys:")
[[print(i) for i in dictA.keys()]]
print("\n========================\nValues:")
[[print(i) for i in dictA.values()]]
print("\n========================\nItems:")
[[print(i) for i in dictA.items()]]
print("\n========================\n========================")
"""

# experiment to see how content of new dict over-write content of existing dict
"""
print(f"A: {dictA}")
print(f"B: {dictB}\n================================\n")

dictC = dictA | dictB
dictD = dictB | dictA
#dictA |= dictB
dictB |= dictA

print(f"A: {dictA}")
print(f"B: {dictB}")
print(f"C: {dictC}")
print(f"D: {dictD}")
"""

# experiment to perform value replacements
"""
a = "get a job"
b = "ASAP"
c = "{} b4 xmas {}"
print(c.format(a, b))
print(f"{a} b44444 xmasss {b}")
"""

# experiment on how to deal wid vars starting wid *
"""
head, *tail = [1, 2, 3, 4, 5]
number = 3
if number in tail:
    print(f"{number} is present in {tail}")

for i in tail:
    print(i)
    if number == i:
        print(f"{number} is present at {i} location in {tail}")
"""

# experiment to understand dictionary-comprehension
"""
users = [
    (0, "a", "passwd142"),
    (1, "b", "passwd231"),
    (2, "c", "passwd876"),
    (3, "d", "passwd823")
]
print('===========================\n1. Users:', users)
dictE = {user[1]: user for user in users}
print('===========================\n2. dictE', dictE)
print('===========================\n3. Keys: ', dictE.keys())
print('===========================\n4. Values: ', dictE.values())
"""

# yet to understand diff. b/w *args & **args in terms of usage
"""
details = {
    "name": "Jas",
    "age": 39
}

details1 = {
    "name": "jz",
    "need": "get job fast"
}


def named(*args):
    print(args)


def named1(**args):
    print(args)


def named2(**kwargs):
    print(kwargs)


def nice_output(**kwargs):
    named2(**kwargs)
    print("nicer")
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


def nice_output1(**args):
    named1(**args)
    print("nicer")
    for arg, value in args.items():
        print(f"{arg}: {value}")


named1(**details)
nice_output(**details)
nice_output1(**details)
"""

# no fun, need to deep dive more on this
# yet to understand diff. b/w *args & **args in terms of usage
"""def both(*args, **kwargs):  # this syntax is used to accept unlimited no. of args
    print(*args)
    print(type(args))
#    for arg in args.items():
#        print(f"{arg}")
    print(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print("================\n=================\n==============")
both(*details, **details1)
"""

"""
class Test:
    def __init__(self):
        print("initiating...")

    def instanceMethod(self):
        print(f"invokes {self} object")

    @classmethod
    def classMethod(cls):  # <class '__main__.Test'>, gets executed always
        #                    without waiting for class to be invoked/initiated
        print(f"invoked always {cls} without instantiating class")

    @staticmethod
    def staticMethod():    # <class 'NoneType'>
        print(f"not sure of much use of this one")


print('\n========\nchecking type for class method:', type(Test.classMethod()))
print('\n========\nchecking type for static method:', type(Test.staticMethod()))
#student = Test()  # instantiation of this invokes __init__ constructor
#print('========\n checking type for instance method:', type(student))
"""

import sys
print('\n===============\nModules used:\n===============\n', sys.modules, sep='\n')
print('\n===============\nPath set:\n===============\n', sys.path)
