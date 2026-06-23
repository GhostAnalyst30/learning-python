"""
00-Fundamentals/
    04-Operators.py

Objective: Learn about operators in Python.
In Python, operators are special symbols that perform operations on variables and values.
"""

"""
Arithmetic Operators:
- Addition: +
- Subtraction: -
- Multiplication: *
- Division: /
- Modulus: %
- Exponentiation: **
- Floor Division: //
"""

print("Arithmetic Operators:")
a = 10
b = 3
print(f"a -> {a}")
print(f"b -> {b}")
print("Addition:", f"{a} + {b} = {a + b}")
print("Subtraction:", f"{a} - {b} = {a - b}")
print("Multiplication:", f"{a} * {b} = {a * b}")
print("Division:", f"{a} / {b} = {a / b}")
print("Modulus:", f"{a} % {b} = {a % b}")
print("Exponentiation:", f"{a} ** {b} = {a ** b}")
print("Floor Division:", f"{a} // {b} = {a // b}")

"""
Assignment Operators:
- Assign: =
- Add and Assign: +=
- Subtract and Assign: -=
- Multiply and Assign: *=
- Divide and Assign: /=
- Modulus and Assign: %=
- Exponentiation and Assign: **=
- Floor Division and Assign: //=
- AND bit a bit: &=
- OR bit a bit: |=
- XOR bit a bit: ^=
- Left Shift and Assign: <<=
- Right Shift and Assign: >>=
- Walrus Operator: :=
"""

print("\nAssignment Operators:")

a = 10
b = 3
print(f"a -> {a}")
print(f"b -> {b}")
print("Assign:", "a = 10 (assigns the value 10 to variable a)")
print("Assign:", "b = 3 (assigns the value 3 to variable b)")

a = 10
b = 3
a += b
print("\nAdd and Assign:", "a += b -> a = a + b ->", a,
      "(adds b to a and stores the result)")

a = 10
b = 3
a -= b
print("\nSubtract and Assign:", "a -= b -> a = a - b ->", a,
      "(subtracts b from a and stores the result)")

a = 10
b = 3
a *= b
print("\nMultiply and Assign:", "a *= b -> a = a * b ->", a,
      "(multiplies a by b and stores the result)")

a = 10
b = 3
a /= b
print("\nDivide and Assign:", "a /= b -> a = a / b ->", a,
      "(divides a by b and stores the result)")

a = 10
b = 3
a %= b
print("\nModulus and Assign:", "a %= b -> a = a % b ->", a,
      "(stores the remainder of the division)")

a = 10
b = 3
a **= b
print("\nExponentiation and Assign:", "a **= b -> a = a ** b ->", a,
      "(raises a to the power of b and stores the result)")

a = 10
b = 3
a //= b
print("\nFloor Division and Assign:", "a //= b -> a = a // b ->", a,
      "(performs integer division and stores the result)")

a = 10
b = 3
a &= b
print("\nBitwise AND and Assign:", "a &= b -> a = a & b ->", a,
      "(sets a bit to 1 only if both corresponding bits are 1)")

a = 10
b = 3
a |= b
print("\nBitwise OR and Assign:", "a |= b -> a = a | b ->", a,
      "(sets a bit to 1 if at least one corresponding bit is 1)")

a = 10
b = 3
a ^= b
print("\nBitwise XOR and Assign:", "a ^= b -> a = a ^ b ->", a,
      "(sets a bit to 1 if the corresponding bits are different)")

a = 10
b = 3
a <<= b
print("\nLeft Shift and Assign:", "a <<= b -> a = a << b ->", a,
      "(shifts bits left by b positions; equivalent to multiplying by 2^b)")

a = 10
b = 3
a >>= b
print("\nRight Shift and Assign:", "a >>= b -> a = a >> b ->", a,
      "(shifts bits right by b positions; equivalent to dividing by 2^b)")

print("\nWalrus Operator:", "(a := 10) assigns 10 to a and returns the value")
print("Example:", (a := 10))
print("Current value of a:", a)

"""
Ternary Operator:
- Syntax: value_if_true if condition else value_if_false
"""

print("\nTernary Operator:")
num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(f"num: {num} ->", x)
num = 4
x = "WEEKEND!" if num > 5 else "Workday"
print(f"num: {num} ->", x)

"""
Comparison Operators:
- Equal: ==
- Not Equal: !=
- Greater Than: >
- Less Than: <
- Greater Than or Equal To: >=
- Less Than or Equal To: <=
"""

print("\nComparison Operators:")

a = 10
b = 3
print(f"a -> {a}")
print(f"b -> {b}")
print("Equal:", f"{a} == {b} -> {a == b}")
print("Not Equal:", f"{a} != {b} -> {a != b}")
print("Greater Than:", f"{a} > {b} -> {a > b}")
print("Less Than:", f"{a} < {b} -> {a < b}")
print("Greater Than or Equal To:", f"{a} >= {b} -> {a >= b}")
print("Less Than or Equal To:", f"{a} <= {b} -> {a <= b}")


"""
Logical Operators:
- AND: and
- OR: or
- NOT: not
"""

print("\nLogical Operators:")
x = 5
print(f"x -> {x}")
print("x > 0 and x < 10 ->", x > 0 and x < 10)
print("x < 5 or x > 10 ->", x < 5 or x > 10)
print("not(x > 3 and x < 10) ->", not(x > 3 and x < 10)) # not(TRUE) -> FALSE

"""
Identity Operators:
- is: Returns True if both variables are the same object
- is not: Returns True if both variables are not the same object
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("\nIdentity Operators:")
print(f"x -> {x}")
print(f"y -> {y}")
print(f"z -> {z}")
print("x is z ->", x is z)
print("x is y ->", x is y)
print("x == y ->", x == y)

"""
Membership Operators:
- in: Returns True if a sequence with the specified value is present in the object
- not in: Returns True if a sequence with the specified value is not present in the object
"""

print("\nMembership Operators:")
fruits = ["apple", "banana", "cherry"]
print(f"fruits -> {fruits}")
print(f"banana is in fruits -> {'banana' in fruits}")

fruits = ["apple", "banana", "cherry"]
print(f"fruits -> {fruits}")
print(f"pineapple is not in fruits -> {'pineapple' not in fruits}")