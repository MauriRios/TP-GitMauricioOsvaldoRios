

#1)

# Usamos range desde 4 hasta 100 inclusive, de 4 en 4
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


#2)

# Creo la lista
comidas = ["pizza", "hamburguesa", "sushi", "empanada", "helado"]

# Muestro el penúltimo elemento
print(comidas[-2])


#3)

# Creo la lista vacía
lista_vacia = []

# Agrego tres palabras
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")

# Imprimo la lista
print(lista_vacia)


#4)

# Lista dada
animales = ["perro", "gato", "conejo", "pez"]

# Cambio el segundo valor (índice 1)
animales[1] = "loro"

# Cambio el último valor (índice -1)
animales[-1] = "oso"

# Imprimo la lista
print(animales)


#5)

numeros = [8, 15, 3, 22, 7] # Define una lista de números
numeros.remove(max(numeros)) # Busca con el metodo "max" el numero maximo de la lista y lo elimina
print(numeros)  # Imprime la lista sin el número mayor


#6)

numeros = list(range(10, 31, 5))    # Crea una lista de números del 10 al 30, de 5 en 5, el 31 es para que incluya el 30
print(numeros[:2])  # Imprime los dos primeros elementos de la lista


#7)

autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo índices 1 y 2
autos[1] = "mustang"
autos[2] = "camaro"

print(autos)


#8)

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)


#9)

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)


#10)

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)
