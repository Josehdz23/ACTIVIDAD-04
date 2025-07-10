from collections import deque
cola = deque()
def ingreso():
    while True:
        nombre = input("\nIngrese su nombre: ")
        if nombre.strip() != "":
            cola.append(nombre)
            print("Se ha registrado con exito")
            break
        else:
            print("\nNo es valido el nombre...")

def atender():
    if len(cola) > 0:
        a = cola.popleft()
        print(f"\nSe ha atendido a {a}")
    else:
        print("\nNo hay pacientes que atender...")

def mostrar_cola():
    if len(cola) > 0:
        print("\n---Pacientes---")
        s = 1
        for i in cola:
            print(f"-{s} {i}")
            s += 1
    else:
        print("\nLa cola esta vacia")