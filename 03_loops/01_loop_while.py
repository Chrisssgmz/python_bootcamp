# 01_loop_while.py
# This program demonstrates the use of a while loop in Python.

# while with simple condition

count = 0

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment count by 1

print("Finished counting!")

# while loop with break statement

count = 0

while count <= 10:
    print(f"Count is: {count}")
    if count == 5:
        print("Count reached 5, breaking the loop.")
        break  # Exit the loop when count is 5
    count += 1

# while loop with continue statement

count = 0

while count <= 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(f"Count is: {count} (odd number)")

# while loop with else clause

count = 0

while count < 3:
    print(f"Count is: {count}")
    count += 1
else:
    print("Loop finished without being interrupted.")

# while loop with user input

while True:
    user_input = input("Enter a positive number (or 'exit' to quit): ").strip()

    if user_input.lower() == "exit":
        print("Exiting the loop.")
        break

    try:
        number = int(user_input)
        if number > 0:
            print(f"You entered {number}. That's a positive number!")
            break
        else:
            print("Please enter a positive number (greater than 0).")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")