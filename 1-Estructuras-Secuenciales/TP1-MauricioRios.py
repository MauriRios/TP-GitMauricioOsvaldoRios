import math


# 1)
print("Hola Mundo")

# 2)
nombre = input("Escriba su nombre: ")
print(f"Hola {nombre}!")

# 3)
nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = int(input("Escriba su edad: "))
paisDeResidencia = input("Escriba su País de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {paisDeResidencia}")

# 4)
radio = float(input("Ingrese el radio del círculo: "))

#NOTA: uso la libreria math para dar un calculo mas especifico, se podria definir pi pero
#con un numero estimado y usarlo en lugar de math, pero esto nos daria una aproximacion
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# 5)
segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos // 3600  
resto = segundos % 3600
minutos = resto // 60  
segundosRestantes = resto % 60

print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundosRestantes} segundos.")

# 6)
numero = int(input("Ingrese un número: "))
index = 0

for index in range(11):
 print(f" {numero} * {index} = {numero * index}")

# 7)
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"La suma entre ambos numeros es: {suma}")
print(f"La division entre ambos numeros es: {division}")
print(f"La multiplicacion entre ambos numeros es: {multiplicacion}")
print(f"La resta entre ambos numeros es: {resta}")

# 8)
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc}")

# 9)
gradosCelcius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = (9/5) * gradosCelcius + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# 10)
numero1 = int(input("Ingrese su 1er numero: "))
numero2 = int(input("Ingrese su 2do numero: "))
numero3 = int(input("Ingrese su 3er numero: "))

sumaTotal = numero1 + numero2 + numero3
promedio = sumaTotal / 3

print(f"El promedio de los 3 números es: {promedio}")

