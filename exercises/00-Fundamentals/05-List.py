"""
00-Fundamentals/
    05-List.py

Objective: Learn about lists in Python.
In Python, a list is a collection of items that are ordered and changeable. Lists are defined by enclosing items in square brackets [] and can contain elements of different data types.
"""
print("Lists:")
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Accessing List Items
print("Item at index 1:", thislist[1])
print("Item at index 2:", thislist[2])
print("Item at index 0:", thislist[0])

# Allow duplicate values in a list
print("\nAllow duplicate values in a list:")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print("\nList Length:")
thislist = ["apple", "banana", "cherry"]
print(len(thislist), "elements")


"""
Indexing:
- Positive Indexing: Starts from 0 and goes up to n-1 (where n is the number of elements in the list).
- Negative Indexing: Starts from -1 (last element) and goes up to -n (first element).
Slicing:
- Slicing allows you to access a range of elements in a list.
- The syntax for slicing is list[start:end], where start is the index of the first element and end is the index of the last element (exclusive).
"""

# Indexing

print("\nIndexing:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
print("Item at index 1:", thislist[1]) # The second item in the list is "banana"
print("Item at index 2:", thislist[-1]) # The last item in the list is "cherry"

# Slicing

print("\nSlicing:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("List ->", thislist)
print("Items from index 2 to 4:", thislist[2:5]) # Prints the items from index 2 to 4 (not including index 5)
print("Items from index 3 to final:", thislist[3:]) # Prints the items from index 3 to the end (not including index 4)
print("Items from index -4 to -1:", thislist[-4:-1]) # Prints the items from the fourth-to-last to the first-to-last (not including index -1)

print("\nCheck if an item exists in the list:")
thislist = ["apple", "banana", "cherry"]
print("List ->", thislist)
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


"""
Changing List Items:
- You can change the value of a specific item in a list by referring to its index.
"""

thislist = ["apple", "banana", "cherry"]
print("\nChanging List Items:")
print("List ->", thislist)
thislist[1] = "blackcurrant"
print("Changed List ->", thislist) # The second item has been changed to "blackcurrant"

print("\nChanging a range of list items:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print("List ->", thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print("Changed List ->", thislist)

# Using the insert() method to add an item at a specific index

thislist = ["apple", "banana", "cherry"]
print("\nUsing the insert() method to add an item at a specific index:")
print("List ->", thislist)
thislist.insert(2, "watermelon")
print("List after insertion ->", thislist)