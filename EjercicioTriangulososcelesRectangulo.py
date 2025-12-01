def dibujar_flecha_hueca():
    try:
        n = int(input("Introduce la altura de la figura: "))
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")
        exit()

    if n <= 0:
        print("La altura debe ser mayor que 0.")
        return

    for i in range(1, n + 1):
        espacios_izq = " " * (2 * (n - i))
        
        if i == 1:
            print(espacios_izq + "*")
        else:
            espacios_hueco = " " * (2 * i - 3)
            print(espacios_izq + "*" + espacios_hueco + "*")

    for i in range(n - 1, 0, -1):
        espacios_izq = " " * (2 * (n - i))
        
        if i == 1:
            print(espacios_izq + "*")
        else:
            espacios_hueco = " " * (2 * i - 3)
            print(espacios_izq + "*" + espacios_hueco + "*")

if __name__ == "__main__":
    dibujar_flecha_hueca()
