

#1)

def imprimer_hola_mundo():
    print("Hola Mundo")

imprimer_hola_mundo()

#2)

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

input_nombre = input("Ingrese su nombre: ")

saludar_usuario(input_nombre)

#3)

def informacion_personal(nombre,apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

input_nombre = input("Ingrese su nombre: ")
input_apellido = input("Ingrese su apellido: ")
input_edad = int(input("Ingrese su edad: "))
input_residencia = input("Ingrese su residencia: ")

informacion_personal(input_nombre, input_apellido, input_edad, input_residencia)

#4)

def calcular_area_circulo(radio):
        area = 3.14 * (radio ** 2)
        return area

def calcular_perimetro_circulo(radio):
        perimetro = 2 * 3.14 * radio
        return perimetro

input_radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(input_radio)
perimetro = calcular_perimetro_circulo(input_radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#5)

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

input_segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(input_segundos)
print(f"{input_segundos} segundos son {horas} horas")


#6)

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


input_numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(input_numero)

#7)

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return suma, resta, multiplicacion, division # Retorna una tupla con los resultados (suma, resta, multiplicacion, division)


input_a = float(input("Ingrese el primer número: "))
input_b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(input_a, input_b) 

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#8)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


input_peso = float(input("Ingrese su peso en kg: "))
input_altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(input_peso, input_altura)
print(f"Su IMC es: {imc}")


#9)

def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


input_celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celcius_a_fahrenheit(input_celsius)
print(f"{input_celsius}°C son {fahrenheit}°F")


#10)

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


input_a = float(input("Ingrese el primer número: "))
input_b = float(input("Ingrese el segundo número: "))
input_c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(input_a, input_b, input_c)
print(f"El promedio es: {promedio}")


