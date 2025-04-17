import random


#1)

for i in range(101):
    print(i)

#2)

numero = int(input("Ingrese un número entero: "))
# Convertimos el número a string para contar los dígitos
numero_str = str(abs(numero))  # usamos abs() para evitar el signo negativo
# Mostramos la cantidad de dígitos
print(f"Cantidad de dígitos: {len(numero_str)}")

#3)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = sum(range(min(a, b) + 1, max(a, b)))
print(f"La suma es: {suma}")


#4)

total = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"Total acumulado: {total}")



#5)

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intenta nuevamente.")


#6)

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


#7)

n = int(input("Ingrese un número entero positivo: "))
suma = sum(range(n + 1))
print(f"La suma de 0 a {n} es: {suma}")


#8)

CANTIDAD = 100  #Se puede cambiar este valor para hacer pruebas con menos números

pares = impares = positivos = negativos = 0

for _ in range(CANTIDAD):
    numero = int(input("Ingrese un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#9)

CANTIDAD = 5 #Se puede cambiar este valor para hacer pruebas con menos números
suma = 0

for _ in range(CANTIDAD):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} números es: {media}")



#10)

numero = int(input("Ingrese un número entero: "))
numero_invertido = int(str(abs(numero))[::-1])  #[::-1]: invierte el string 

if numero < 0:
    numero_invertido = -numero_invertido

print(f"Número invertido: {numero_invertido}")