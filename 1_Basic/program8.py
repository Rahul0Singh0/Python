def greet(name):
    print("Hello", name)

greet('rahul');


def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, mul = calculate(10, 5)
print(sum_, diff, mul)
# Python returns tuple internally