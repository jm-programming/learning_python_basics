#CONDICIONALES IF ELIF ELSE


numero1 = int(input("INGRESA EL PRIMER NUMERO: "))  #recibe el primer numero y lo convierte a un numero entero
numero2 = int(input("INGRESA EL SEGUNDO NUMERO: ")) #recibe el segundo numero y lo convierte a un numero entero


if numero1 > numero2:
    resultado = f"""{numero1} es mayor que {numero2} """
elif numero1  < numero2:
    resultado = f"""{numero1} es menor que {numero2} """
else:
    resultado = f"""{numero1} y {numero2} son iguales """

print(resultado)