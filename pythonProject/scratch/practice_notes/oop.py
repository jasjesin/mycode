from typing import List
from operator import itemgetter
import functools

# Functions inside class are called methods
# Methods starting & ending wid __ are called magic methods
#      cuz Python invokes these methods internally for execution,
#      based on situations,and we do not need to call these methods
# self is standard convention in python
# __init__(self) is constructor method, that instantiates/assigns values
#           internally, when an instance of class is created
# __str__(self) method returns string representation of object(instance of class)
# __repr__(self) method helps provide debug sttmts to Python Debugger
#             goal is to be unambiguous & help recreate original object easily

class Person:
    def __init__(self, name, grades):
        self.name = name  # takes whtever self is & accesses name property inside of it
        self.grades = grades


jas = Person("Jas", (83, 76, 92, 71, 64))  # Python calls init method automatically
print(jas)  # gives object description like
#                      <__main__.Person object at 0x10c859f50>
print(jas.name)
print(jas.grades)


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"Name: {self.name}, Grades: {self.grades}"

    def __repr__(self):
        return f"<Name: {self.name}, Grades: {self.grades}>"

    def average_grades(self):
        return sum(self.grades) / len(self.grades)


jas = Student("Jas", (82, 87, 93, 74, 61))  # use class to create object of it
#                                             This new thing behaves like class
# Basically python creates new empty container & runs init method,
# and creates empty thing called self, sets/changes property name under self
# python gives that loaded self and name given to that self, now, is, jas
print(jas)  # This time, see difference in object description given by python like
#                      Name: Jas, Grades: (83, 76, 92, 71, 64)
#             So, this time, __str__ is invoked internally by Python
print(jas.average_grades())  # basically, this one calls


#     Student.average_grades(jas)

# =============================================================================
# =========================== Execrise ========================================
# =============================================================================


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = sum([item['price'] for item in self.items])
        return total


# =============================================================================
# =============================================================================

# instance, class & static methods
# instance methods r used most of the time, to produce action from data passed
#                  inside the object
# class methods r used often as factories, good to restrict specific value
#      as one of pre-defined ones. These invoke class to create new object.
# static method is used for code organization

class ClassTest:
    def instance_method(self):  # any method containing self, is instance method
        #                         cuz it gets instance or object of class
        print(f"invoked {self}")

    @classmethod
    def class_method(cls):  # gets cls (class) as pmtr
        print(f"invoked {cls} without creating object")

    @staticmethod
    def static_method():  # don't get anything in pmtr, called without
        #                     instantiation of class.
        print("invoked static method")


ClassTest.class_method()  # invoked without creating any instance of class
ClassTest.static_method()
student = ClassTest()
student.instance_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book: {self.name}, Type: {self.book_type}, Weight: {self.weight}gms>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


heavy = Book.hardcover("A", 540)
light = Book.paperback("B", 315)
print(heavy, light, sep='\n')


# ===========================================================================
# ====================== Exercise  ==========================================
# ===========================================================================


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {int(store.stock_price())}"


# ===========================================================================
# ===========================================================================


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device: {self.name!r}, connected by {self.connected_by}"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


printer = Device("printer", "USB")
print(printer)


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}, pages remaining: {self.remaining_pages}"

    def print_pages(self, pages):
        if self.connected:
            print(f"Printing {pages} pages...")
            self.remaining_pages -= pages
        else:
            print("Printer is disconnected.")
            return


printer = Printer("Epson", "USB", 500)
print(printer)
printer.print_pages(246)
print(printer)
printer.print_pages(77)
print(printer)


# class composition, used more...inheritance is used lesser


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<BookName: {self.name}>"


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"No. of books loaded on bookshelf: {len(self.books)}"


b1 = Book("TikTok")
b2 = Book("Samsung")
shelf = BookShelf(b1, b2)

print(b1, b2, shelf, sep='\n')


# Type Hinting -- we can mandate types expected and IDE can pass hints
#                 if incorrect type is passed, thereby, easing out debugging
#                 These r just helpers, these don't stop ur code from running

def avg(sequence: List) -> float:  # mandating needed n returned types
    #                                IDE like PyCharm shows data type needed
    #                                when you hover mouse over arg passed
    return sum(sequence) / len(sequence)


print(avg([2, 5, 7]))


# print(avg(357))

# imports
# __name__ is a global var in Python tht changes based on which file
#          execution is performed in. It helps rectify file u run n file u import
#          Only the initial file gets __main__ value, rest all get filenames

# How does python knows from which path, module needs to be imported from
# import sys -- unlocks system functionalities,
#               print(sys.path), provides list of paths for python to look for
#               print(sys.modules) provides list of imported modules
# absolute imports preferable, relative is confusing


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("ERROR: Divisor cannot be zero")
    return x / y


grades = []
print("Welcome to average grade check program")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("ERROR: There are no grades for you yet")
    print(e)
except ValueError as v:
    print("Values missing")
else:  # this code runs if NO error
    print(f"Your average grade is {average}")
finally:  # this code always runs, irrespective of error or not
    print("Thank you")


# custom errors


class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return f"Book: {self.name}, Pages Read: {self.pages_read}, " \
               f"Total Pages: {self.page_count}"

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f"The amount of pages read, i.e.,"
                                        f" {self.pages_read + pages}, exceeds total pages "
                                        f"{self.page_count}")
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of total "
              f"{self.page_count} pages")


b1 = Book("Get a Job", 163)
print(b1)
try:
    b1.read(93)
    b1.read(74)
except TooManyPagesReadError as t:
    print(t)
else:
    print("Good Going")
finally:
    print("Thank you")


# First-class functions, means functions that r just vars
# we can pass these as args n can use them same way as any other var

def get_friend_name(friend):  # going to use this as 1st-class fn to add as arg
    return friend["name"]


def search(sequence, expected, finder):
    for i in sequence:
        if finder(i) == expected:
            return i
    raise RuntimeError(f"Could not find {expected}")


friends = [
    {"name": "jas", "age": 39},
    {"name": "jasjesin", "age": 40},
    {"name": "jzsingh", "age": 38}
]

print(search(friends, "jas", get_friend_name))  # added fn without (), like arg
# we can also use lambda in this case, instead of 1st class fn
#print(search(friends, "sunny", lambda friend: friend["name"]))
# can also use built-in fn
print(search(friends, "jzsingh", itemgetter("name")))

# decorators -- allow us to easily modify fns
# wid decorator, we create a new fn to replace original fn wid secure one
# its like safeguarding another fn. Example:

user = {"name": "jas", "access_level": "guest"}


def make_admin_secure(func):
    @functools.wraps(func)  # makes it a wrapper for func, needed for inner fn
    def secure_admin(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **args)
        else:
            return f"No admin access for {user['name']}"
    return secure_admin


@make_admin_secure
def get_admin_passwd():
    return "admin1234"


# below one not needed anymore wid decorator used before fn definition
# get_admin_passwd = make_admin_secure(get_admin_passwd)
print(get_admin_passwd())

# @ syntax for decorators
# decorating fns wid pmtrs
# use *args, **kwargs as pmtrs in decorator fn for it to accept any args
# adding pmtrs to decorators themselves
# mutability in python
# immutable objects -- tuples, strings, integers, floats & booleans

a = []
b = a
a.append("hello")
print(id(a))
print(id(b))
print(a)
print(b)
b.append("world")
print(id(a))
print(id(b))
print(a)
print(b)
# both a n b still point to same location, irrespective of change in a or b

# Mutable default pmtrs

