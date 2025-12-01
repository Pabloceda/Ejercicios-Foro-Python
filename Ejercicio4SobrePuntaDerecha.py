# Cuadrado con diagonales y borde relleno
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
        # Parte superior del chevron (incluyendo la fila central)
        # La condición j == i + 1 dibuja la diagonal desplazada
        elif i <= lado // 2 and j == i + 1:
            print("* ", end="")
        # Parte inferior del chevron
        # La condición j == lado - i dibuja la diagonal inversa desplazada
        elif i > lado // 2 and j == lado - i:
             print("* ", end="")
        else:
            print("  ", end="")
    print() # Salto de línea al final de cada fila