
def rombo_solido():
    try:
        n = int(input("Introduce la altura del diamante: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()

    # Upper half of the diamond (including the widest row)
    for i in range(1, n + 1):
        # Calculate leading spaces
        espacios = n - i
        # Calculate asterisks for the current row
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        # Calculate leading spaces
        espacios = n - i
        # Calculate asterisks for the current row
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

rombo_solido()
