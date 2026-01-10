# *args (Variable Length Arguments)
# Used when number of arguments is unknown.
def total_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))


# **kwargs (Keyword Variable Arguments)
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(name="Rahul", age=24, course="MCA")