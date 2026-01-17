# Reverse the list
def reverse_list(input_list):
    left = 0
    right = len(input_list)-1
    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1
    return input_list

my_list = [1, 2, 3, 4, 5]   
print(my_list[::-1])  # Using slicing to reverse the list
reversed_list = reverse_list(my_list)
print("Reversed List:", reversed_list)

