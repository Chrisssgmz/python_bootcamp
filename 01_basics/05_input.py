# 05_input.py
# input() function: The input() function is used to take input from the user. It

name = input("What is your name?\n")
print(f"Hello, {name}!")

age = input("What is your age?\n")
print(f"You are {age} years old.")

country, city = input("What is your country and city?\n").split(",")
print(f"You are from {city.strip()} in {country.strip()}.")