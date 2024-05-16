import math as mt

# ejercicio 1 #
def hola_mundo () -> str:
    return print ("hola mundo")
# hola_mundo()

# ejercicio 2 #
def letra_cancion () -> str:
    return print ("boca yo te amo\nsiempre te sigo a todos lados de corazon\nponga mas huevo") 
# letra_cancion()

# ejercicio 3 #
def raiz_de_dos () -> float :
    return round (mt.sqrt (2) , 4)
# raiz_de_dos()

# ejercicio 4 #
def factorial_de_dos () -> int :
    return mt.factorial(2)
# factorial_de_dos()

# ejercicio 5 #
def perimetro_circunferencia () -> float :
    r = input()
    return (mt.pi * r) 
#perimetro_circunferencia()

# ejercicio 6 # 
def imprimir_un_saludo () -> str:
    print("Decime tu nombre : ")
    nombre = input()
    return print (f"Okey , Hola {nombre} , ¿como estas?")
# imprimir_un_saludo()

# ejercicio 7 #
def raiz_cuadrada_de_n () -> float :
    print("Dame el numero :")
    numero = int(input()) 
    return round (mt.sqrt(numero) , 3 )
# raiz_cuadrada_de_n()

# ejercicio 8 # 
def farenheit_a_celsius () -> float :
    print("Dame los grados que te los calculo: ")
    grados = int(input())
    return (((grados - 32) * 5) /9)
# farenheit_a_celsius()

# ejercicio 9 #
def repetir_string () -> str: 
    print("Decime algo que lo repito: ")
    string = str(input())
    return string * 5
# repetir_string()

# ejercico 10 # 
def es_multiplo_de_n (x:int , y:int) -> bool: 
    if x % y == 0:
        return True
    else:
        return False 
# es_multiplo_de_n()

# ejercicio 11 # 
def es_par(x:int) -> bool:
    if (es_multiplo_de_n(2 , x )):
        return True 
    else:
        return False
# es_par()



