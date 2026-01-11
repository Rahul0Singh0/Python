# Set

# A set is an unordered collection of unique elements.
# Sets are defined by enclosing items in curly braces {} or using the set() function.
# Example of creating a set
my_set = {1, 2, 3, 'a', 'b', 'c'}
# Accessing elements in a set (note: sets are unordered)
print("Set:", my_set)

# Adding elements to a set
my_set.add(4)
print("Set after adding 4:", my_set)

# Removing elements from a set
my_set.remove('a')
print("Set after removing 'a':", my_set)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets:", difference_set)     

# Set methods
set_length = len(my_set)
print("Length of set:", set_length)
is_subset = {1, 2}.issubset(my_set)
print("Is {1, 2} a subset of my_set?:", is_subset)

# Frozenset
# A frozenset is an immutable version of a set.
# Frozensets are defined using the frozenset() function.
# Example of creating a frozenset
my_frozenset = frozenset([1, 2, 3, 'a', 'b', 'c'])
print("Frozenset:", my_frozenset)

# Attempting to modify a frozenset (will raise an error)
# my_frozenset.add(4)  # Uncommenting this line will raise an AttributeError
# Frozenset methods
frozenset_length = len(my_frozenset)
print("Length of frozenset:", frozenset_length)
if 'b' in my_frozenset:
    count_of_b = 1
else:
    count_of_b = 0
print("Count of 'b' in frozenset:", count_of_b)

