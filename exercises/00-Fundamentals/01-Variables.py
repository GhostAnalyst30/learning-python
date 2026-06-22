"""
00-Fundamentals/
    01-Variables.py

Objective: Learn about variables in Python.
In Python, variables are used to store data values. A variable is created the moment you first
"""

print("Variables:")
x = 5
y = "John"
print("x ->", x)
print("y ->", y)

"""
We could know the type of a variable by using the type() function or casting with the variables types.
"""
# Typing a variable
print("\nTyping a variable:")
x = 5
print("x ->", x)

y = "John"
print("y ->", y)


# Casting a variable
print("\nCasting a variable:")
x = str(3)    # x will be '3'
print("x ->", x)
y = int(3)    # y will be 3
print("y ->", y)
z = float(3)  # z will be 3.0
print("z ->", z)

"""
Python permits single and double quotes, also is sensitive to the case of the variables names
"""

a = "Hello"
A = 'Hello'

print("\nCase sensitive:")
print("a ->", a)
print("A ->", A)

# a and A have different variables names but have the same value, so they are equal.
print("a == A ->", a == A)

"""
Python permits many values to multiple variables in one line, and also allows to assign the same value to multiple variables in one line.
"""

x, y, z = "Orange", "Banana", "Cherry"
print("\nMany values to multiple variables:")
print("x ->", x)
print("y ->", y)
print("z ->", z)

x = y = z = "Orange"
print("\nSame value to multiple variables:")
print("x ->", x)
print("y ->", y)
print("z ->", z)

# And we can unpack a collection of values into variables, but is uncommonly used in python.
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print("\nUnpacking a collection of values into variables:")
print("x ->", x)
print("y ->", y)
print("z ->", z)

"""
In python, variables can be globals or locals, we called it like scope.
"""

print("\nGlobal and local variables:")
x = "awesome"

def myfunc():
    x = "fantastic"
    return "Python is " + x

print("Local ->", myfunc())

print("Global ->", "Python is " + x)
