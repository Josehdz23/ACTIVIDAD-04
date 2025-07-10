#Manejo para agregar medicamentos

medicamentos = []
def agregar_Medicamentos():
    while True:
        nombreMedicamento = input("Nombre Medicamento: ")
        if not nombreMedicamento is nombreMedicamento.isspace():
            medicamentos.append(nombreMedicamento)
        else:
            print("Debe de ingresar un medicamento!!!")

def entregar_Medicamentos():
    print(f"Se entregara el medicamento {medicamentos.pop()}")

def mostrar_Medicamentos():
    for i in medicamentos:
        cont = 1
        print(f"Medicamento {cont}: {i}")
        cont = cont + 1



