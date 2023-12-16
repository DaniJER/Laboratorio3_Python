# UNIVERSIDAD DEL VALLE - FUNDAMENTOS DE PROGRAMACION ORIENTADA A EVENTOS (LABORATORIO 3)
#AUTORES: DANIEL JOSE ENRIQUEZ RANGEL, COD: 2240920 Y JUAN SEBASTIAN VIEDMAN, COD: 2242562
#SUMAS REPETITIVAS

contador = 0
while True:
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    resultado = num1 + num2
    print("La suma es: ", resultado)
    
    contador += resultado
    
    opcion = str(input("Desea realizar otra suma (s/n)? : "))
    
    if opcion == "n":
        print("La suma total de todos los numeros digitados es: ", contador)
        print("Saliendo del programa")
        break
    