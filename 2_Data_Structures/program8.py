# count frequecy of characters in a string
def char_frequency(string):
    frequency = {} # dictionary to hold character frequency

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

print(char_frequency("hello world"))