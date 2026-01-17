# Tuple

# A tuple is an immutable ordered collection of items.
# Tuples are defined by enclosing items in parentheses ().
# Example of creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
# Accessing elements in a tuple
first_element = my_tuple[0] 
print("First element:", first_element)

# Attempting to modify a tuple (will raise an error)
# my_tuple[0] = 10  # Uncommenting this line will raise a TypeError
# Tuple methods
tuple_length = len(my_tuple)
print("Length of tuple:", tuple_length)
count_of_a = my_tuple.count('a')
print("Count of 'a' in tuple:", count_of_a)