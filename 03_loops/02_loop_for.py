# 02_loop_for
# This script demonstrates the use of for loops in Python with various examples.

fruits = ["apple", "banana", "cherry", "orange", "grape"]
string = "Hello, World!"

# for loop with a list
for fruit in fruits:
    print(f"I like {fruit}.")

# for loop with a string
for char in string:
    print(char)

# enumerate function to get index and value
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# for loop with range function
for i in range(0, 10, 2): # Loop from 0 to 9 with a step of 2
    print(f"Number: {i}")

# loop for inside a loop (nested loops)

nested_numbers = [1, 2, 3, 4, 5]
nested_vowels = ["a", "e", "i", "o", "u"]

for vowel, number in zip(nested_vowels, nested_numbers): # Using zip to iterate over two lists simultaneously
    print(f"Vowel: {vowel}, Number: {number}")

# for loop with break statement
animals = ["cat", "dog", "rabbit", "hamster", "parrot"]
for index, animal in enumerate(animals):
    print(f"Animal: {animal}")
    if animal == "rabbit":
        print(f"Found a rabbit at index {index}, breaking the loop.")
        break  # Exit the loop when rabbit is found     

# for loop with continue statement
for index, animal in enumerate(animals):
    if animal == "hamster":
        print(f"Skipping hamster at index {index}.")
        continue  # Skip the rest of the loop for hamster
    print(f"Animal: {animal}")