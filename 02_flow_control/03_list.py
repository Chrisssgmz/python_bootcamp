# 03_list.py
# Lists are used to store multiple items in a single variable. They are ordered, changeable, and allow duplicate values.

int_list = [1, 2, 3, 4, 5]
str_list = ["apple", "banana", "cherry"]

empty_list = []
list_with_lists = [[1, 2, 3], [4, 5, 6]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# accessing list items by index
print(int_list[0])  # 1
print(str_list[0])  # apple
print(matrix[0][0])  # 1
print(int_list[-1])  # 5

# slicing lists
print(int_list[1:4])  # [2, 3, 4]
print(int_list[1:2])  # [2]
print(int_list[:2])  # [1, 2]
print(int_list[3:])  # [4, 5]

# modifying list items
int_list[0] = 10
print(int_list)  # [10, 2, 3, 4, 5]

# adding items to a list
int_list.append(6)  # adds 6 to the end of the list

int_list += [7, 8, 9]  # adds multiple items to the end of the list
print(int_list)  # [10, 2, 3, 4, 5, 6, 7, 8, 9

# get longth of a list
print(len(int_list))  # 9

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]