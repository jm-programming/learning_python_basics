"""CALCULADORA DE 2 NUMEROS"""

n1 = int(input("Ingrese primer numero "))
n2 = int(input("Ingrese segundo numero "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2


res = f"""
El resultado de la suma de los numeros es: {suma}.
El resultado de la resta de los numeros es: {resta}.
El resultado de la multiplicacion de los numeros es: {multi}.
El resultado de la division de los numeros es: {div}.
"""

print(res)
