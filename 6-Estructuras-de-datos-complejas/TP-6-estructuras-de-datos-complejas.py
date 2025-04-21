

#1)

precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melon": 3000,
    "Uva": 1450
}

precios_frutas.append("Naranja", 1200)
precios_frutas.append("Manzana", 1500)
precios_frutas.append("Pera", 2300)




#2)

precios_frutas["Ananá"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800


#3)

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


#4)

class Persona: # Definimos la clase Persona
    def __init__(self, nombre, pais, edad): # Inicializa los atributos de la persona
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self): # Método para imprimir un saludo
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Inicializamos la persona con sus atributos
# y llamamos al método saludar para que imprima su saludo
persona1 = Persona("Lucía", "Argentina", 30)
persona1.saludar()


#5)

import math

class Circulo: # Definimos la clase Circulo
    def __init__(self, radio): # Inicializa el radio del círculo
        self.radio = radio

    def calcular_area(self): # Método para calcular el área del círculo
        return math.pi * self.radio ** 2

    def calcular_perimetro(self): # Método para calcular el perímetro del círculo
        return 2 * math.pi * self.radio

# Inicializamos el círculo con su radio
# y llamamos a los métodos para calcular el área y el perímetro
circulo1 = Circulo(5)
print("Área:", circulo1.calcular_area())
print("Perímetro:", circulo1.calcular_perimetro())


#6)

def balanceado(cadena): # Creo metodo para verificar si la cadena está balanceada
    # Defino una lista vacía para almacenar los caracteres de apertura
    pila = []
    pares = {')': '(', '}': '{', ']': '['} # Defino un diccionario para los pares de caracteres

    for caracter in cadena: # Recorro cada caracter de la cadena
        if caracter in "({[": # Si el caracter es de apertura, lo agrego a la pila
            pila.append(caracter) # Agrego el caracter a la pila
        elif caracter in ")}]": # Si el caracter es de cierre, verifico si la pila está vacía o si el último caracter no es el correspondiente
            if not pila or pila.pop() != pares[caracter]: # Si la pila está vacía o el último caracter no es el correspondiente, retorno False
                return False # Retorno False
    # Si la pila está vacía al final, significa que todos los caracteres de apertura tienen su correspondiente cierre

    return not pila

# Ejemplos:
print(balanceado("({[()]})"))  # True
print(balanceado("({[})"))     # False
print(balanceado("(){}[]"))    # True
print(balanceado("([)]"))      # False



#7)

from collections import deque

class ColaBanco: # Definimos la clase ColaBanco
    # Esta clase simula una cola de clientes en un banco
    def __init__(self): # Inicializa la cola vacía
        self.cola = deque() # Inicializa la cola como una deque (double-ended queue) para eficiencia en las operaciones de encolar y desencolar

    def encolar(self, cliente): # Encola un cliente al final de la fila
        self.cola.append(cliente)
        print(f"Cliente '{cliente}' agregado a la fila.")

    def desencolar(self): # Desencola al primer cliente de la fila
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Cliente '{cliente}' atendido.")
            return cliente
        else:
            print("No hay clientes en la fila.")
            return None

    def siguiente_cliente(self): # Muestra el siguiente cliente sin desencolarlo
        if self.cola:
            print(f"El siguiente cliente es: {self.cola[0]}")
            return self.cola[0]
        else:
            print("No hay clientes en la fila.")
            return None

# Ejemplo de uso
banco = ColaBanco()
banco.encolar("Juan")
banco.encolar("Ana")
banco.encolar("Luis")

banco.siguiente_cliente()  # Ana es el siguiente porque Juan esta en la fila para ser atendido
banco.desencolar() # Juan es atendido
banco.desencolar() # Ana es atendida
banco.siguiente_cliente() # Luis es el siguiente porque Ana ya fue atendida



#8)

class Nodo: # Definimos la clase Nodo para la lista enlazada
    # Cada nodo tiene un valor y un puntero al siguiente nodo
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada: # Definimos la clase ListaEnlazada
    # Esta clase representa una lista enlazada simple
    def __init__(self): # Inicializa la lista vacía
        self.cabeza = None # La cabeza de la lista es None al inicio

    def insertar_al_inicio(self, valor): # Inserta un nuevo nodo al inicio de la lista
        # Crea un nuevo nodo con el valor dado y lo coloca al inicio de la lista
        nuevo_nodo = Nodo(valor) # Crea un nuevo nodo
        nuevo_nodo.siguiente = self.cabeza # El siguiente del nuevo nodo apunta a la cabeza actual
        self.cabeza = nuevo_nodo # La cabeza ahora es el nuevo nodo
        # Actualiza la cabeza de la lista para que apunte al nuevo nodo
        print(f"Insertado '{valor}' al inicio de la lista.")

    def recorrer(self): # Recorre la lista e imprime los valores de cada nodo
        # Recorre la lista desde la cabeza hasta el final, imprimiendo los valores de cada nodo
        actual = self.cabeza # Comienza desde la cabeza de la lista
        print("Valores en la lista:") 
        while actual: # Mientras haya nodos en la lista
            # Imprime el valor del nodo actual
            print(f"-> {actual.valor}") 
            actual = actual.siguiente # Avanza al siguiente nodo

    def invertir(self): # Agrego método para invertir la lista enlazada en el punto 9
        anterior = None # Inicializa el nodo anterior como None para el primer nodo de la lista
        actual = self.cabeza # Comienza desde la cabeza de la lista para invertirla 
        # Recorre la lista y va invirtiendo los enlaces entre los nodos en cada iteración

        while actual: # Mientras haya nodos en la lista
            siguiente = actual.siguiente # Guarda el siguiente nodo
            actual.siguiente = anterior # Invierto el enlace del nodo actual
            anterior = actual # Muevo el nodo anterior al nodo actual
            actual = siguiente # Avanzo al siguiente nodo

        self.cabeza = anterior # Al final, la cabeza de la lista es el último nodo procesado

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_inicio(1)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(3)
lista.recorrer()


#9)

print("Lista original:") 
lista.recorrer() # Imprime la lista original del punto 8

lista.invertir() # Invierte la lista enlazada del punto 8

print("Lista invertida:")
lista.recorrer() # Imprime la lista invertida del punto 8



