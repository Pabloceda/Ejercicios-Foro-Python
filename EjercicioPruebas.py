#Cuadrado vacio

lado = int(input("Introduce el lado del cuadrado: "))

for i in range(1, lado + 1):
    if i == 1 or i == lado:
        print("* " * lado)
    else:
        print("*" + "  " * (lado - 2) + " *")