from collections import deque
def ingreso():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.strip() != "":
            cola = deque()
            cola.append(nombre)
            print("Se ha registrado con exito")


def atender():
    a = cola.popleft()
    print(f"Se ha atendido a {a}")

def mostrar_cola():
    for i in cola:
        print(i)