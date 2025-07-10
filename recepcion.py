from collections import deque
def ingreso():
    nombre = input("Ingrese su nombre: ")
    cola = deque()
    cola.append(nombre)
    print("Se ha registrado con exito")

def atender():
    a = cola.popleft()
    print(f"Se ha atendido a {a}")

def mostrar_cola():
    for i in cola:
        print(i)