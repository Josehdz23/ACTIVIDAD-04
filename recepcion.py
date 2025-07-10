from collections import deque
def recepcion():
    nombre = print("Ingrese su nombre: ")
    cola = deque()
    cola.append(nombre)
    for i in cola:
        print(i)