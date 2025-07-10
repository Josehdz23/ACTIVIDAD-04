#Manejo para agregar medicamentos

medicamentos = []
def agregar_Medicamentos():
    while True:
        nombreMedicamento = input("\nIngrese el nombre del Medicamento: ")
        if not nombreMedicamento is nombreMedicamento.isspace():
            medicamentos.append(nombreMedicamento)
            print("Se ha agregado el medicamento")
            break
        else:
            print("Debe de ingresar un medicamento!!!")

def entregar_Medicamentos():
    if(len(medicamentos) > 0):
        print(f"\nSe entregara el medicamento {medicamentos.pop()}")
    else:
        print("\nNo hay medicamentos para entregar!")

def mostrar_Medicamentos():
    cont = len(medicamentos)
    print("\n- - - - - MEDICAMENTOS - - - - -")
    if (len(medicamentos) > 0):
        for i in medicamentos:
            print(f"Medicamento {cont}: {i}")
            cont = cont - 1
    else:
        print("\nNo hay medicamentos que mostrar")

