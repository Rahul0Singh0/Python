list_nums = [1, 2, 3, 4, 5]
print("Original list:", list_nums)

# Append an element to the end of the list
list_nums.append(6)
print("After appending 6:", list_nums)

# Remove an element from the list
list_nums.remove(3) 
print("After removing 3:", list_nums)

# Insert an element at a specific index
list_nums.insert(2, 10)
print("After inserting 10 at index 2:", list_nums)

# Sort the list in ascending order
list_nums.sort()
print("After sorting the list:", list_nums)

# Reverse the list
list_nums.reverse() 
print("After reversing the list:", list_nums)

# Get the length of the list
length = len(list_nums)
print("Length of the list:", length)

# Access an element by index
element_at_index_2 = list_nums[2]
print("Element at index 2:", element_at_index_2)

# Slice the list to get a sublist
sublist = list_nums[1:4]
print("Sublist from index 1 to 3:", sublist)

# Clear all elements from the list [because of list is mutable]
list_nums.clear()
print("After clearing the list:", list_nums)

# Demonstrate that the list is mutable by adding elements again
list_nums.extend([7, 8, 9])
print("After extending the list with [7, 8, 9]:", list_nums)

# Copy the list
copied_list = list_nums.copy()
print("Copied list:", copied_list)

# Count occurrences of an element
count_of_8 = list_nums.count(8)
print("Count of 8 in the list:", count_of_8)

# Find the index of an element
index_of_9 = list_nums.index(9)
print("Index of 9 in the list:", index_of_9)

# Pop an element from the end of the list
popped_element = list_nums.pop()
print("Popped element:", popped_element)
print("List after popping an element:", list_nums)

# Extend the list with another list
list_nums.extend([10, 11, 12])
print("After extending the list with [10, 11, 12]:", list_nums)

# Demonstrate list comprehension to create a new list
squared_list = [x**2 for x in list_nums]
print("Squared list using list comprehension:", squared_list)

# Demonstrate nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)

# Accessing elements in a nested list
element_in_nested = nested_list[1][0]
print("Element at nested_list[1][0]:", element_in_nested)

# Flattening a nested list using list comprehension
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list from nested list:", flattened_list)