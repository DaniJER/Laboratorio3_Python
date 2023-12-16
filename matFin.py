
# UNIVERSIDAD DEL VALLE - FUNDAMENTOS DE PROGRAMACION ORIENTADA A EVENTOS (LABORATORIO 3)
#AUTORES: DANIEL JOSE ENRIQUEZ RANGEL, COD: 2240920 Y JUAN SEBASTIAN VIEDMAN, COD: 2242562
#MATRICULA FINANCIERA

totalIngresos = 0.0
totalDescuentos = 0.0
totalIngresosNetos = 0.0

print("MATRICULA FINANCIERA - UNIVERSIDAD DEL VALLE")
cantEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))
nombrePlan = str(input("Ingrese el nombre del plan: "))

for i in range(cantEstudiantes):
    
    codEstudiante = int(input("Digite el codigo del estudiante: "))
    nombreEstudiante = str(input("Digite el nombre completo del estudiante: "))
    valorMatricula = float(input("Digite el valor a pagar por concepto de matricula: "))
    promedioEstudiante = float(input("Digite el promedio del estudiante: "))
    
    print("----------DATOS DEL ESTUDIANTE----------")
    print("Codigo: ",codEstudiante)
    print("Nombre: ",nombreEstudiante)
    print("Promedio: ",promedioEstudiante)
    
    def operacionesMatricula():
        global totalDescuentos, totalIngresos, totalIngresosNetos
        
        if  promedioEstudiante >= 4.7:
            descuento = 0.8 
            matriculaDescuento = valorMatricula * descuento;
            valorMatriculaFinal = valorMatricula - matriculaDescuento;
            print("Valor Matricula: ", valorMatricula)
            print("Porcentaje a descontar: ",descuento, "%")
            print("Valor descuento: ",matriculaDescuento)
            print("Total a pagar: ", valorMatriculaFinal)
            
            
        elif promedioEstudiante >= 4.5 and promedioEstudiante < 4.7:
                descuento = 0.3 
                matriculaDescuento = valorMatricula * descuento;
                valorMatriculaFinal = valorMatricula - matriculaDescuento;
                print("Valor Matricula: ", valorMatricula)
                print("Porcentaje a descontar: ",descuento, "%")
                print("Valor descuento: ",matriculaDescuento)
                print("Total a pagar: ", valorMatriculaFinal)
                
        elif promedioEstudiante >= 4.3 and promedioEstudiante < 4.5:
                descuento = 0.2 
                matriculaDescuento = valorMatricula * descuento;
                valorMatriculaFinal = valorMatricula - matriculaDescuento;
                print("Valor Matricula: ", valorMatricula)
                print("Porcentaje a descontar: ",descuento * 100, "%")
                print("Valor descuento: ",matriculaDescuento)
                print("Total a pagar: ", valorMatriculaFinal)
                
        totalIngresos += valorMatricula
        totalDescuentos += matriculaDescuento
        totalIngresosNetos = totalIngresos - totalDescuentos
    
    print("-----------DATOS MATRICULA FINANCIERA------------")
    operacionesMatricula()
         
print("=============RESUMEN - MATRICULA FINANCIERA ================")
print("Plan: ",nombrePlan)
print("total ingresos: ", totalIngresos)
print("Total descuentos: ", totalDescuentos)
print("total ingresos netos: ",totalIngresosNetos)
        
    