
def rombo_solido():
    try:
        n = int(input("Introduce la altura del diamante: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()

    for i in range(1, n + 1):
        espacios = n - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

    for i in range(n - 1, 0, -1):
        espacios = n - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

rombo_solido()
