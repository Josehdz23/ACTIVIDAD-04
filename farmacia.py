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
    if(len(medicamentos) > 0):
        print(f"Se entregara el medicamento {medicamentos.pop()}")
    else:
        print("No hay medicamentos para entregar!")

def mostrar_Medicamentos():
    if (len(medicamentos) > 0):
        for i in medicamentos:
            cont = 1
            print(f"Medicamento {cont}: {i}")
            cont = cont + 1
    else:
        print("No hay medicamentos que mostrar")


