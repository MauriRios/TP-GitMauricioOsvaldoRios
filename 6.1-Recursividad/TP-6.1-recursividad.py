

#1)

def calculeElFactorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * calculeElFactorial(n - 1)  # Llamada recursiva
    
n = int(input("Ingrese un número entero positivo: "))
for i in range(1, n + 1):
    print(f"El factorial de {i} es: {calculeElFactorial(i)}")  # Imprime el factorial de cada número entre 1 y n

#2)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva
    
n = int(input("Ingrese la posición de la serie de Fibonacci: "))
fibonacci_series = [fibonacci(i) for i in range(n + 1)]  # Genera la serie de Fibonacci hasta la posición n
print(f"Serie de Fibonacci hasta la posición {n}: {fibonacci_series}")  # Imprime la serie completa

#3)

def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Llamada recursiva
# Pedir datos al usuario
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calcular y mostrar el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")


#4)

def decimal_a_binario(n):
    if n < 0:
        raise ValueError("El número debe ser entero positivo") # Verifica si el número es negativo, si lo es lanza un una excepción
    if n == 0:  # Caso base
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  # Llamada recursiva
# Pedir datos al usuario
n = int(input("Ingrese un número entero positivo: "))
# Calcular y mostrar el resultado
resultado = decimal_a_binario(n)
if resultado == "":
    resultado = "0"  # Si el número es 0, su representación binaria es "0"
print(f"El número {n} en binario es: {resultado}")  # Imprime el resultado


#5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:  # Caso base
        return True
    else:
        if palabra[0] == palabra[-1]:  # Compara el primer y último carácter
            return es_palindromo(palabra[1:-1])  # Llamada recursiva con la subcadena sin los extremos
        else:
            return False  # Si no son iguales, no es un palíndromo
palabra = input("Ingrese una palabra: ").lower()  # Convierte la palabra a minúsculas           
print(es_palindromo(palabra)) # Imprime el resultado de la función


#6)

def suma_digitos(n):
    if n == 0:  # Caso base
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)  # Llamada recursiva al dividir por 10 se obtiene el número sin el último dígito
                                               # y se suma el último dígito (n % 10) a la suma de los dígitos restantes,
                                               # cuando obtenemos 0 se sale del bucle y se devuelve la suma
n = int(input("Ingrese un número entero positivo: "))
print(suma_digitos(n)) 

#7)

def contar_bloques(n):
    if n == 1:  # Caso base
        return 1
    else:
        return n + contar_bloques(n - 1)  # Llamada recursiva al nivel siguiente
n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(contar_bloques(n))  # Imprime el resultado


#8)

def contar_digito(numero, digito):
    if digito < 0 or digito > 9:  # Verifica si el dígito está en el rango válido
        raise ValueError("El dígito debe estar entre 0 y 9")
    if numero < 0:  # Verifica si el número es negativo
        raise ValueError("El número debe ser entero positivo")
    if numero == 0:  # Caso base: ya no quedan más dígitos que revisar
        return 0
    else:
        # Verifica si el último dígito coincide con el dígito buscado
        # Si coincide, suma 1 a la cuenta, de lo contrario suma 0
        coincidencia = 1 if numero % 10 == digito else 0 
        # Llama recursivamente con el resto del número
        return coincidencia + contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese un dígito del 0 al 9: "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}")
