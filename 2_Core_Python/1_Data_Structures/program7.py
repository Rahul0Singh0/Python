def is_palindrome(str):
    return str == str[::-1]

print(is_palindrome("racecar"))

# second way to check palindrome
def is_palindrome_two(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome_two("hello"))