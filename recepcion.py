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
    if len(cola) > 0:
        a = cola.popleft()
        print(f"Se ha atendido a {a}")
    else:
        print("No hay pacientes que atender...")

def mostrar_cola():
    if len(cola) > 0:
        for i in cola:
            print(i)
    else:
        print("La cola esta vacia")