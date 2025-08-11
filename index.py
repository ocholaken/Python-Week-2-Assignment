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
