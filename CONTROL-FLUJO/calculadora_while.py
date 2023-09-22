"""calculadora_while"""


entrada = ""
print(f"""
Bienvenidos a la calculadora
Para salir escribe Salir
Las operaciones son suma, resta, multi y div""")


#n2 = input("Ingresa segundo numero")




while True:
    if  not entrada:
        entrada = input("Ingresa Numero: ")
        if entrada.lower() == "salir":
            break
        entrada = int(entrada)
        operacion = input("Ingresa operacion: ")
        num2 = input("Ingresa el otro numero: ")
        num2 = int(num2)
        if operacion.lower() == "suma":
            entrada += num2
            print(entrada)
        elif operacion.lower() == "resta":
            entrada -= num2
            print(entrada)
        elif operacion.lower() == "multi":
            entrada *= num2
            print(entrada)
        elif operacion.lower() == "div":
            entrada /= num2
            print(entrada)
        else:
            print("Operacion no valida!")
        print(f"El resultado es {entrada}")