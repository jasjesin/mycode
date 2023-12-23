from datetime import datetime

# factorial


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)


def factorial_iterative(number):
    total = 1
    for i in range(1, number+1):
        total = total * i
    return total


#number = int(input("Type number to check factorial of: "))
"""number = 5
start = datetime.now()
print(factorial(number))
end = datetime.now()
print(f"Time taken: {end - start}")

start = datetime.now()
print(factorial_iterative(number))
end = datetime.now()
print(f"Time taken: {end - start}")
"""
# Fibonacci


def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number-2) + fibonacci(number-1)


def fibonacci_iterative(number):
    a, b, total = 0, 1, 0
    for i in range(number-1):
        total = a+b
        a = b
        b = total
    return total


"""start = datetime.now()
print(fibonacci(3))
end = datetime.now()
print(f"Time taken: {end - start}")
start = datetime.now()
print(fibonacci_iterative(3))
end = datetime.now()
print(f"Time taken: {end - start}")
print("0 1 1 2 3 5 8 13 21 34 55")


letters = ['a', 'f', 's', 'd', 'q']
names = ['Álvarez', 'Óscar', 'Josín', 'Olivia', 'José', 'Aarón']
numbers = [2, 65, 34, 2, 1, 7, 8]
numbers1 = ['2', '65', '34', '2', '1', '7', '8']

letters.sort()
names.sort()
numbers1.sort()

print(letters, names, numbers, numbers1, sep='\n')

letters.sort(reverse=True)
numbers.sort(reverse=True)

print(letters, numbers, sep='\n')
"""


