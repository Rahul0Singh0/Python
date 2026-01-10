text = input("Enter a string: ")
count = 0

text = text.lower()

for ch in text:
    if ch in "aeiou":
        count += 1

# one liner alternative
print("Vowel count:", count)

text = input("Enter a string: ")

vowel_count = sum(1 for ch in text.lower() if ch in "aeiou")

print("Vowel count:", vowel_count)


# using dictionary
text = input("Enter a string: ").lower()
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for ch in text:
    if ch in vowels:
        vowels[ch] += 1

print(vowels)
print("Total vowels:", sum(vowels.values()))

