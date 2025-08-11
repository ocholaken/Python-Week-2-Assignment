"""
# Python List Operations Exercise 🐍

This exercise demonstrates basic Python list operations, including:
- Creating an empty list
- Adding elements with append()
- Inserting elements at a specific position
- Extending a list with another list
- Removing elements with pop()
- Sorting the list in ascending order
- Finding the index of a specific value

## How to Run
1. Save this file as list_operations.py.
2. Open a terminal or command prompt.
3. Run:
   python list_operations.py

## Expected Output
Index of 30: 4
Final list: [10, 15, 20, 30, 40, 50, 60]

✨ Skills Practiced: Python basics, list manipulation, indexing, sorting.
"""

# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position
my_list.insert(1, 15)

# Extend with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find and print index of 30
print("Index of 30:", my_list.index(30))

# Print final list
print("Final list:", my_list)
