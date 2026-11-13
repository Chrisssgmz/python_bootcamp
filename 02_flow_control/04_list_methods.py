# 04_list_methods.py
# Lists have many built-in methods that allow you to manipulate and interact with them.

list_methods = ["append", "extend", "insert", "remove", "pop", "clear", "index", "count", "sort", "reverse"]

int_list = [5, 2, 9, 1, 5, 6]

# append() - adds an item to the end of the list
int_list.append(10)
print(int_list)  # [5, 2, 9, 1, 5, 6, 10]

# insert() - adds an item at a specified index
int_list.insert(2, 15)
print(int_list)  # [5, 2, 15, 9, 1, 5, 6, 10]

# extend() - adds multiple items to the end of the list
int_list.extend([20, 25])
print(int_list)  # [5, 2, 15, 9, 1, 5, 6, 10, 20, 25]

# remove() - removes the first occurrence of a specified value
int_list.remove(5)

# pop() - removes and returns the item at a specified index (default is the last item)
popped_item = int_list.pop(3)

# del - removes an item at a specified index
del int_list[0]

# clear() - removes all items from the list
int_list.clear()

int_list = [5, 2, 9, 1, 5, 6]

# delete a range of items using del
del int_list[1:4]
print(int_list)  # [5, 6]

# sort() - sorts the list in ascending order
int_list = [5, 2, 9, 1, 5, 6]

int_list.sort()
print(int_list)  # [1, 5, 5, 6, 9]

# sorted() - returns a new sorted list without modifying the original list
int_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(int_list)
print(sorted_list)  # [1, 5, 5, 6, 9]
print(int_list)  # [5, 2, 9, 1, 5, 6]

# string methods can also be used with lists of strings
str_list = ["banana", "apple", "cherry"]

# sort() - sorts the list of strings in alphabetical order
str_list.sort()
print(str_list)  # ['apple', 'banana', 'cherry']

# len() - returns the number of items in the list
print(len(str_list))  # 3

# count() - returns the number of occurrences of a specified value
print(int_list.count(5))  # 2

# in - checks if a value is in the list
print(5 in int_list)  # True

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.