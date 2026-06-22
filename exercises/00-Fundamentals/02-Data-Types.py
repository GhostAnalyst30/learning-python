"""
00-Fundamentals/
    02-Data-Types.py

Objective: Learn about data types in Python.
In Python, there are several built-in data types that are used to store different types of data.
"""

"""
Booleans:
- True
- False
"""

x = True
y = False

print("Booleans:")
print("x ->", x)
print("y ->", y)

# Booleans Operations
print("\nBooleans Operations:")
print("x and y ->", x and y)
print("x or y ->", x or y)
print("not x ->", not x)
print("not y ->", not y)

"""
Numbers:
- int: Integer numbers, e.g., 1, 2, 3
- float: Floating-point numbers, e.g., 1.5, 2.0, 3.14
- complex: Complex numbers, e.g., 1 + 2j
"""
print("\nNumbers:")
print("Integer:", 1, 2, 3)
print("Float:", 1.5, 2.0, 3.14)
print("Complex:", 1 + 2j, 3 + 4j)


"""
Strings:
- str: A sequence of characters, e.g., "Hello, World!"
"""
print("\nStrings:")

word = "Hello, World!"
print("word ->", word)

reversed_word = word[::-1]
print("reversed_word ->", reversed_word)
# Or...
reversed_word = "".join(reversed(word))
print("reversed_word ->", reversed_word)