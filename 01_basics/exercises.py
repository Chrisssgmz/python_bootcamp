###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

print("Chris")
print("Tia juana")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"El tipo de datos de a es: {type(a)}")
print(f"El tipo de datos de b es: {type(b)}")
print(f"El tipo de datos de c es: {type(c)}")
print(f"El tipo de datos de d es: {type(d)}")
print(f"El tipo de datos de e es: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

int_num = int("12345")

print(f"La cadena \"12345\" convertida a entero es: {int_num}")
print(f"El entero {int_num} convertido a float es: {float(int_num)}")

float_num = 3.99

int_num = int(float_num)
print(f"El float {float_num} convertido a entero es: {int_num}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

name, age, height = input("Introduce tu nombre, edad y altura separados por comas:\n").split(",")
print(f"Hola! Me llamo {name.strip()} y tengo {age.strip()} años, mido {height.strip()} metros.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

Pi: float = 3.14159
rounded_pi = round(Pi)
integer_division = rounded_pi // 2
print(f"El resultado de la división entera es: {integer_division}")