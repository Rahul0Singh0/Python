def second_largest(t):
    unique = list(set(t)) # remove duplicates after converting to list
    unique.sort() # sort the list
    return unique[-2] # return the second last element

print(second_largest((10, 20, 30, 20)))
