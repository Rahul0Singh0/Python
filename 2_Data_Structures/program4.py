def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print("Max value in [3, 1, 4, 1, 5, 9]:", find_max([3, 1, 4, 1, 5, 9]) )