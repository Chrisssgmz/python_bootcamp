# 04_variables.py
# variables are used to store data in memory. They can be assigned a value using the assignment operator (=).

my_name = "chris"

print("my name is", my_name)

my_Age = 21
print("my age is", my_Age)

my_Age = 22
print("my age is", my_Age)

# Dynamic typing: Python is a dynamically typed language, which means that you don't have to declare the type of a variable when you create it. The type of a variable is determined at runtime based on the value assigned to it.
my_name = "chris"
print(type(my_name))

my_name = 21
print(type(my_name))

# f-strings: f-strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}.
print(f"my name is {my_name} and my age is {my_Age}")

# Constants: Constants are variables that are not meant to be changed. In Python, there is no built-in way to create constants, but you can use a naming convention to indicate that a variable is a constant. By convention, constants are usually written in all uppercase letters.
PI: float = 3.14159
print(f"PI is {PI}")

# Note: In Python, you can still change the value of a constant, but it's not recommended.
# PI = 3
# print(f"PI is {PI} but it should be 3.14159")