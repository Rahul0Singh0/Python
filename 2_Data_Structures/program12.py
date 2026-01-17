def invert_dict(d):
    inverted = {}

    for key, value in d.items():
        inverted[value] = key

    return inverted

print(invert_dict({"a": 1, "b": 2}))
