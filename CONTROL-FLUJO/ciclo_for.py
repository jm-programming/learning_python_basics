"""ciclo for"""

buscar = 5


for item in range(20):
    print("ITERANDO EN EL NUMERO", item)
    if buscar == item:
        print("Encontrado" , item)
        break
else:
    print("No esta en el rango deseado!")
        
 