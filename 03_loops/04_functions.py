# 04_functions.py
# Functions are a way to group code into reusable blocks. They allow you to define a set of instructions that can be executed whenever you call the function by its name.

name = "Chris"

def greet():
    """This function takes a name as an argument and prints a greeting message."""
    print(f"Hello, {name}! Welcome to the Python Bootcamp.")
    
greet()  # Calling the function to execute its code

# Function with a parameter
def greet_with_name(name: str):
    """This function takes a name as an argument and prints a personalized greeting message."""
    print(f"Hello, {name}! Welcome to the Python Bootcamp.")

greet_with_name("Alice")  # Calling the function with an argument

# Function with a return value
def add_numbers(a: int, b: int) -> int:
    """This function takes two numbers as arguments and returns their sum."""
    return a + b

# Calling the function with a return value
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is {result}.")

# Function with docstrings
def multiply_numbers(a: int, b: int) -> int:
    """
    This function takes two numbers as arguments and returns their product.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The product of the two numbers.
    """
    return a * b

# Calling the function with a return value
product = multiply_numbers(4, 6)
print(f"The product of 4 and 6 is {product}.")

# Default parameters

def multiply(a: int, b: int = 2):
    return a * b

print(multiply(4))

# key arguments

def greet_person(name: str, greeting: str = "Hello"):
    """This function takes a name and an optional greeting message as arguments and prints a personalized greeting."""
    print(f"{greeting}, {name}!")
    
greet_person("Bob")  # Using default greeting
greet_person("Bob", greeting="Hi")  # Using a custom greeting

# positional arguments

def describe_person(name: str, age: int):
    """This function takes a name and age as arguments and prints a description."""
    print(f"{name} is {age} years old.")    
    
describe_person(name="Alice", age=30)  # Using positional arguments

# key args 
def add_numbers_with_key_args(*args: int | float) -> int | float:
    """
    This function takes any number of arguments and returns their sum.
    """
    total: int | float = 0
    for num in args:
        total += num
    return total

print(add_numbers_with_key_args(1, 2, 3, 4, 5, 1.5))  # Output: 16.5

# key argumnts with **kwargs

def print_person_info(**kwargs: str) -> None:
    """
    This function takes any number of keyword arguments and prints the person's information.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_person_info(name="Alice", age="30", city="New York")