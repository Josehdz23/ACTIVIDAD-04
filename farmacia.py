#Manejo para agregar medicamentos

medicamentos = []
def agregar_Medicamentos():
    while True:
        nombreMedicamento = input("Nombre Medicamento: ")
        if not nombreMedicamento is nombreMedicamento.isspace():
            medicamentos.append(nombreMedicamento)
        else:
            print("Debe de ingresar un medicamento!!!")



