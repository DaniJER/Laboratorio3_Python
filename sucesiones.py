# UNIVERSIDAD DEL VALLE - FUNDAMENTOS DE PROGRAMACION ORIENTADA A EVENTOS (LABORATORIO 3)
#AUTORES: DANIEL JOSE ENRIQUEZ RANGEL, COD: 2240920 Y JUAN SEBASTIAN VIEDMAN, COD: 2242562
#CALCULO DE SERIES
                 
while True:
    print("---------CALCULO DE SERIES--------- \n")
    print("Para seleccionar el tipo de sucesión: \n")
    print("1- Geométrica, 2- Aritmética y 3- Para salir \n")
    opcionSucesion = int(input("Escriba el tipo de sucesión que desea calcular: "))
    
    if opcionSucesion == 3:
        print("Saliendo del programa")
        break
    
    valorInicio = int(input("Escriba el valor de inicio de la sucesión: "))
    cantDigitos = int(input("Escriba la cantidad de digitos de la sucesion: "))
    valorCrecimiento = int(input("Escriba el valor de crecimiento de la sucesión: "))
    
    #OPERACIONES
    if opcionSucesion == 1:
        i = 0
        while i < cantDigitos:
            resultado = valorInicio * (valorCrecimiento ** i)
            print(resultado)
            i += 1
    
    elif opcionSucesion == 2:
        i = valorInicio
        while i < valorInicio + cantDigitos * valorCrecimiento:
            print(i)
            i += valorCrecimiento

            