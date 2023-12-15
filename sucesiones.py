# UNIVERSIDAD DEL VALLE - FUNDAMENTOS DE PROGRAMACION ORIENTADA A EVENTOS (LABORATORIO 3)
#AUTORES: DANIEL JOSE ENRIQUEZ RANGEL, COD: 2240920 Y JUAN SEBASTIAN VIEDMAN, COD: 2242562
#CALCULO DE SERIES

''' 
    PSEUDOCODIGO:
    abrir bucle (mientras o while) = y asignarlo verdadero o true:
        imprimir: calculo de series
        imprimir: para seleccionar el tipo de sucesión
        imprimir("1- Geométrica ó 2- Aritmética ")
        crear variable de entrada 1: opcionSucesion = tipo entero (entrada por consola: ("Escriba el tipo de sucesión que desea calcular: "))
        crear variable de entrada 2: valorInicio = tipo entero (entrada por consola: ("Escriba el valor de inicio de la sucesión: "))
        crear variable de entrada 3 cantDigitos = tipo entero (entrada por consola: ("Escriba la cantidad de digitos de la sucesion: "))
        crear variable de entrada 4 valorCrecimiento = tipo entero(entrada por consola: ("Escriba el valor de crecimiento de la sucesión: "))
    
        #Aqui estaran todas la operaciones
            si(opcionSucesion es igual a 1):
                para i hasta el rango de (cantDigitos):
                    resultado = valorInicio * (valorCrecimiento ** i)
                    imprimir(resultado)
             
            sino(opcionSucesion es igual a 2):
                para i hasta el rango (valorInicio, valorInicio + cantDigitos * valorCrecimiento, valorCrecimiento):
                    imprimir(i) 
'''                    
while True:
    print("---------CALCULO DE SERIES--------- \n")
    print("Para seleccionar el tipo de sucesión: \n")
    print("1- Geométrica ó 2- Aritmética \n")
    opcionSucesion = int(input("Escriba el tipo de sucesión que desea calcular: "))
    valorInicio = int(input("Escriba el valor de inicio de la sucesión: "))
    cantDigitos = int(input("Escriba la cantidad de digitos de la sucesion: "))
    valorCrecimiento = int(input("Escriba el valor de crecimiento de la sucesión: "))
    
    #OPERACIONES
    if(opcionSucesion == 1):
         for i in range(cantDigitos):
            resultado = valorInicio * (valorCrecimiento ** i)
            print(resultado)
             
    
    elif(opcionSucesion == 2):
        for i in range(valorInicio, valorInicio + cantDigitos * valorCrecimiento, valorCrecimiento):
            print(i) 
            