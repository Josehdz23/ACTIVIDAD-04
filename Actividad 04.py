#Clinica medica
from farmacia import agregar_Medicamentos, entregar_Medicamentos, mostrar_Medicamentos
from recepcion import ingreso, mostrar_cola, atender

def menu():
    print("- - - - CLINICA - - - -\n1. Agregar paciente\n2. Atender pacientes\n3. Mostrar pacientes\n4. Agregar Medicamentos\n5. Entregar Medicamentos\n6. Mostrar medicamentos\n7. Salir")

def main():
    menu()
    while True:
        try:
            op = int(input("Selecciona una opcion: "))
            match op:
                case 1:
                    ingreso()
                case 2:
                    atender()
                case 3:
                    mostrar_cola()
                case 4:
                    agregar_Medicamentos()
                case 5:
                    entregar_Medicamentos()
                case 6:
                    mostrar_Medicamentos()
                case 7:
                    print("Saliendo...")
                case _:
                    print("Esa opción no existe!!")
        except Exception as ex:
            print(ex)

main()
