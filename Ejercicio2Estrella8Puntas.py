def imprimir_estrella():
    try:
        n = int(input("Introduce la altura de la estrella: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()

    if n % 2 == 0:
        print("El número debe ser impar.")
        return

    centro = n // 2

    for i in range(n):
        for j in range(n):
            if i == centro or j == centro or i == j or i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
        
    print(f"Figura para n={n}:")

imprimir_estrella()
