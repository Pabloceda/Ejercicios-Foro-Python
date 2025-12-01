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
        if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
            print("* ", end="")
        elif i <= lado // 2:
            if j == i:
                print("* ", end="")
            elif j == (lado - 1) - i:
                print("* ", end="")
            else:
                print("  ", end="")
        else:
            print("  ", end="")
    print()