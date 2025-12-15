# Default parameter values and Keyword Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice") # Default greeting
greet("Bob", greeting="Hi") # Keyword argument for greeting

# Passing a function to another function
def display_result(func, num1, num2):
    result = func(num1, num2)
    print(f"The result of the operation is: {result}")

def multiply_nums(n1, n2):
    return n1 * n2

def add_nums(n1, n2):
    return n1 + n2

display_result(multiply_nums, 5, 3) # Passing multiply_nums
display_result(add_nums, 5, 3) # Passing add_nums