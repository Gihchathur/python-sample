def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the division of a by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Addition: ", add(2, 3))
    print("Subtraction: ", subtract(5, 2))
    print("Multiplication: ", multiply(3, 4))
    print("Division: ", divide(10, 2))
