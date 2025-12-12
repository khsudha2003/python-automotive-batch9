def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiple(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error Division by zero," 
    return a / b
print("Addition (5 + 3)=", add(5,3))
print("Subtraction (12 - 5) =", subtract(12, 5))
print("Multiplication (6 * 7) =", multiply(6, 7))

    