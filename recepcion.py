from collections import deque
cola = deque()
def ingreso():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.strip() != "":
            cola.append(nombre)
            print("Se ha registrado con exito")
            break
        else:
            print("No es valido el nombre...")

def atender():
    a = cola.popleft()
    print(f"Se ha atendido a {a}")

def mostrar_cola():
    for i in cola:
        print(i)