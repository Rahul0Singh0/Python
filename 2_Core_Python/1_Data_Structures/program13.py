def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
