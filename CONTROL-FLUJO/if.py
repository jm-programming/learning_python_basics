"""CONDICIONALES IF ELIF ELSE"""


edad = input("Que edad tienes?")
edad = int(edad)

if edad > 17:
    print("Puedes entrar al cine")
    print("Enhorabuena amigo")
    
elif edad == 17:
    print("Espera un poco para ser mayor!")
else:
    print("No puedes ver peliculas para mayores de edad!")