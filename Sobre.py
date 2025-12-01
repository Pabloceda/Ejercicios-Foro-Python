#Figura sobre Punta hacia abajo

try:
    lado = int(input("Introduce el lado del cuadrado: "))
except ValueError:
    print("Por favor, introduce un número entero.")
    exit()

print(f"Figura para n={lado}:")
print()

for i in range(lado):
    for j in range(lado):
        # Bordes del cuadrado
        if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
            print("* ", end="")
        
        # Pico hacia abajo (forma de V en la mitad superior)
        # Solo dibujamos si estamos en la mitad superior o centro (i <= lado // 2)
        elif i <= lado // 2:
            # Diagonal izquierda (baja de izquierda a derecha)
            # Ecuación: j = i
            if j == i:
                print("* ", end="")
            # Diagonal derecha (baja de derecha a izquierda / sube de centro a derecha)
            # Ecuación: j = (lado - 1) - i
            elif j == (lado - 1) - i:
                print("* ", end="")
            else:
                print("  ", end="")
        else:
            print("  ", end="")
    print() # Salto de línea al final de cada fila