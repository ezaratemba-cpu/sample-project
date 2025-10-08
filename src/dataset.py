def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
