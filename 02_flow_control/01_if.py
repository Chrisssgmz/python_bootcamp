# 01_if.py
# if statements are used to make decisions in your code. They allow you to execute certain blocks of code based on conditions.

age = 18

# if statement
if age >= 18:
    print(f"You are an adult, you're {age} years old.")
elif age >= 13:
    print(f"You are a teenager, you're {age} years old.")
else:
    print(f"You are a child, you're {age} years old.")
    
age = 25
driver_license = True

# and
if age >= 18 and driver_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")
    
second_age = 15

# or
if second_age >= 18 or driver_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")
    
# not
if not driver_license:
    print("You need a driver's license to drive.")
    
# Nested if statements
if age >= 18:
    if driver_license:
        print("You are eligible to drive.")
    else:
        print("You need a driver's license to drive.")
else:
    print("You are not eligible to drive.")
    
# ternary operator
result = "You are eligible to drive." if age >= 18 and driver_license else "You are not eligible to drive."
print(result)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num_1 = int(input("Introduce el primer número: "))
num_2 = int(input("Introduce el segundo número: "))

if num_1 > num_2:
    print(f"El primer número ({num_1}) es mayor que el segundo ({num_2}).")
elif num_1 < num_2:
    print(f"El segundo número ({num_2}) es mayor que el primer ({num_1}).")
else:
    print(f"Los dos números son iguales ({num_1}).")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num_1 = int(input("Introduce el primer número: "))
num_2 = int(input("Introduce el segundo número: "))
operation = input("Introduce la operación (+, -, *, /): ")

if operation == "+":
    result = num_1 + num_2
    print(f"El resultado de {num_1} + {num_2} es {result}.")
elif operation == "-":
    result = num_1 - num_2
    print(f"El resultado de {num_1} - {num_2} es {result}.")
elif operation == "*":
    result = num_1 * num_2
    print(f"El resultado de {num_1} * {num_2} es {result}.")
elif operation == "/":
    if num_2 != 0:
        result = num_1 / num_2
        print(f"El resultado de {num_1} / {num_2} es {result}.")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operación no válida.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

user_age = int(input("Introduce tu edad: "))

if user_age >= 0 and user_age <= 2:
    print("Eres un bebé.")
elif user_age >= 3 and user_age <= 12:
    print("Eres un niño.")
elif user_age >= 13 and user_age <= 17:
    print("Eres un adolescente.")
elif user_age >= 18 and user_age <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")