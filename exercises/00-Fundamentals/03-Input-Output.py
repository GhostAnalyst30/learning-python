"""
00-Fundamentals/
    03-Input-Output.py

Objective: Learn about input and output in Python.
In Python, we can use the input() function to get user input from the console.
"""

"""
Input and Output
"""

# Get user input

name = input("Enter your name: ")
age = input("Enter your age: ")

# Print user input

print("\nHello, " + name + "! You are " + age + " years old.", " [Concatenation with + operator]")
print("Hello, {}! You are {} years old.".format(name, age), " [Using format() method]")

print("name ->", type(name))
print("age ->", type(age))

# Convert user input to integers

age = int(age)

# We could include that function there age = int(input("Enter your age: "))

# Print user input with formatted strings

print(f"\nHello, {name}! You are {age} years old.", " [Using f-string]")
print("Hello, {}! You are {} years old.".format(name, age), " [Using format() method]")
print("name ->", type(name))
print("age ->", type(age))

"""
We can use labels for input() function to provide a prompt message to the user.
"""

print("\nUsing labels for input() function:")

name: str = input("Enter your name: ")
age: int = int(input("Enter your age: "))

print(f"\nHello, {name}! You are {age} years old.")

# If i write in the variable age a string, it will throw an error