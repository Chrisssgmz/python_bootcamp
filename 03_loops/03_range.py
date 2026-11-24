# 03_range.py
# This script demonstrates the use of the range function in Python with various examples.

range_nums = range(10)  # Creates a range object from 0 to 9
print("Range from 0 to 9:", list(range_nums))

for num in range(5):  # Loop from 0 to 4
    print(f"Number: {num}")

for num in range(11, 0, -1):  # This will print numbers from 10 to 1
    print(f"Number: {num}")

num_list = list(range(1, 21))  # Creates a list of numbers from 1 to 20

for num in num_list:
    print(f"Number: {num}")

# counter 
for _ in range(3):  # Loop 3 times
    print("Hello, World!")